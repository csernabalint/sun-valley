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
USER_DATA = r"C:\Users\csern\AppData\Local\Temp\chrome_batch_verify"
PORT = 9811

async def run_verification():
    print("=== STARTING COMPREHENSIVE VERIFICATION FOR USER REQUEST ITEMS ===")
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
            res = await send_cdp("Runtime.evaluate", {
                "expression": expr,
                "awaitPromise": True,
                "returnByValue": True
            })
            if "exceptionDetails" in res:
                print("JS EXCEPTION:", res["exceptionDetails"])
            return res.get("result", {}).get("value")

        await send_cdp("Page.enable")
        await send_cdp("DOM.enable")
        await send_cdp("Emulation.setDeviceMetricsOverride", {
            "width": 1280,
            "height": 850,
            "deviceScaleFactor": 1,
            "mobile": False
        })
        await asyncio.sleep(1.0)

        # -------------------------------------------------------------
        # TEST 1: Hero Section - Right column has ONLY image, NO overlays/specs
        # -------------------------------------------------------------
        print("\n--- TEST 1: Hero Right Column Clean Image ---")
        hero_info = await eval_js("""
        (() => {
            const heroGrid = document.querySelector('h1').closest('.grid');
            const heroRight = heroGrid ? heroGrid.children[1] : null;
            const img = heroRight ? heroRight.querySelector('img') : null;
            const overlays = heroRight ? heroRight.querySelectorAll('.absolute, button, table, [data-i18n="hero_card_pill"], [data-i18n="card_hero_cat"]') : [];
            const textContent = heroRight ? heroRight.innerText.trim() : '';
            return {
                hasHeroRight: !!heroRight,
                imgSrc: img ? img.getAttribute('src') : null,
                imgNaturalW: img ? img.naturalWidth : 0,
                imgNaturalH: img ? img.naturalHeight : 0,
                overlayCount: overlays.length,
                textLength: textContent.length,
                textContent: textContent
            };
        })()
        """)
        print(f"  Hero right column exists: {hero_info['hasHeroRight']}")
        print(f"  Image src: {hero_info['imgSrc']} (natural: {hero_info['imgNaturalW']}x{hero_info['imgNaturalH']})")
        print(f"  Overlays/buttons inside hero right: {hero_info['overlayCount']}")
        print(f"  Text content length inside hero right: {hero_info['textLength']}")
        assert hero_info["hasHeroRight"], "Hero right column not found!"
        assert "apricot" in hero_info["imgSrc"], f"Unexpected image in hero right: {hero_info['imgSrc']}"
        assert hero_info["overlayCount"] == 0, f"Hero right column must have ZERO overlays/buttons, got {hero_info['overlayCount']}"
        assert hero_info["textLength"] == 0, f"Hero right column must have NO description text, got '{hero_info['textContent']}'"
        print("  [PASS] Hero right column has clean image with zero overlays and zero text descriptions.")

        # -----------------------------------------------------------------
        # TEST 2: Catalog Section Header - No category subtitle paragraph
        # -----------------------------------------------------------------
        print("\n--- TEST 2: Catalog Section Header (No subtitle) ---")
        cat_header_info = await eval_js("""
        (() => {
            const header = document.querySelector('#termekek .max-w-3xl');
            const paragraphs = header ? header.querySelectorAll('p') : [];
            return {
                headerText: header ? header.innerText.trim() : '',
                pCount: paragraphs.length,
                hasSectionDesc: !!document.querySelector('[data-i18n="cat_section_desc"]')
            };
        })()
        """)
        print(f"  Catalog header p tag count: {cat_header_info['pCount']}")
        print(f"  Has cat_section_desc: {cat_header_info['hasSectionDesc']}")
        assert cat_header_info["pCount"] == 0, f"Catalog header should not have subtitle paragraph, found {cat_header_info['pCount']}"
        assert not cat_header_info["hasSectionDesc"], "cat_section_desc element should be removed from DOM!"
        print("  [PASS] Catalog header has no subtitle paragraph.")

        # -----------------------------------------------------------------
        # TEST 3: Catalog Card Layout & Specs/Caption Removal
        # -----------------------------------------------------------------
        print("\n--- TEST 3: Catalog Card Specs & Caption Removal & Width ---")
        card_info = await eval_js("""
        (() => {
            const card = document.getElementById('catalog-card');
            const viewport = document.querySelector('.catalog-viewport');
            const specs = document.getElementById('cat-specs');
            const caption = document.getElementById('cat-img-caption');
            const img = document.getElementById('cat-image');
            const desc = document.getElementById('cat-desc');
            return {
                cardExists: !!card,
                viewportClasses: viewport ? viewport.className : '',
                specsExists: !!specs,
                captionExists: !!caption,
                imgClasses: img ? img.className : '',
                descText: desc ? desc.innerText.trim() : ''
            };
        })()
        """)
        print(f"  Card exists: {card_info['cardExists']}")
        print(f"  Viewport classes: {card_info['viewportClasses']}")
        print(f"  cat-specs exists: {card_info['specsExists']}")
        print(f"  cat-img-caption exists: {card_info['captionExists']}")
        print(f"  cat-desc text: {card_info['descText'][:80]}...")
        assert "max-w-7xl" in card_info["viewportClasses"], "Catalog card container should be widened to max-w-7xl!"
        assert not card_info["specsExists"], "cat-specs must be completely removed from DOM!"
        assert not card_info["captionExists"], "cat-img-caption must be completely removed from DOM!"
        assert "h-full" in card_info["imgClasses"], "Catalog image must have full vertical height stretch class!"
        print("  [PASS] Catalog card widened, specs and captions removed, image vertically stretched.")

        # -----------------------------------------------------------------
        # TEST 4: Catalog Category 3 Description ("Magas gyümölcstartalmú")
        # -----------------------------------------------------------------
        print("\n--- TEST 4: Catalog Navigation & Category 3 Description ---")
        # Navigate to category 3 (extra-jam)
        await eval_js("switchCatalogTab('extra-jam', 1)")
        await asyncio.sleep(0.5)

        cat3_info = await eval_js("""
        (() => {
            const desc = document.getElementById('cat-desc');
            const title = document.getElementById('cat-title');
            const counter = document.getElementById('cat-current-num');
            return {
                title: title ? title.innerText.trim() : '',
                counter: counter ? counter.innerText.trim() : '',
                desc: desc ? desc.innerText.trim() : '',
                descI18n: desc ? desc.getAttribute('data-i18n') : '',
                titleI18n: title ? title.getAttribute('data-i18n') : ''
            };
        })()
        """)
        print(f"  Active category title: {cat3_info['title']}")
        print(f"  Counter: {cat3_info['counter']}")
        print(f"  Category 3 Description: {cat3_info['desc']}")
        print(f"  Category 3 data-i18n: {cat3_info['descI18n']} (title: {cat3_info['titleI18n']})")
        assert "Extra dzsemek" in cat3_info["title"], f"Expected Extra dzsemek, got {cat3_info['title']}"
        assert cat3_info["counter"] == "03", f"Expected counter 03, got {cat3_info['counter']}"
        assert "Magas gyümölcstartalmú" in cat3_info["desc"], f"Description must contain 'Magas gyümölcstartalmú', got: {cat3_info['desc']}"
        assert "hányad" not in cat3_info["desc"], f"Description must NOT contain 'hányad', got: {cat3_info['desc']}"
        assert cat3_info["descI18n"] == "prod_cat3_desc", f"Expected desc data-i18n to be prod_cat3_desc, got: {cat3_info['descI18n']}"
        assert cat3_info["titleI18n"] == "prod_cat3_title", f"Expected title data-i18n to be prod_cat3_title, got: {cat3_info['titleI18n']}"
        print("  [PASS] Category 3 uses 'Magas gyümölcstartalmú' instead of 'Magas gyümölcshányadú' and keeps data-i18n synced.")

        # -----------------------------------------------------------------
        # TEST 5: Exotic Fruits into 6 Separate Individual Cards
        # -----------------------------------------------------------------
        print("\n--- TEST 5: 6 Individual Exotic Fruit Cards ---")
        exotic_info = await eval_js("""
        (() => {
            const exoticSection = document.querySelector('[data-i18n=\"exotic_title\"]').closest('.grid');
            const cards = Array.from(exoticSection.querySelectorAll('.grid > div.rounded-xl'));
            return cards.map(c => ({
                text: c.innerText.trim(),
                hasDot: !!c.querySelector('span.rounded-full'),
                dotClasses: c.querySelector('span.rounded-full')?.className || '',
                i18nKey: c.querySelector('[data-i18n]')?.getAttribute('data-i18n') || ''
            }));
        })()
        """)
        print(f"  Found {len(exotic_info)} exotic fruit cards:")
        for c in exotic_info:
            print(f"    - {c['text']} (key: {c['i18nKey']}, dot: {c['hasDot']})")
        assert len(exotic_info) == 6, f"Expected exactly 6 exotic fruit cards, found {len(exotic_info)}"
        expected_fruits = ["Mangó", "Maracuja", "Ananász", "Kivi", "Citrus", "Narancs"]
        card_texts = [c["text"] for c in exotic_info]
        for ef in expected_fruits:
            assert ef in card_texts, f"Missing exotic fruit: {ef} in {card_texts}"
        for c in exotic_info:
            assert c["hasDot"], f"Card '{c['text']}' missing colored indicator dot!"
        print("  [PASS] 6 individual exotic fruit cards rendered with consistent indicator dot styling.")

        # -----------------------------------------------------------------
        # TEST 6: Fruit Bowl Image in Exotic Section
        # -----------------------------------------------------------------
        print("\n--- TEST 6: Fruit Bowl Image Replacement ---")
        await eval_js("document.querySelector('[data-i18n=\"exotic_title\"]').scrollIntoView({ behavior: 'instant', block: 'center' });")
        await asyncio.sleep(0.5)
        bowl_info = await eval_js("""
        (() => {
            const exoticSection = document.querySelector('[data-i18n=\"exotic_title\"]').closest('.grid');
            const img = exoticSection.querySelector('img');
            const source = exoticSection.querySelector('source');
            return {
                imgSrc: img ? img.getAttribute('src') : null,
                imgNaturalW: img ? img.naturalWidth : 0,
                imgNaturalH: img ? img.naturalHeight : 0,
                sourceSrcset: source ? source.getAttribute('srcset') : null
            };
        })()
        """)
        print(f"  Exotic image src: {bowl_info['imgSrc']} ({bowl_info['imgNaturalW']}x{bowl_info['imgNaturalH']})")
        print(f"  Exotic source srcset: {bowl_info['sourceSrcset']}")
        assert "fruit-bowl1.jpg" in bowl_info["imgSrc"], f"Expected fruit-bowl1.jpg, got {bowl_info['imgSrc']}"
        assert "fruit-bowl1.webp" in bowl_info["sourceSrcset"], f"Expected fruit-bowl1.webp in source, got {bowl_info['sourceSrcset']}"
        assert bowl_info["imgNaturalW"] > 0 and bowl_info["imgNaturalH"] > 0, "fruit-bowl1 image failed to load!"
        print("  [PASS] fruit-bowl1 image loaded with WebP fallback.")

        # -----------------------------------------------------------------
        # TEST 7 & 8: Cégünkről - No overlay badge, No proof strips, Vertically stretched image
        # -----------------------------------------------------------------
        print("\n--- TEST 7 & 8: Cégünkről Section Clean Image & Vertically Stretched ---")
        ceg_info = await eval_js("""
        (() => {
            const cegSection = document.getElementById('cegunkrol');
            const cols = cegSection.querySelectorAll('.grid > div');
            const leftCol = cols[0];
            const rightCol = cols[1];
            const badges = rightCol ? rightCol.querySelectorAll('.absolute, [data-i18n="about_plant_badge"]') : [];
            const proofStrips = rightCol ? rightCol.querySelectorAll('[data-i18n*="about_proof"]') : [];
            const img = rightCol ? rightCol.querySelector('img') : null;
            return {
                hasRightCol: !!rightCol,
                badgeCount: badges.length,
                proofCount: proofStrips.length,
                rightColH: rightCol ? rightCol.offsetHeight : 0,
                leftColH: leftCol ? leftCol.offsetHeight : 0,
                imgSrc: img ? img.getAttribute('src') : null
            };
        })()
        """)
        print(f"  Cégünkről right column exists: {ceg_info['hasRightCol']}")
        print(f"  Badge count in right column: {ceg_info['badgeCount']}")
        print(f"  Proof strips in right column: {ceg_info['proofCount']}")
        print(f"  Left column height: {ceg_info['leftColH']}px, Right column height: {ceg_info['rightColH']}px")
        assert ceg_info["badgeCount"] == 0, f"Expected 0 badges on Cégünkről image, found {ceg_info['badgeCount']}"
        assert ceg_info["proofCount"] == 0, f"Expected 0 proof strips below image, found {ceg_info['proofCount']}"
        assert abs(ceg_info["rightColH"] - ceg_info["leftColH"]) <= 10, f"Image column should vertically match left column: left={ceg_info['leftColH']}, right={ceg_info['rightColH']}"
        print("  [PASS] Cégünkről right column has clean, vertically stretched image with zero badge overlays and zero proof strips.")

        # -----------------------------------------------------------------
        # TEST 9 & 10: Prospektus - No file size anywhere, PDF opens in browser reader
        # -----------------------------------------------------------------
        print("\n--- TEST 9 & 10: Prospektus PDF Link & Zero File Size Mentions ---")
        prosp_info = await eval_js("""
        (() => {
            const prosp = document.getElementById('prospektus');
            const link = prosp ? prosp.querySelector('a') : null;
            const fullBodyText = document.body.innerText;
            const has11MB = fullBodyText.includes('11,1 MB') || fullBodyText.includes('11.1 MB');
            return {
                hasProsp: !!prosp,
                linkHref: link ? link.getAttribute('href') : null,
                linkTarget: link ? link.getAttribute('target') : null,
                linkRel: link ? link.getAttribute('rel') : null,
                linkDownload: link ? link.getAttribute('download') : null,
                linkText: link ? link.innerText.trim() : '',
                has11MB: has11MB
            };
        })()
        """)
        print(f"  Link href: {prosp_info['linkHref']}")
        print(f"  Link target: {prosp_info['linkTarget']}")
        print(f"  Link rel: {prosp_info['linkRel']}")
        print(f"  Link download attr: {prosp_info['linkDownload']}")
        print(f"  Link text: {prosp_info['linkText']}")
        print(f"  Page contains '11,1 MB' mention: {prosp_info['has11MB']}")
        assert "Sun_Valley_B2B_Prospektus.pdf" in prosp_info["linkHref"], f"Expected PDF link, got {prosp_info['linkHref']}"
        assert prosp_info["linkTarget"] == "_blank", f"Expected target='_blank', got {prosp_info['linkTarget']}"
        assert prosp_info["linkRel"] == "noopener noreferrer", f"Expected rel='noopener noreferrer', got {prosp_info['linkRel']}"
        assert prosp_info["linkDownload"] is None, f"Expected NO download attribute on link, got {prosp_info['linkDownload']}"
        assert not prosp_info["has11MB"], "Page must NOT mention file size (~11,1 MB) anywhere!"
        print("  [PASS] Prospektus links to PDF with target='_blank' (opens in browser reader), no download attribute, zero file size mentions.")

        # -----------------------------------------------------------------
        # TEST 11: Multilingual Switcher (HU <-> EN)
        # -----------------------------------------------------------------
        print("\n--- TEST 11: Multilingual Switcher (HU <-> EN) ---")
        await eval_js("setLanguage('en')")
        await asyncio.sleep(0.3)
        en_info = await eval_js("""
        (() => {
            const prospLink = document.querySelector('#prospektus a');
            const exoticCards = Array.from(document.querySelectorAll('[data-i18n=\"exotic_title\"]')[0].closest('.grid').querySelectorAll('.grid > div.rounded-xl'));
            const cat3Desc = document.getElementById('cat-desc');
            return {
                prospLinkText: prospLink ? prospLink.innerText.trim() : '',
                exoticCards: exoticCards.map(c => c.innerText.trim()),
                cat3DescText: cat3Desc ? cat3Desc.innerText.trim() : ''
            };
        })()
        """)
        print(f"  EN Brochure button text: {en_info['prospLinkText']}")
        print(f"  EN Exotic cards: {en_info['exoticCards']}")
        print(f"  EN Cat3 Desc snippet: {en_info['cat3DescText'][:60]}...")
        assert "Open Brochure (.PDF)" in en_info["prospLinkText"], f"EN brochure text mismatch: {en_info['prospLinkText']}"
        assert "Mango" in en_info["exoticCards"] and "Passion Fruit" in en_info["exoticCards"], f"EN exotic cards mismatch: {en_info['exoticCards']}"

        # Switch back to HU
        await eval_js("setLanguage('hu')")
        await asyncio.sleep(0.3)
        hu_info = await eval_js("""
        (() => {
            const prospLink = document.querySelector('#prospektus a');
            const exoticCards = Array.from(document.querySelectorAll('[data-i18n=\"exotic_title\"]')[0].closest('.grid').querySelectorAll('.grid > div.rounded-xl'));
            return {
                prospLinkText: prospLink ? prospLink.innerText.trim() : '',
                exoticCards: exoticCards.map(c => c.innerText.trim())
            };
        })()
        """)
        print(f"  HU Brochure button text: {hu_info['prospLinkText']}")
        print(f"  HU Exotic cards: {hu_info['exoticCards']}")
        assert "Prospektus Megnyitása (.PDF)" in hu_info["prospLinkText"]
        assert "Mangó" in hu_info["exoticCards"] and "Maracuja" in hu_info["exoticCards"]
        print("  [PASS] Clean bilingual toggling verified.")

        # -----------------------------------------------------------------
        # TEST 12: Zero Horizontal Overflow Invariant across 4 Breakpoints
        # -----------------------------------------------------------------
        print("\n--- TEST 12: Zero Horizontal Overflow across 4 Breakpoints ---")
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
            assert overflow_info["scrollW"] <= overflow_info["clientW"] + 1, f"Horizontal overflow at {bp}px: scrollWidth={overflow_info['scrollW']} > clientWidth={overflow_info['clientW']}"
        print("  [PASS] Zero horizontal overflow strictly maintained across 375px, 768px, 1024px, and 1440px.")

        # -----------------------------------------------------------------
        # SCREENSHOTS CAPTURE
        # -----------------------------------------------------------------
        print("\n--- Capturing Screenshots for Verification Record ---")
        await send_cdp("Emulation.setDeviceMetricsOverride", {
            "width": 1280,
            "height": 800,
            "deviceScaleFactor": 1,
            "mobile": False
        })
        await asyncio.sleep(0.4)

        # 1. Hero
        await eval_js("window.scrollTo(0, 0);")
        await asyncio.sleep(0.4)
        shot1 = await send_cdp("Page.captureScreenshot", {"format": "png"})
        p1 = os.path.join(SCREENSHOTS_DIR, "verify_clean_hero.png")
        with open(p1, "wb") as f:
            f.write(base64.b64decode(shot1["data"]))
        print(f"  [OK] Saved {p1}")

        # 2. Catalog
        await eval_js("document.getElementById('termekek').scrollIntoView({ behavior: 'instant', block: 'start' });")
        await asyncio.sleep(0.4)
        shot2 = await send_cdp("Page.captureScreenshot", {"format": "png"})
        p2 = os.path.join(SCREENSHOTS_DIR, "verify_wide_catalog.png")
        with open(p2, "wb") as f:
            f.write(base64.b64decode(shot2["data"]))
        print(f"  [OK] Saved {p2}")

        # 3. Exotic fruits + Fruit bowl
        await eval_js("document.querySelector('[data-i18n=\"exotic_title\"]').scrollIntoView({ behavior: 'instant', block: 'center' });")
        await asyncio.sleep(0.4)
        shot3 = await send_cdp("Page.captureScreenshot", {"format": "png"})
        p3 = os.path.join(SCREENSHOTS_DIR, "verify_exotic_cards_and_fruitbowl.png")
        with open(p3, "wb") as f:
            f.write(base64.b64decode(shot3["data"]))
        print(f"  [OK] Saved {p3}")

        # 4. Cégünkről
        await eval_js("document.getElementById('cegunkrol').scrollIntoView({ behavior: 'instant', block: 'start' });")
        await asyncio.sleep(0.4)
        shot4 = await send_cdp("Page.captureScreenshot", {"format": "png"})
        p4 = os.path.join(SCREENSHOTS_DIR, "verify_cegunkrol_stretched_image.png")
        with open(p4, "wb") as f:
            f.write(base64.b64decode(shot4["data"]))
        print(f"  [OK] Saved {p4}")

        # 5. Prospektus
        await eval_js("document.getElementById('prospektus').scrollIntoView({ behavior: 'instant', block: 'start' });")
        await asyncio.sleep(0.4)
        shot5 = await send_cdp("Page.captureScreenshot", {"format": "png"})
        p5 = os.path.join(SCREENSHOTS_DIR, "verify_prospektus_pdf_clean.png")
        with open(p5, "wb") as f:
            f.write(base64.b64decode(shot5["data"]))
        print(f"  [OK] Saved {p5}")

        print("\n=== ALL COMPREHENSIVE VERIFICATION TESTS PASSED SUCCESSFULLY! ===")

    finally:
        try:
            conn.close()
        except:
            pass
        proc.terminate()

if __name__ == "__main__":
    asyncio.run(run_verification())
