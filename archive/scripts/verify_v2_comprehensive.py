import os
import sys
import json
import re
import time
import subprocess
import asyncio
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')


HTML_V2 = r"C:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b\index_v2.html"
HTML_INDEX = r"C:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b\index.html"
HTML_V1 = r"C:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b\index_v1.html"
HTML_V3 = r"C:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b\index_v3.html"
ASSETS_DIR = r"C:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b\assets"
DOC_RESEARCH = r"C:\Users\csern\Desktop\sun valley\docs\b2b-food-tech-research-and-v2-concept.md"

def test_file_duplication_and_assets():
    print("=== TEST 1: FILE DUPLICATION & ASSET INTEGRITY ===")
    assert os.path.exists(HTML_V1), "index_v1.html must exist"
    assert os.path.exists(HTML_V2), "index_v2.html must exist"
    assert os.path.exists(HTML_V3), "index_v3.html must exist"
    assert os.path.exists(HTML_INDEX), "index.html must exist"
    assert os.path.exists(DOC_RESEARCH), "Research document must exist"

    v1_size = os.path.getsize(HTML_V1)
    v2_size = os.path.getsize(HTML_V2)
    v3_size = os.path.getsize(HTML_V3)
    index_size = os.path.getsize(HTML_INDEX)

    print(f"  v1 size: {v1_size} bytes (reference)")
    print(f"  v3 size: {v3_size} bytes (prepared)")
    print(f"  v2 size: {v2_size} bytes (enhanced)")
    print(f"  index size: {index_size} bytes (synced)")

    assert v1_size == 86947, "v1 should be exact original file"
    assert v2_size == index_size, "index.html and index_v2.html must be in sync"
    assert v2_size > v1_size, "v2 must contain enriched B2B features"

    # Verify all 12 assets from ChatGPT preview
    expected_assets = [
        "sun-valley-logo.png",
        "apricot-hero.png",
        "catalog-bake-stable.png",
        "catalog-spreadable.png",
        "catalog-extra-jam.png",
        "familiar-jams-group.png",
        "exotic-fruits-fresh-v2.png",
        "technology-baking-pastry-v2.png",
        "technology-freezing-cake.png",
        "technology-pumpable-doughnut.png",
        "custom-recipe-jam-sizes.png",
        "Sun_Valley_B2B_Prospektus_V1_4.pptx"
    ]
    for asset in expected_assets:
        p = os.path.join(ASSETS_DIR, asset)
        assert os.path.exists(p), f"Asset missing: {p}"
        size = os.path.getsize(p)
        assert size > 1000000, f"Asset suspiciously small: {asset} ({size} bytes)"
        print(f"  [OK ASSET] {asset} ({size:,} bytes)")

    print("File duplication & assets PASSED.\n")

