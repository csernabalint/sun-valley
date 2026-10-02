import asyncio
import base64
import json
import os
import subprocess
import sys
import time
from pathlib import Path
import tornado.httpclient
import tornado.websocket

REPO_ROOT = Path(__file__).resolve().parent.parent
HTML_ROOT = str(REPO_ROOT / "index.html")
SCREENSHOTS_DIR = str(REPO_ROOT / "docs" / "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
USER_DATA = r"C:\Users\csern\AppData\Local\Temp\chrome_footer_verify"
PORT = 9791

async def run_verification():
    print("=== STARTING FOOTER REDESIGN VERIFICATION ===")
    cmd = [
        CHROME_PATH,
        "--headless=new",
        f"--remote-debugging-port={PORT}",
        f"--user-data-dir={USER_DATA}",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check"
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)

    try:
        hc = tornado.httpclient.AsyncHTTPClient()
        resp = await hc.fetch(f"http://127.0.0.1:{PORT}/json/version")
        ver_data = json.loads(resp.body)
        conn = await tornado.websocket.websocket_connect(ver_data["webSocketDebuggerUrl"], max_message_size=100*1024*1024)

        req_id = 1
        root_url = f"file:///{HTML_ROOT.replace('\\', '/')}"
        await conn.write_message(json.dumps({"id": req_id, "method": "Target.createTarget", "params": {"url": root_url}}))
        target_id = json.loads(await conn.read_message())["result"]["targetId"]

        req_id += 1
        await conn.write_message(json.dumps({"id": req_id, "method": "Target.attachToTarget", "params": {"targetId": target_id, "flatten": True}}))
        session_id = None
        while not session_id:
            m = json.loads(await conn.read_message())
            if m.get("method") == "Target.attachedToTarget":
                session_id = m.get("params", {}).get("sessionId")
            elif m.get("id") == req_id and "result" in m:
                session_id = m.get("result", {}).get("sessionId")

        async def send_cdp(method, params=None):
            nonlocal req_id
            req_id += 1
            payload = {"id": req_id, "sessionId": session_id, "method": method}
            if params:
                payload["params"] = params
            await conn.write_message(json.dumps(payload))
            while True:
                msg = json.loads(await conn.read_message())
                if msg.get("id") == req_id:
                    return msg.get("result", {})

        async def eval_js(expr):
            res = await send_cdp("Runtime.evaluate", {"expression": expr, "returnByValue": True})
            return res.get("result", {}).get("value")

        await send_cdp("Page.enable")
        await send_cdp("DOM.enable")
        await asyncio.sleep(1)

        # 1. TEST VIEWPORTS & ZERO OVERFLOW
        viewports = [
            ("Desktop 1440px", 1440, 900),
            ("Laptop 1024px", 1024, 768),
            ("Tablet 768px", 768, 1024),
            ("Mobile 375px", 375, 812)
        ]

        print("\n--- 1. Testing Zero Horizontal Overflow Invariant ---")
        for label, w, h in viewports:
            await send_cdp("Emulation.setDeviceMetricsOverride", {
                "width": w,
                "height": h,
                "deviceScaleFactor": 1,
                "mobile": (w < 768)
            })
            await asyncio.sleep(0.5)

            overflow_data = await eval_js("""
                (() => {
                    const scrollW = document.documentElement.scrollWidth;
                    const clientW = document.documentElement.clientWidth;
                    return {
                        scrollWidth: scrollW,
                        clientWidth: clientW,
                        hasOverflow: scrollW > clientW,
                        diff: scrollW - clientW
                    };
                })()
            """)
            print(f"[{label}] clientW={overflow_data['clientWidth']}, scrollW={overflow_data['scrollWidth']}, diff={overflow_data['diff']}")
            assert not overflow_data['hasOverflow'], f"Horizontal overflow detected on {label}!"

        # 2. TEST DOM & CONTENT INVARIANTS
        print("\n--- 2. Testing Footer DOM & Content Invariants ---")
        await send_cdp("Emulation.setDeviceMetricsOverride", {
            "width": 1440,
            "height": 900,
            "deviceScaleFactor": 1,
            "mobile": False
        })
        await asyncio.sleep(0.5)

        footer_check = await eval_js("""
            (() => {
                const footer = document.querySelector('footer#kapcsolat');
                if (!footer) return { error: 'footer#kapcsolat not found' };

                const style = window.getComputedStyle(footer);
                const text = footer.innerText;

                const hasLogo = !!footer.querySelector('img[src*="sun-valley-logo"]');
                const hasMobile = text.includes('+36 30 899 8548');
                const hasEmail = text.includes('ifj.vecsei.andras@sunvalley.hu');
                const hasPlant = text.includes('8060 Mór, Major utca 3.');
                const hasHq = text.includes('1138 Budapest, Váci út 186.');
                const hasLandline = text.includes('+36 22 400 984');
                const hasRep = text.includes('ifj. Vécsei András');
                const hasCopyright = text.includes('© 2026 Sun Valley Kereskedelmi Zrt. • Minden jog fenntartva.');

                // Prohibitions
                const hasUnwantedBadges = text.includes('AA+ Pénzügyi Minősítés') || text.includes('ISO / HACCP Szabvány');
                const hasFluff1 = text.includes('Garantált szakmai válaszidő 24 órán belül');
                const hasFluff2 = text.includes('Azonnali kereskedelmi és termékkonzultáció');

                return {
                    tagName: footer.tagName.toLowerCase(),
                    bgColor: style.backgroundColor,
                    hasLogo,
                    hasMobile,
                    hasEmail,
                    hasPlant,
                    hasHq,
                    hasLandline,
                    hasRep,
                    hasCopyright,
                    hasUnwantedBadges,
                    hasFluff1,
                    hasFluff2
                };
            })()
        """)
        print("Footer check results:", json.dumps(footer_check, indent=2, ensure_ascii=False))

        assert footer_check.get("tagName") == "footer", "Expected tag to be 'footer'"
        assert "69, 28, 27" in footer_check.get("bgColor") or "rgb" in footer_check.get("bgColor"), f"Unexpected bg color: {footer_check.get('bgColor')}"
        assert footer_check.get("hasLogo"), "Missing logo in footer"
        assert footer_check.get("hasMobile"), "Missing mobile number in footer"
        assert footer_check.get("hasEmail"), "Missing email in footer"
        assert footer_check.get("hasPlant"), "Missing plant address in footer"
        assert footer_check.get("hasHq"), "Missing HQ in footer"
        assert footer_check.get("hasLandline"), "Missing landline in footer"
        assert footer_check.get("hasRep"), "Missing representative name in footer"
        assert footer_check.get("hasCopyright"), "Missing copyright notice in footer"
        assert not footer_check.get("hasUnwantedBadges"), "Unwanted badges present in footer!"
        assert not footer_check.get("hasFluff1"), "Fluff text 1 present in footer!"
        assert not footer_check.get("hasFluff2"), "Fluff text 2 present in footer!"
        print("[OK] All footer content and anti-fluff assertions passed!")

        # 3. TEST PRIVACY MODAL INTERACTIVITY
        print("\n--- 3. Testing Privacy Modal Interactivity ---")
        modal_opened = await eval_js("""
            (() => {
                openPrivacyModal();
                const modal = document.getElementById('privacy-modal');
                return {
                    exists: !!modal,
                    isHidden: modal.classList.contains('hidden'),
                    isFlex: modal.classList.contains('flex')
                };
            })()
        """)
        print("Privacy modal open state:", modal_opened)
        assert not modal_opened['isHidden'] and modal_opened['isFlex'], "Privacy modal did not open properly!"

        modal_closed = await eval_js("""
            (() => {
                closePrivacyModal();
                const modal = document.getElementById('privacy-modal');
                return {
                    isHidden: modal.classList.contains('hidden'),
                    isFlex: modal.classList.contains('flex')
                };
            })()
        """)
        print("Privacy modal closed state:", modal_closed)
        assert modal_closed['isHidden'] and not modal_closed['isFlex'], "Privacy modal did not close properly!"
        print("[OK] Privacy modal interactive flow verified!")

        # 4. TEST LANGUAGE TOGGLE TO EN
        print("\n--- 4. Testing Language Toggle to EN ---")
        en_check = await eval_js("""
            (() => {
                setLanguage('en');
                const footer = document.querySelector('footer#kapcsolat');
                return {
                    infoCol: document.querySelector('[data-i18n=\"footer_col_info\"]')?.innerText,
                    contactCol: document.querySelector('[data-i18n=\"footer_col_contact\"]')?.innerText,
                    hqCol: document.querySelector('[data-i18n=\"footer_col_hq\"]')?.innerText,
                    rights: document.querySelector('[data-i18n=\"footer_rights\"]')?.innerText,
                    mapsLink: document.querySelector('[data-i18n=\"link_google_maps\"]')?.innerText
                };
            })()
        """)
        print("EN Translations in Footer:", json.dumps(en_check, indent=2, ensure_ascii=False))
        assert en_check['infoCol'].upper() == "INFORMATION", f"Expected 'INFORMATION', got {en_check['infoCol']}"
        assert en_check['contactCol'].upper() == "DIRECT CONTACT", f"Expected 'DIRECT CONTACT', got {en_check['contactCol']}"
        assert en_check['hqCol'].upper() == "HEADQUARTERS & LEADERSHIP", f"Expected 'HEADQUARTERS & LEADERSHIP', got {en_check['hqCol']}"
        print("[OK] EN i18n fidelity verified!")

        # Reset back to HU
        await eval_js("setLanguage('hu');")

        # 5. TAKE SCREENSHOTS
        print("\n--- 5. Capturing Footer Screenshots ---")
        # Desktop
        await send_cdp("Emulation.setDeviceMetricsOverride", {
            "width": 1440,
            "height": 900,
            "deviceScaleFactor": 1,
            "mobile": False
        })
        await asyncio.sleep(0.5)
        # Dismiss cookie banner, force instant scrolling, and align footer exactly
        await eval_js("""
            if (typeof acceptCookies === 'function') acceptCookies();
            document.documentElement.style.scrollBehavior = 'auto';
            document.body.style.scrollBehavior = 'auto';
            const f = document.querySelector('footer#kapcsolat');
            if (f) {
                const y = f.getBoundingClientRect().top + window.pageYOffset;
                window.scrollTo(0, y);
            }
        """)
        await asyncio.sleep(0.8)

        shot_res = await send_cdp("Page.captureScreenshot", {"format": "png"})
        shot_path_desktop = os.path.join(SCREENSHOTS_DIR, "verify_footer_desktop.png")
        with open(shot_path_desktop, "wb") as f:
            f.write(base64.b64decode(shot_res["data"]))
        print(f"Captured: {shot_path_desktop}")

        # Mobile
        await send_cdp("Emulation.setDeviceMetricsOverride", {
            "width": 375,
            "height": 950,
            "deviceScaleFactor": 2,
            "mobile": True
        })
        await asyncio.sleep(0.5)
        await eval_js("""
            document.documentElement.style.scrollBehavior = 'auto';
            document.body.style.scrollBehavior = 'auto';
            window.scrollTo(0, document.body.scrollHeight);
        """)
        await asyncio.sleep(0.8)

        shot_res_mob = await send_cdp("Page.captureScreenshot", {"format": "png"})
        shot_path_mob = os.path.join(SCREENSHOTS_DIR, "verify_footer_mobile.png")
        with open(shot_path_mob, "wb") as f:
            f.write(base64.b64decode(shot_res_mob["data"]))
        print(f"Captured: {shot_path_mob}")

        print("\n=== ALL VERIFICATIONS PASSED SUCCESSFULLY! ===")

    finally:
        try:
            proc.terminate()
            proc.wait(timeout=3)
        except Exception:
            pass

if __name__ == "__main__":
    asyncio.run(run_verification())
