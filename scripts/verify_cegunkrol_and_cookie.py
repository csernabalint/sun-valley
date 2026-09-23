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
USER_DATA = r"C:\Users\csern\AppData\Local\Temp\chrome_cegunkrol_verify"
PORT = 9799

async def run_verification():
    print("=== STARTING CÉGÜNKRŐL, TECHNOLÓGIA & COOKIE VERIFICATION ===")
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

        async def evaluate(expr):
            res = await send_cdp("Runtime.evaluate", {"expression": expr, "returnByValue": True})
            return res.get("result", {}).get("value")

        await send_cdp("Page.enable")
        await send_cdp("DOM.enable")

        # Set 1440px desktop viewport
        await send_cdp("Emulation.setDeviceMetricsOverride", {
            "width": 1440,
            "height": 900,
            "deviceScaleFactor": 1,
            "mobile": False
        })
        await asyncio.sleep(1.5)

        # 1. TEST CÉGÜNKRŐL SECTION
        print("\n--- TEST 1: Cégünkről Section Presence & Content ---")
        ceg_exists = await evaluate("!!document.getElementById('cegunkrol')")
        print(f"Section #cegunkrol exists: {ceg_exists}")
        assert ceg_exists, "Error: #cegunkrol not found!"

        ceg_tag = await evaluate("document.querySelector('#cegunkrol [data-i18n=\"about_tag\"]')?.textContent?.trim()")
        print(f"Cégünkről tag: {ceg_tag}")

        ceg_title_p1 = await evaluate("document.querySelector('#cegunkrol [data-i18n=\"about_title_p1\"]')?.textContent?.trim()")
        ceg_title_p2 = await evaluate("document.querySelector('#cegunkrol [data-i18n=\"about_title_p2\"]')?.textContent?.trim()")
        print(f"Cégünkről title: '{ceg_title_p1} {ceg_title_p2}'")

        ceg_p1 = await evaluate("document.querySelector('#cegunkrol [data-i18n=\"about_p1\"]')?.textContent?.trim()")
        print(f"Cégünkről p1 snippet: {ceg_p1[:80]}...")
        assert "30 évvel ezelőtt" in ceg_p1, "Error: 30 year heritage not mentioned in p1!"

        proof_count = await evaluate("document.querySelectorAll('#cegunkrol [data-i18n^=\"about_proof\"]').length")
        print(f"Cégünkről proof items: {proof_count}")
        assert proof_count >= 6, f"Expected 6 proof text elements (3 titles + 3 descs), got {proof_count}"

        # 2. TEST TECHNOLÓGIÁK SECTION
        print("\n--- TEST 2: Technológiák Section Asymmetric Layout ---")
        tech_exists = await evaluate("!!document.getElementById('technologia')")
        print(f"Section #technologia exists: {tech_exists}")
        assert tech_exists, "Error: #technologia not found!"

        hero_feature_title = await evaluate("document.querySelector('#technologia [data-i18n=\"tech_card1_title\"]')?.textContent?.trim()")
        print(f"Hero Feature Title: {hero_feature_title}")
        assert "Garantált Sütésállóság" in hero_feature_title, "Error: Hero feature title mismatch!"

        hero_check_count = await evaluate("document.querySelectorAll('#technologia [data-i18n^=\"tech_hero_check\"]').length")
        print(f"Hero feature checklist items: {hero_check_count}")
        assert hero_check_count == 3, f"Expected 3 checklist items, got {hero_check_count}"

        pillars = await evaluate("""
            Array.from(document.querySelectorAll('#technologia [data-i18n^=\"tech_card\"]:not([data-i18n=\"tech_card1_title\"]):not([data-i18n=\"tech_card1_desc\"])'))
                .filter(el => el.getAttribute('data-i18n').endsWith('_title'))
                .map(el => el.textContent.trim())
        """)
        print(f"Right-side pillars: {pillars}")
        assert len(pillars) == 3, f"Expected 3 pillars, got {len(pillars)}"

        # 3. TEST NAVIGATION (RIBBON)
        print("\n--- TEST 3: Navigation Menu Links & Ribbon Invariants ---")
        nav_data = await evaluate("""
            (() => {
                const links = Array.from(document.querySelectorAll('header nav a')).map(a => {
                    const rect = a.getBoundingClientRect();
                    return {
                        text: a.innerText.trim(),
                        href: a.getAttribute('href'),
                        x: Math.round(rect.x),
                        y: Math.round(rect.y),
                        width: Math.round(rect.width),
                        height: Math.round(rect.height),
                        whiteSpace: window.getComputedStyle(a).whiteSpace
                    };
                });
                const h = document.getElementById('main-nav').getBoundingClientRect();
                const headerRect = { x: Math.round(h.x), y: Math.round(h.y), width: Math.round(h.width), height: Math.round(h.height) };
                return { links, headerRect };
            })()
        """)
        labels = [l["text"] for l in nav_data["links"]]
        print(f"Desktop Nav items: {labels}")
        assert "Technológia" in labels, f"Expected 'Technológia' in nav, got: {labels}"
        assert not any("200" in l for l in labels), f"Error: 200 Celsius still found in nav labels: {labels}"
        assert not any("°C" in l for l in labels), f"Error: °C still found in nav labels: {labels}"

        # Invariant: No wrapping! Heights must be <= 30px
        for l in nav_data["links"]:
            print(f"Nav link '{l['text']}' height: {l['height']}px, y: {l['y']}px, white-space: {l['whiteSpace']}")
            assert l["height"] <= 30, f"Error: Nav link '{l['text']}' is wrapping onto multiple lines (height {l['height']}px)!"

        # Invariant: Identical vertical baselines across all links
        y_baselines = set(l["y"] for l in nav_data["links"])
        assert len(y_baselines) == 1, f"Error: Nav links are not on the same vertical baseline: {y_baselines}"

        # Mobile menu checks
        mob_tech = await evaluate("document.querySelector('#mobile-menu a[href=\"#technologia\"]')?.textContent?.trim()")
        print(f"Mobile Nav 'Technológia' link: '{mob_tech}'")
        assert mob_tech == "Technológia", f"Expected mobile link to be 'Technológia', got '{mob_tech}'"

        # Capture Header Ribbon Screenshot
        clip_box = {
            "x": nav_data["headerRect"]["x"],
            "y": nav_data["headerRect"]["y"],
            "width": nav_data["headerRect"]["width"],
            "height": nav_data["headerRect"]["height"],
            "scale": 1
        }
        shot_ribbon = await send_cdp("Page.captureScreenshot", {"format": "png", "clip": clip_box})
        shot_ribbon_path = os.path.join(SCREENSHOTS_DIR, "ribbon_desktop_1440.png")
        with open(shot_ribbon_path, "wb") as f:
            f.write(base64.b64decode(shot_ribbon["data"]))
        print(f"Captured Header Ribbon: {shot_ribbon_path}")

        # 4. TEST COOKIE BANNER
        print("\n--- TEST 4: Cookie Banner Interaction & LocalStorage ---")
        cookie_exists = await evaluate("!!document.getElementById('cookie-banner')")
        print(f"Cookie banner exists: {cookie_exists}")
        assert cookie_exists, "Error: #cookie-banner not found!"

        # Wait for the 800ms timer to show banner
        await asyncio.sleep(1.2)
        is_cookie_visible = await evaluate("!document.getElementById('cookie-banner').classList.contains('opacity-0')")
        print(f"Cookie banner is visible: {is_cookie_visible}")

        # Click accept button
        await evaluate("acceptCookies()")
        await asyncio.sleep(0.3)
        ls_consent = await evaluate("localStorage.getItem('sv_cookie_consent')")
        is_hidden_after_click = await evaluate("document.getElementById('cookie-banner').classList.contains('opacity-0')")
        print(f"LocalStorage consent value: '{ls_consent}', Banner hidden after accept: {is_hidden_after_click}")
        assert ls_consent == "accepted", "Error: localStorage consent not set to 'accepted'!"
        assert is_hidden_after_click, "Error: Cookie banner not hidden after accept!"

        # 5. TEST LANGUAGE SWITCHING (HU <-> EN)
        print("\n--- TEST 5: Language Switching (HU <-> EN) ---")
        await evaluate("setLanguage('en')")
        await asyncio.sleep(0.5)

        en_about_tag = await evaluate("document.querySelector('#cegunkrol [data-i18n=\"about_tag\"]')?.textContent?.trim()")
        en_about_title = await evaluate("document.querySelector('#cegunkrol [data-i18n=\"about_title_p1\"]')?.textContent?.trim()")
        en_nav_about = await evaluate("document.querySelector('nav a[href=\"#cegunkrol\"]')?.textContent?.trim()")
        print(f"EN About Tag: {en_about_tag}")
        print(f"EN About Title P1: {en_about_title}")
        print(f"EN Nav About: {en_nav_about}")
        assert "HUNGARIAN PROCESSING" in en_about_tag, f"Expected English tag, got '{en_about_tag}'"
        assert "About Us" in en_nav_about, f"Expected 'About Us', got '{en_nav_about}'"

        # Switch back to HU
        await evaluate("setLanguage('hu')")
        await asyncio.sleep(0.5)
        hu_about_tag = await evaluate("document.querySelector('#cegunkrol [data-i18n=\"about_tag\"]')?.textContent?.trim()")
        print(f"HU About Tag restored: {hu_about_tag}")
        assert "MAGYAR GYÁRTÁS" in hu_about_tag, f"Expected Hungarian tag, got '{hu_about_tag}'"

        # 6. TEST ZERO HORIZONTAL OVERFLOW ACROSS BREAKPOINTS
        print("\n--- TEST 6: Zero Horizontal Overflow Invariant ---")
        breakpoints = [
            ("Desktop", 1440, 900),
            ("Laptop", 1024, 768),
            ("Tablet", 768, 1024),
            ("Mobile", 375, 812)
        ]

        for name, width, height in breakpoints:
            await send_cdp("Emulation.setDeviceMetricsOverride", {
                "width": width,
                "height": height,
                "deviceScaleFactor": 1,
                "mobile": (width < 768)
            })
            await asyncio.sleep(0.5)

            overflow = await evaluate("""
                (() => {
                    const scrollW = document.documentElement.scrollWidth;
                    const clientW = document.documentElement.clientWidth;
                    return {
                        scrollW,
                        clientW,
                        hasOverflow: scrollW > clientW,
                        diff: scrollW - clientW
                    };
                })()
            """)
            print(f"[{name} - {width}px] scrollWidth: {overflow['scrollW']}, clientWidth: {overflow['clientW']}, diff: {overflow['diff']}, hasOverflow: {overflow['hasOverflow']}")
            assert not overflow['hasOverflow'], f"Horizontal overflow detected on {name} ({width}px): diff {overflow['diff']}px"

        # 7. TEST DISZTRÍBUCIÓ (ÉRTÉKESÍTÉSI CSATORNÁK) REDESIGN
        print("\n--- TEST 7: Disztribúció Section Architectural Layout ---")
        dist_exists = await evaluate("!!document.getElementById('disztribucio')")
        assert dist_exists, "Error: #disztribucio not found!"
        
        dist_articles = await evaluate("document.querySelectorAll('#disztribucio article').length")
        print(f"Disztribúció article columns: {dist_articles}")
        assert dist_articles == 2, f"Expected 2 article columns in disztribúció, got {dist_articles}"

        # 8. TEST KAPCSOLAT REDESIGN & EXCLUSION OF TAX/REG/RATING
        print("\n--- TEST 8: Kapcsolat Section Redesign & Legal Data Exclusion ---")
        kapcsolat_exists = await evaluate("!!document.getElementById('kapcsolat')")
        assert kapcsolat_exists, "Error: #kapcsolat not found!"

        kapcsolat_text = await evaluate("document.getElementById('kapcsolat').innerText")
        assert "14650969-2-41" not in kapcsolat_text, "Error: Adószám still present in kapcsolat!"
        assert "01-10-046300" not in kapcsolat_text, "Error: Cégjegyzékszám still present in kapcsolat!"
        assert "AA+ Bonitás" not in kapcsolat_text, "Error: Pénzügyi besorolás still present in kapcsolat!"
        print("Confirmed: Adószám, Cégjegyzékszám, and Pénzügyi besorolás are completely removed from #kapcsolat.")

        kapcsolat_articles = await evaluate("document.querySelectorAll('#kapcsolat article').length")
        print(f"Kapcsolat article columns: {kapcsolat_articles}")
        assert kapcsolat_articles == 3, f"Expected 3 article columns in kapcsolat, got {kapcsolat_articles}"

        # Check phone and email are intact
        assert "+36 30 899 8548" in kapcsolat_text, "Error: Direct mobile not found in kapcsolat!"
        assert "ifj.vecsei.andras@sunvalley.hu" in kapcsolat_text, "Error: Email not found in kapcsolat!"
        assert "8060 Mór, Major utca 3." in kapcsolat_text, "Error: Plant address not found in kapcsolat!"

        # 9. TEST SECTION COLOR RHYTHM
        print("\n--- TEST 9: Section Color Rhythm Verification ---")
        colors = await evaluate("""
            (() => {
                const getBg = id => {
                    const el = document.getElementById(id);
                    return el ? window.getComputedStyle(el).backgroundColor : null;
                };
                return {
                    cegunkrol: getBg('cegunkrol'),
                    technologia: getBg('technologia'),
                    egyedi: getBg('egyedi-fejlesztes'),
                    prospektus: getBg('prospektus'),
                    disztribucio: getBg('disztribucio'),
                    kapcsolat: getBg('kapcsolat')
                };
            })()
        """)
        print(f"Section Background Colors: {colors}")
        # cegunkrol should be red (approx rgb(163, 57, 46))
        # egyedi should be green (approx rgb(45, 54, 40))
        # prospektus should be red (approx rgb(163, 57, 46))
        # kapcsolat should be green (approx rgb(45, 54, 40))
        assert "45, 54, 40" in colors['kapcsolat'], f"Expected green background on #kapcsolat, got {colors['kapcsolat']}"
        assert "45, 54, 40" in colors['egyedi'], f"Expected green background on #egyedi-fejlesztes, got {colors['egyedi']}"
        assert "163, 57, 46" in colors['cegunkrol'], f"Expected red background on #cegunkrol, got {colors['cegunkrol']}"

        # 10. CAPTURE VISUAL SCREENSHOTS
        print("\n--- TEST 10: Capturing Visual Proof Screenshots ---")
        # Desktop 1440
        await send_cdp("Emulation.setDeviceMetricsOverride", {
            "width": 1440,
            "height": 900,
            "deviceScaleFactor": 1,
            "mobile": False
        })
        await asyncio.sleep(0.5)

        # Disztribucio screenshot
        await evaluate("document.getElementById('disztribucio').scrollIntoView({ behavior: 'instant' })")
        await asyncio.sleep(0.6)
        shot_dist = await send_cdp("Page.captureScreenshot", {"format": "png"})
        shot_dist_path = os.path.join(SCREENSHOTS_DIR, "disztribucio_desktop.png")
        with open(shot_dist_path, "wb") as f:
            f.write(base64.b64decode(shot_dist["data"]))
        print(f"Captured: {shot_dist_path}")

        # Kapcsolat screenshot
        await evaluate("document.getElementById('kapcsolat').scrollIntoView({ behavior: 'instant' })")
        await asyncio.sleep(0.6)
        shot_kapcs = await send_cdp("Page.captureScreenshot", {"format": "png"})
        shot_kapcs_path = os.path.join(SCREENSHOTS_DIR, "kapcsolat_desktop.png")
        with open(shot_kapcs_path, "wb") as f:
            f.write(base64.b64decode(shot_kapcs["data"]))
        print(f"Captured: {shot_kapcs_path}")

        # Mobile view of Kapcsolat
        await send_cdp("Emulation.setDeviceMetricsOverride", {
            "width": 375,
            "height": 812,
            "deviceScaleFactor": 2,
            "mobile": True
        })
        await evaluate("document.getElementById('kapcsolat').scrollIntoView({ behavior: 'instant' })")
        await asyncio.sleep(0.6)
        shot_kapcs_mob = await send_cdp("Page.captureScreenshot", {"format": "png"})
        shot_kapcs_mob_path = os.path.join(SCREENSHOTS_DIR, "kapcsolat_mobile.png")
        with open(shot_kapcs_mob_path, "wb") as f:
            f.write(base64.b64decode(shot_kapcs_mob["data"]))
        print(f"Captured: {shot_kapcs_mob_path}")

        print("\nALL VERIFICATION TESTS PASSED SUCCESSFULLY!")

    finally:
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except Exception:
            proc.kill()

if __name__ == "__main__":
    asyncio.run(run_verification())
