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
USER_DATA = r"C:\Users\csern\AppData\Local\Temp\chrome_user_req_verify"
PORT = 9788

async def run_verification():
    print("=== STARTING USER REQUEST VERIFICATION ===")
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
                res = json.loads(await conn.read_message())
                if res.get("id") == req_id:
                    return res.get("result", {})

        async def eval_js(expr):
            res = await send_cdp("Runtime.evaluate", {
                "expression": expr,
                "awaitPromise": True,
                "returnByValue": True
            })
            return res.get("result", {}).get("value")

        await asyncio.sleep(1.5)

        # -------------------------------------------------------------
        # TEST 1: Header Button Heights (Language Switcher vs Contact)
        # -------------------------------------------------------------
        print("\n--- TEST 1: Header Button Heights ---")
        await send_cdp("Emulation.setDeviceMetricsOverride", {
            "width": 1280,
            "height": 800,
            "deviceScaleFactor": 1,
            "mobile": False
        })
        await asyncio.sleep(0.5)

        h_info = await eval_js("""
        (() => {
            const langContainer = document.querySelector('#lang-hu')?.parentElement;
            const contactBtn = document.querySelectorAll('header a[href="#kapcsolat"]')[1];
            return {
                langH: langContainer?.offsetHeight,
                contactH: contactBtn?.offsetHeight,
                langDisplay: window.getComputedStyle(langContainer).display,
                contactDisplay: window.getComputedStyle(contactBtn).display
            };
        })()
        """)
        print(f"  Language Switcher Height: {h_info['langH']}px")
        print(f"  Contact Button Height:    {h_info['contactH']}px")
        assert h_info["langH"] == h_info["contactH"] == 36, f"Expected 36px equal height, got lang={h_info['langH']}, contact={h_info['contactH']}"
        print("  [PASS] Header buttons have exact equal height (36px).")

        # -------------------------------------------------------------
        # TEST 2: Hero Spacing between H1 Lines
        # -------------------------------------------------------------
        print("\n--- TEST 2: Hero Headline Spacing ---")
        for width in [375, 768, 1280]:
            await send_cdp("Emulation.setDeviceMetricsOverride", {
                "width": width,
                "height": 800,
                "deviceScaleFactor": 1,
                "mobile": width < 768
            })
            await asyncio.sleep(0.3)
            gap = await eval_js("""
            (() => {
                const h1 = document.querySelector('h1');
                const line1 = h1.querySelector('[data-i18n="hero_h1_p1"]');
                const line2Container = line1.nextElementSibling;
                const r1 = line1.getBoundingClientRect();
                const r2 = line2Container.getBoundingClientRect();
                return {
                    r1_bottom: r1.bottom,
                    r2_top: r2.top,
                    gap: r2.top - r1.bottom
                };
            })()
            """)
            print(f"  Width {width}px: Line gap = {gap['gap']}px (r1_bottom={gap['r1_bottom']:.1f}, r2_top={gap['r2_top']:.1f})")
            assert gap["gap"] >= 10, f"At {width}px gap is too small: {gap['gap']}px"
        print("  [PASS] Hero lines have distinct, healthy vertical spacing across breakpoints.")

        # -------------------------------------------------------------
        # TEST 3: Catalog Title, Tabs, Paginator & Flip Animation
        # -------------------------------------------------------------
        # -------------------------------------------------------------
        # TEST 3: Catalog Title, Card-Embedded Counter & Flanking Arrows
        # -------------------------------------------------------------
        print("\n--- TEST 3: Streamlined Catalog Layout & Flanking Navigation ---")
        cat_info = await eval_js("""
        (() => {
            const titleEl = document.querySelector('[data-i18n="cat_section_title"]');
            const tagEl = document.querySelector('[data-i18n="cat_section_tag"]');
            const cardEl = document.getElementById('catalog-card');
            const counterEl = document.getElementById('cat-current-num');
            const isCounterInsideCard = cardEl && counterEl ? cardEl.contains(counterEl) : false;
            const hasTopTabs = !!document.getElementById('tab-btn-spreadable');
            const hasTopStepper = !!document.getElementById('cat-prev-btn');
            const hasSidePrev = !!document.getElementById('cat-side-prev');
            const hasSideNext = !!document.getElementById('cat-side-next');

            return {
                title: titleEl?.innerText.trim(),
                tag: tagEl?.innerText.trim(),
                counter: counterEl?.innerText.trim(),
                isCounterInsideCard,
                hasTopTabs,
                hasTopStepper,
                hasSidePrev,
                hasSideNext
            };
        })()
        """)
        print(f"  Catalog Tag:               {cat_info['tag']}")
        print(f"  Catalog Title:             {cat_info['title']}")
        print(f"  Initial Counter:           {cat_info['counter']}")
        print(f"  Counter Inside Card:       {cat_info['isCounterInsideCard']}")
        print(f"  Top Tabs Present:          {cat_info['hasTopTabs']}")
        print(f"  Top Stepper Present:       {cat_info['hasTopStepper']}")
        print(f"  Flanking Side Arrows:      Prev={cat_info['hasSidePrev']}, Next={cat_info['hasSideNext']}")

        assert "Lekvárok felhasználás szerint" in cat_info["title"], f"Catalog title mismatch: {cat_info['title']}"
        assert cat_info["isCounterInsideCard"], "Page counter MUST be inside #catalog-card at bottom center!"
        assert not cat_info["hasTopTabs"], "Top category tabs toolbar MUST be completely removed!"
        assert not cat_info["hasTopStepper"], "Top mini stepper buttons MUST be completely removed!"
        assert cat_info["hasSidePrev"] and cat_info["hasSideNext"], "Flanking side arrows must exist!"

        # Step forward using cat-side-next
        step1 = await eval_js("""
        new Promise((resolve) => {
            document.getElementById('cat-side-next').click();
            setTimeout(() => {
                resolve({
                    counter: document.querySelector('#cat-current-num')?.innerText,
                    title: document.querySelector('#cat-title')?.innerText
                });
            }, 400);
        })
        """)
        print(f"  After cat-side-next -> Counter: {step1['counter']}, Card: {step1['title']}")
        assert step1["counter"] == "02" and "Sütésálló" in step1["title"]

        # Step forward again to extra-jam
        step2 = await eval_js("""
        new Promise((resolve) => {
            document.getElementById('cat-side-next').click();
            setTimeout(() => {
                resolve({
                    counter: document.querySelector('#cat-current-num')?.innerText,
                    title: document.querySelector('#cat-title')?.innerText
                });
            }, 400);
        })
        """)
        print(f"  After cat-side-next -> Counter: {step2['counter']}, Card: {step2['title']}")
        assert step2["counter"] == "03" and "Extra" in step2["title"]

        # Step backwards using cat-side-prev
        step3 = await eval_js("""
        new Promise((resolve) => {
            document.getElementById('cat-side-prev').click();
            setTimeout(() => {
                resolve({
                    counter: document.querySelector('#cat-current-num')?.innerText,
                    title: document.querySelector('#cat-title')?.innerText
                });
            }, 400);
        })
        """)
        print(f"  After cat-side-prev -> Counter: {step3['counter']}, Card: {step3['title']}")
        assert step3["counter"] == "02" and "Sütésálló" in step3["title"]

        # Step backwards to spreadable
        step4 = await eval_js("""
        new Promise((resolve) => {
            document.getElementById('cat-side-prev').click();
            setTimeout(() => {
                resolve({
                    counter: document.querySelector('#cat-current-num')?.innerText,
                    title: document.querySelector('#cat-title')?.innerText
                });
            }, 400);
        })
        """)
        print(f"  After cat-side-prev -> Counter: {step4['counter']}, Card: {step4['title']}")
        assert step4["counter"] == "01" and "Kenhető" in step4["title"]
        print("  [PASS] Streamlined catalog with card-embedded counter and flanking arrows verified.")

        # -------------------------------------------------------------
        # TEST 3B: Language Integrity (HU & EN only, NO German)
        # -------------------------------------------------------------
        print("\n--- TEST 3B: Language Integrity (Bilingual Only) ---")
        lang_info = await eval_js("""
        (() => {
            return {
                hasLangHu: !!document.getElementById('lang-hu'),
                hasLangEn: !!document.getElementById('lang-en'),
                hasLangDe: !!document.getElementById('lang-de'),
                hasGermanInTranslations: typeof translations !== 'undefined' && 'de' in translations
            };
        })()
        """)
        print(f"  HU button: {lang_info['hasLangHu']}, EN button: {lang_info['hasLangEn']}, DE button: {lang_info['hasLangDe']}")
        print(f"  German in translations: {lang_info['hasGermanInTranslations']}")
        assert lang_info["hasLangHu"] and lang_info["hasLangEn"], "HU and EN buttons must exist!"
        assert not lang_info["hasLangDe"], "DE button must NOT exist!"
        assert not lang_info["hasGermanInTranslations"], "DE translations must NOT exist!"
        print("  [PASS] Strictly bilingual (HU/EN) verified. Zero German remnants.")

        # -------------------------------------------------------------
        # TEST 4: Zero Horizontal Overflow across 4 Breakpoints
        # -------------------------------------------------------------
        print("\n--- TEST 4: Zero Horizontal Overflow Invariant ---")
        for bp in [375, 768, 1024, 1440]:
            await send_cdp("Emulation.setDeviceMetricsOverride", {
                "width": bp,
                "height": 900,
                "deviceScaleFactor": 1,
                "mobile": bp < 768
            })
            await asyncio.sleep(0.3)
            overflow_info = await eval_js("""
            (() => {
                return {
                    scrollW: document.documentElement.scrollWidth,
                    clientW: document.documentElement.clientWidth
                };
            })()
            """)
            print(f"  Breakpoint {bp}px: scrollWidth={overflow_info['scrollW']}, clientWidth={overflow_info['clientW']}")
            assert overflow_info["scrollW"] <= overflow_info["clientW"] + 1, f"Horizontal overflow at {bp}px!"
        print("  [PASS] Zero horizontal overflow verified across all 4 breakpoints.")

        # -------------------------------------------------------------
        # SCREENSHOTS
        # -------------------------------------------------------------
        print("\n--- Capturing Verification Screenshots ---")
        await send_cdp("Emulation.setDeviceMetricsOverride", {
            "width": 1280,
            "height": 850,
            "deviceScaleFactor": 1,
            "mobile": False
        })
        await asyncio.sleep(0.4)
        
        # Screenshot Hero & Header
        shot_res = await send_cdp("Page.captureScreenshot", {"format": "png"})
        shot_path = os.path.join(SCREENSHOTS_DIR, "verify_task_hero_header.png")
        with open(shot_path, "wb") as f:
            f.write(base64.b64decode(shot_res["data"]))
        print(f"  [OK] Saved {shot_path}")

        # Scroll to catalog and capture desktop
        await eval_js("document.getElementById('termekek').scrollIntoView({ behavior: 'instant', block: 'start' });")
        await asyncio.sleep(0.4)
        shot_res2 = await send_cdp("Page.captureScreenshot", {"format": "png"})
        shot_path2 = os.path.join(SCREENSHOTS_DIR, "verify_task_catalog.png")
        with open(shot_path2, "wb") as f:
            f.write(base64.b64decode(shot_res2["data"]))
        print(f"  [OK] Saved {shot_path2}")

        # Mobile Screenshot of catalog (375px)
        await send_cdp("Emulation.setDeviceMetricsOverride", {
            "width": 375,
            "height": 812,
            "deviceScaleFactor": 1,
            "mobile": True
        })
        await asyncio.sleep(0.4)
        await eval_js("document.getElementById('termekek').scrollIntoView({ behavior: 'instant', block: 'start' });")
        await asyncio.sleep(0.4)
        shot_res3 = await send_cdp("Page.captureScreenshot", {"format": "png"})
        shot_path3 = os.path.join(SCREENSHOTS_DIR, "verify_task_catalog_mobile.png")
        with open(shot_path3, "wb") as f:
            f.write(base64.b64decode(shot_res3["data"]))
        print(f"  [OK] Saved {shot_path3}")

        print("\n=== ALL USER REQUEST VERIFICATION TESTS PASSED SUCCESSFULLY! ===")

    finally:
        try:
            conn.close()
        except:
            pass
        proc.terminate()

if __name__ == "__main__":
    asyncio.run(run_verification())