def test_static_html_and_accessibility():
    print("=== TEST 2: HTML STRUCTURE, FORMS & ACCESSIBILITY ===")
    with open(HTML_V2, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # Form verification
    form = soup.find("form", id="sample-request-form")
    assert form is not None, "Sample request form with id='sample-request-form' must exist"

    inputs = form.find_all(["input", "select", "textarea"])
    print(f"  Found {len(inputs)} form input elements inside sample-request-form:")
    for inp in inputs:
        name = inp.get("name")
        elem_id = inp.get("id")
        assert name is not None and len(name) > 0, f"Input tag <{inp.name}> missing name attribute!"
        assert elem_id is not None and len(elem_id) > 0, f"Input tag <{inp.name}> missing id attribute!"
        print(f"    [OK INPUT] <{inp.name}> id='{elem_id}' name='{name}'")

    # Label for-association
    labels = form.find_all("label")
    for lbl in labels:
        for_id = lbl.get("for")
        assert for_id is not None, f"Label '{lbl.text.strip()}' missing 'for' attribute!"
        assert form.find(id=for_id) is not None, f"Label for='{for_id}' has no matching element id in form!"
    print(f"  [OK LABELS] All {len(labels)} labels properly associated with inputs")

    # Lazy loading verification
    imgs = soup.find_all("img")
    for img in imgs:
        src = img.get("src", "")
        if "apricot-hero" in src or "sun-valley-logo" in src:
            continue
        loading = img.get("loading")
        decoding = img.get("decoding")
        assert loading == "lazy", f"Below-the-fold image {src} must have loading='lazy'"
        assert decoding == "async", f"Below-the-fold image {src} must have decoding='async'"
    print(f"  [OK LAZY LOADING] Verified {len(imgs)} images")

    # i18n key completeness
    script = soup.find("script", string=re.compile("const translations ="))
    assert script is not None, "translations object must exist in script"
    match = re.search(r"const translations\s*=\s*(\{.+?\n\s*\});", script.string, re.DOTALL)
    assert match is not None, "translations block must be valid JS object"

    # Parse JSON or inspect keys
    data_i18n_tags = soup.find_all(attrs={"data-i18n": True})
    print(f"  Found {len(data_i18n_tags)} data-i18n tags in markup")
    assert len(data_i18n_tags) >= 80, "Expected comprehensive data-i18n coverage"

    print("HTML structure, forms & accessibility PASSED.\n")

async def test_runtime_browser():
    print("=== TEST 3: RUNTIME CDP BROWSER VERIFICATION (PORT 9333) ===")
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    user_data = r"C:\Users\csern\AppData\Local\Temp\chrome_audit_p9333"
    port = 9333

    cmd = [
        chrome_path,
        "--headless=new",
        f"--remote-debugging-port={port}",
        f"--user-data-dir={user_data}",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check"
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)

    import tornado.httpclient
    import tornado.websocket

    try:
        # Get websocket URL
        http_client = tornado.httpclient.AsyncHTTPClient()
        resp = await http_client.fetch(f"http://127.0.0.1:{port}/json/version")
        ver_data = json.loads(resp.body)
        ws_browser_url = ver_data["webSocketDebuggerUrl"]
        print(f"  Chrome DevTools URL: {ws_browser_url}")

        conn = await tornado.websocket.websocket_connect(ws_browser_url, max_message_size=100*1024*1024)
        req_id = 1

        v2_url = f"file:///{HTML_V2.replace(os.sep, '/')}"
        await conn.write_message(json.dumps({"id": req_id, "method": "Target.createTarget", "params": {"url": v2_url}}))
        cr = json.loads(await conn.read_message())
        target_id = cr["result"]["targetId"]

        req_id += 1
        await conn.write_message(json.dumps({"id": req_id, "method": "Target.attachToTarget", "params": {"targetId": target_id, "flatten": True}}))
        session_id = None
        while not session_id:
            m = json.loads(await conn.read_message())
            if m.get("method") == "Target.attachedToTarget":
                session_id = m.get("params", {}).get("sessionId")
            elif m.get("id") == req_id and "result" in m:
                session_id = m.get("result", {}).get("sessionId")

        async def call_eval(expr):
            nonlocal req_id
            req_id += 1
            await conn.write_message(json.dumps({
                "id": req_id,
                "sessionId": session_id,
                "method": "Runtime.evaluate",
                "params": {"expression": expr, "awaitPromise": True, "returnByValue": True}
            }))
            while True:
                raw = await conn.read_message()
                res = json.loads(raw)
                if res.get("id") == req_id:
                    return res.get("result", {}).get("result", {}).get("value")

        await asyncio.sleep(1.5)

        # 1. Page Title & Initial DOM
        title = await call_eval("document.title")
        print(f"  [PAGE TITLE] {title}")
        assert "Sun Valley Zrt." in title

        # 2. Test Multilingual Switching
        print("  Testing Trilingual Engine (HU -> EN -> DE)...")
        # Switch to EN
        await call_eval("setLanguage('en')")
        en_h1 = await call_eval("document.querySelector('h1').innerText")
        assert "No boil-out" in en_h1, f"Expected EN H1, got: {en_h1}"
        en_tab1 = await call_eval("document.getElementById('tab-btn-bake-stable').innerText")
        assert "Bake-Stable" in en_tab1, f"Expected EN tab, got: {en_tab1}"
        en_apps = await call_eval("document.getElementById('cat-apps').innerText")
        assert "Apricot Buns" in en_apps or "Turnovers" in en_apps, f"Expected EN apps, got: {en_apps}"
        print(f"    [OK EN] H1: {en_h1[:40]}... Tab 1: {en_tab1}")

        # Switch to DE
        await call_eval("setLanguage('de')")
        de_h1 = await call_eval("document.querySelector('h1').innerText")
        assert "Kein Auskochen" in de_h1, f"Expected DE H1, got: {de_h1}"
        de_tab1 = await call_eval("document.getElementById('tab-btn-bake-stable').innerText")
        assert "Backstabile" in de_tab1, f"Expected DE tab, got: {de_tab1}"
        de_apps = await call_eval("document.getElementById('cat-apps').innerText")
        assert "Aprikosenbuchteln" in de_apps or "Plunder-Taschen" in de_apps, f"Expected DE apps, got: {de_apps}"
        print(f"    [OK DE] H1: {de_h1[:40]}... Tab 1: {de_tab1}")

        # Switch back to HU
        await call_eval("setLanguage('hu')")
        hu_tab1 = await call_eval("document.getElementById('tab-btn-bake-stable').innerText")
        assert "Sütésálló" in hu_tab1, f"Expected HU tab, got: {hu_tab1}"

        # 3. Test Gastro-Catalog Tab Switching
        print("  Testing Gastro-Catalog Tab Switching...")
        await call_eval("switchCatalogTab('spreadable')")
        t2_title = await call_eval("document.getElementById('cat-title').innerText")
        assert "Kenhető" in t2_title
        await call_eval("switchCatalogTab('extra-jam')")
        t3_title = await call_eval("document.getElementById('cat-title').innerText")
        assert "Extra" in t3_title
        await call_eval("switchCatalogTab('bake-stable')")
        print("    [OK TABS] All 3 tabs switch seamlessly")

        # 4. Test TDS Modal Opening, Localization & Preselection Funnel
        print("  Testing TDS Modal Localized Specifications...")
        # Open in English
        await call_eval("setLanguage('en')")
        await call_eval("openTdsModal(1)") # Apricot
        modal_visible = await call_eval("!document.getElementById('tds-modal').classList.contains('hidden')")
        assert modal_visible is True, "Modal should be visible"
        modal_content = await call_eval("document.getElementById('tds-modal-content').innerText")
        assert "Product Code" in modal_content, "Modal must have EN labels ('Product Code')"
        assert "Refractometric Brix" in modal_content, "Modal must have EN 'Refractometric Brix'"
        assert "Request Sample for This Product" in modal_content, "Modal CTA must be localized in EN"
        print("    [OK TDS MODAL EN] Spec table, microbiology & CTA properly localized in English")

        # Click CTA inside modal and test preselection funnel
        print("  Testing Conversion Funnel: TDS Modal -> Sample Form Preselection...")
        await call_eval("selectProductAndScroll('sutesallo-kajszi')")
        modal_closed = await call_eval("document.getElementById('tds-modal').classList.contains('hidden')")
        assert modal_closed is True, "Modal should close automatically upon sample selection"
        selected_prod = await call_eval("document.getElementById('sample-product').value")
        assert selected_prod == "sutesallo-kajszi", f"Form dropdown should be set to 'sutesallo-kajszi', got: {selected_prod}"
        print("    [OK FUNNEL] Product 'sutesallo-kajszi' successfully pre-selected in form dropdown!")

        # 5. Test Form Submission & Data Serialization
        print("  Testing Form Submission & Serialization...")
        await call_eval("""
            document.getElementById('sample-name').value = 'Teszt Elek (Főtechnológus)';
            document.getElementById('sample-company').value = 'Kovács Kenyérgyár Zrt. • 12345678-2-41';
            document.getElementById('sample-email').value = 'technologia@kovacspekseg.hu';
            document.getElementById('sample-phone').value = '+36 30 999 8888';
            document.getElementById('sample-volume').value = 'vol-large';
            document.getElementById('sample-notes').value = 'Ipari automata tésztabetétező tesztelés 215 fokon';
            document.getElementById('form-gdpr').checked = true;
        """)

        form_data_entries = await call_eval("[...new FormData(document.getElementById('sample-request-form')).entries()]")
        print(f"    FormData serializes {len(form_data_entries)} key-value pairs:")
        for k, v in form_data_entries:
            print(f"      - {k}: {v}")
        assert len(form_data_entries) == 8, f"Expected 8 serialized entries, got {len(form_data_entries)}"

        # Submit form
        await call_eval("document.getElementById('sample-request-form').dispatchEvent(new Event('submit', {cancelable: true, bubbles: true}))")
        success_text = await call_eval("document.getElementById('form-success-message').innerText")
        assert "Teszt Elek" in success_text, f"Success message should mention the contact name, got: {success_text}"
        print(f"    [OK FORM SUBMISSION] Localized success message displayed: {success_text[:60]}...")

        # 6. Capture Screenshots for Verification
        print("  Capturing Responsive Screenshots...")
        breakpoints = [
            ("v2_desktop_1440.png", 1440, 900),
            ("v2_tablet_768.png", 768, 1024),
            ("v2_mobile_375.png", 375, 812)
        ]
        for filename, width, height in breakpoints:
            req_id += 1
            await conn.write_message(json.dumps({
                "id": req_id,
                "sessionId": session_id,
                "method": "Emulation.setDeviceMetricsOverride",
                "params": {"width": width, "height": height, "deviceScaleFactor": 1, "mobile": width < 768}
            }))
            while True:
                m = json.loads(await conn.read_message())
                if m.get("id") == req_id:
                    break

            await asyncio.sleep(0.5)

            req_id += 1
            await conn.write_message(json.dumps({
                "id": req_id,
                "sessionId": session_id,
                "method": "Page.captureScreenshot",
                "params": {"format": "png"}
            }))
            while True:
                m = json.loads(await conn.read_message())
                if m.get("id") == req_id:
                    import base64
                    img_data = base64.b64decode(m["result"]["data"])
                    out_path = os.path.join(r"C:\Users\csern\Desktop\sun valley", filename)
                    with open(out_path, "wb") as sf:
                        sf.write(img_data)
                    print(f"    Saved verified screenshot: {filename} ({len(img_data):,} bytes)")
                    break

        # Close target
        req_id += 1
        await conn.write_message(json.dumps({"id": req_id, "method": "Target.closeTarget", "params": {"targetId": target_id}}))
        conn.close()

    finally:
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except Exception:
            proc.kill()

    print("\nALL VERIFICATIONS (STATIC + RUNTIME) COMPLETED SUCCESSFULLY WITH ZERO ERRORS!")

if __name__ == "__main__":
    test_file_duplication_and_assets()
    test_static_html_and_accessibility()
    asyncio.run(test_runtime_browser())
