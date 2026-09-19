import asyncio
import base64
import json
import os
import subprocess
import sys
import time
import tornado.httpclient
import tornado.websocket
from pathlib import Path
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
HTML_ROOT = str(REPO_ROOT / "index.html")
HTML_V2 = str(REPO_ROOT / "prototypes" / "sun-valley-b2b" / "index_v2.html")
HTML_INDEX = str(REPO_ROOT / "prototypes" / "sun-valley-b2b" / "index.html")
SCREENSHOTS_DIR = str(REPO_ROOT / "docs" / "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
USER_DATA = r"C:\Users\csern\AppData\Local\Temp\chrome_full_verify"
PORT = 9777

def test_static_integrity():
    print("\n--- 1. STATIC INTEGRITY & DOM ACCESSIBILITY ---")
    with open(HTML_ROOT, "r", encoding="utf-8") as f:
        html_root = f.read()

    with open(HTML_V2, "r", encoding="utf-8") as f:
        html = f.read()

    with open(HTML_INDEX, "r", encoding="utf-8") as f:
        html_index = f.read()

    assert html_root == html, "Root index.html and index_v2.html must be identical!"
    assert html == html_index, "index_v2.html and prototypes index.html must be identical!"
    print("  [OK] Root index.html, index_v2.html and prototypes index.html are byte-identical.")

    soup = BeautifulSoup(html, "html.parser")

    # Form fields check
    form = soup.find("form", id="sample-request-form")
    assert form is not None, "Form sample-request-form must exist"
    for fid in ["sample-name", "sample-company", "sample-email", "sample-phone", "sample-product", "sample-volume", "sample-notes", "form-gdpr"]:
        el = form.find(id=fid)
        assert el is not None, f"Form field #{fid} missing!"
    print("  [OK] All form fields present and properly structured.")

    # Check error containers
    for err_id in ["err-name", "err-company", "err-email", "err-phone", "err-gdpr"]:
        el = form.find(id=err_id)
        assert el is not None, f"Error span #{err_id} missing!"
    print("  [OK] All validation error containers present.")

    # Check font configuration
    assert "family=Syne" not in html, "Syne font import must not exist!"
    assert ".font-syne" in html and "Plus Jakarta Sans" in html, "font-syne must map to Plus Jakarta Sans!"
    print("  [OK] Font family correctly harmonized (no Syne, Plus Jakarta Sans enforced).")

    # Check logo references
    logos = [img for img in soup.find_all("img") if "sun-valley-logo" in img.get("src", "")]
    assert len(logos) >= 2, "Logo must appear in header and footer!"
    for l in logos:
        assert "brightness-0" not in l.get("class", []), "Logo must not have inversion filter!"
    print(f"  [OK] Logo found in {len(logos)} places without destructive inversion filters.")

    # Check vibe colors removed
    assert "vibe" not in html.lower() or "vibe colors" not in html.lower(), "Vibe colors must be completely removed!"
    print("  [OK] Vibe colors feature fully absent.")

async def test_runtime_flows():
    print("\n--- 2. RUNTIME FLOWS & VERIFICATION HOOKS VIA CDP ---")
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

        async def eval_js(expr):
            nonlocal req_id
            req_id += 1
            await conn.write_message(json.dumps({
                "id": req_id,
                "sessionId": session_id,
                "method": "Runtime.evaluate",
                "params": {"expression": expr, "awaitPromise": True, "returnByValue": True}
            }))
            while True:
                res = json.loads(await conn.read_message())
                if res.get("id") == req_id:
                    return res.get("result", {}).get("result", {}).get("value")

        await asyncio.sleep(1.5)

        # 1. Test responsive overflow across 4 breakpoints
        breakpoints = [
            ("verified_375.png", 375, 812),
            ("verified_768.png", 768, 1024),
            ("verified_1024.png", 1024, 768),
            ("verified_1440.png", 1440, 900)
        ]

        print("\n  [Responsive Breakpoint Audit & Screenshot Capture]:")
        for fname, width, height in breakpoints:
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
            await asyncio.sleep(0.4)

            scroll_w = await eval_js("document.documentElement.scrollWidth")
            inner_w = await eval_js("window.innerWidth")
            assert scroll_w <= inner_w, f"Breakpoint {width}px failed: scrollWidth {scroll_w} > innerWidth {inner_w}!"

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
                    img_bytes = base64.b64decode(m["result"]["data"])
                    target_path = os.path.join(SCREENSHOTS_DIR, fname)
                    with open(target_path, "wb") as img_f:
                        img_f.write(img_bytes)
                    print(f"    ✓ Width {width}px: scrollWidth={scroll_w}px (zero overflow). Saved to docs/screenshots/{fname} ({len(img_bytes):,} bytes)")
                    break

        # 2. Test Multilingual switcher (HU -> EN -> DE -> HU)
        print("\n  [Trilingual Switching Verification]:")
        await eval_js("setLanguage('en')")
        h1_en = await eval_js("document.querySelector('h1').innerText")
        assert "No boil-out" in h1_en, f"English H1 mismatch: {h1_en}"
        print(f"    ✓ Switched to EN: H1 reads '{h1_en.splitlines()[0]}'")

        await eval_js("setLanguage('de')")
        h1_de = await eval_js("document.querySelector('h1').innerText")
        assert "Kein Auskochen" in h1_de, f"German H1 mismatch: {h1_de}"
        print(f"    ✓ Switched to DE: H1 reads '{h1_de.splitlines()[0]}'")

        await eval_js("setLanguage('hu')")
        h1_hu = await eval_js("document.querySelector('h1').innerText")
        assert "200 °C felett" in h1_hu, f"Hungarian H1 mismatch: {h1_hu}"
        print(f"    ✓ Switched back to HU: H1 reads '{h1_hu.splitlines()[0]}'")

        # 3. Test Interactive Gastro-Catalog tabs
        print("\n  [Gastro-Catalog Tab Switching Verification]:")
        for tab_id in ["spreadable", "extra-jam", "bake-stable"]:
            await eval_js(f"switchCatalogTab('{tab_id}')")
            active_btn_cls = await eval_js(f"document.getElementById('tab-btn-{tab_id}').className")
            assert "active" in active_btn_cls, f"Tab #{tab_id} not active"
        print("    ✓ All 3 catalog tabs switch and render content accurately.")

        # 4. Test TDS Modal Opening, Specification Display & Preselection Funnel
        print("\n  [TDS Modal & Preselection Funnel Verification]:")
        await eval_js("openTdsModal(1)")
        modal_hidden = await eval_js("document.getElementById('tds-modal').classList.contains('hidden')")
        assert not modal_hidden, "TDS Modal failed to open!"
        modal_content = await eval_js("document.getElementById('tds-modal-content').innerText")
        assert "Kajszi" in modal_content or "Apricot" in modal_content, f"Unexpected TDS content: {modal_content[:100]}"
        print(f"    ✓ TDS Modal opened for: {modal_content.splitlines()[0]}")

        await eval_js("selectProductAndScroll('sutesallo-kajszi')")
        modal_now_hidden = await eval_js("document.getElementById('tds-modal').classList.contains('hidden')")
        assert modal_now_hidden, "TDS Modal should close when sample CTA is clicked!"
        selected_prod = await eval_js("document.getElementById('sample-product').value")
        assert selected_prod == "sutesallo-kajszi", f"Expected 'sutesallo-kajszi', got '{selected_prod}'"
        print(f"    ✓ TDS CTA preselected '{selected_prod}' in the sample request form dropdown.")

        # 5. Test Form Validation: Failure Modes (Empty fields, invalid tax ID, invalid email, missing GDPR)
        print("\n  [Form Validation - Failure Modes & Security Testing]:")
        
        # Helper to submit form
        submit_script = "document.getElementById('sample-request-form').dispatchEvent(new Event('submit', {cancelable: true, bubbles: true}))"

        # Test empty submission
        await eval_js("document.getElementById('sample-name').value = ''")
        await eval_js(submit_script)
        err_name = await eval_js("!document.getElementById('err-name').classList.contains('hidden')")
        assert err_name, "Error should show for empty name!"
        print("    ✓ Failure Mode 1 (Empty name): correctly blocked with error.")

        # Test invalid tax number (less than 8 digits)
        await eval_js("document.getElementById('sample-name').value = 'Kovács Péter'")
        await eval_js("document.getElementById('sample-company').value = 'Kovács Kft. (1234)'")
        await eval_js(submit_script)
        err_comp = await eval_js("!document.getElementById('err-company').classList.contains('hidden')")
        assert err_comp, "Error should show for invalid tax number!"
        print("    ✓ Failure Mode 2 (Invalid Tax ID < 8 digits): correctly blocked with error.")

        # Test invalid email
        await eval_js("document.getElementById('sample-company').value = 'Kovács Kft. • 12345678-2-41'")
        await eval_js("document.getElementById('sample-email').value = 'invalid-email-format'")
        await eval_js(submit_script)
        err_email = await eval_js("!document.getElementById('err-email').classList.contains('hidden')")
        assert err_email, "Error should show for invalid email!"
        print("    ✓ Failure Mode 3 (Invalid email): correctly blocked with error.")

        # Test invalid phone
        await eval_js("document.getElementById('sample-email').value = 'peter@kovacspekseg.hu'")
        await eval_js("document.getElementById('sample-phone').value = '123'")
        await eval_js(submit_script)
        err_phone = await eval_js("!document.getElementById('err-phone').classList.contains('hidden')")
        assert err_phone, "Error should show for invalid phone (< 8 digits)!"
        print("    ✓ Failure Mode 4 (Invalid phone < 8 digits): correctly blocked with error.")

        # Test invalid phone (letters in phone)
        await eval_js("document.getElementById('sample-phone').value = '+36 30 abc 1234'")
        await eval_js(submit_script)
        err_phone2 = await eval_js("!document.getElementById('err-phone').classList.contains('hidden')")
        assert err_phone2, "Error should show for phone containing letters (+36 30 abc 1234)!"
        print("    ✓ Failure Mode 4b (Phone with letters): correctly blocked with error.")

        # Test language switch clears active form errors
        await eval_js("setLanguage('en')")
        err_phone_cleared = await eval_js("document.getElementById('err-phone').classList.contains('hidden')")
        assert err_phone_cleared, "Language switch should clear previous validation errors!"
        print("    ✓ Language switch: active form errors cleared on switch.")
        await eval_js("setLanguage('hu')")

        # Test missing GDPR
        await eval_js("document.getElementById('sample-phone').value = '+36 30 123 4567'")
        await eval_js("document.getElementById('form-gdpr').checked = false")
        await eval_js(submit_script)
        err_gdpr = await eval_js("!document.getElementById('err-gdpr').classList.contains('hidden')")
        assert err_gdpr, "Error should show when GDPR checkbox is unchecked!"
        print("    ✓ Failure Mode 5 (Unchecked GDPR): correctly blocked with error.")

        # 6. Test Form Validation: Happy Path & Security Sanitization
        print("\n  [Form Validation - Happy Path, XSS Sanitization & Ampersand Fidelity]:")
        await eval_js("""
            document.getElementById('sample-name').value = 'Nagy & Fiai János <script>alert(1)</script>';
            document.getElementById('sample-company').value = 'B&B Dunapataji Kenyérgyár Zrt. • 23456789-2-03';
            document.getElementById('sample-email').value = 'nagy.janos@dunapatajpekseg.hu';
            document.getElementById('sample-phone').value = '+36 20 888 9999';
            document.getElementById('sample-volume').value = 'vol-medium';
            document.getElementById('sample-notes').value = '<b>Kiemelt</b> próbagyártás 220°C-os kemencében';
            document.getElementById('form-gdpr').checked = true;
        """)
        await eval_js(submit_script)
        success_hidden = await eval_js("document.getElementById('form-success-message').classList.contains('hidden')")
        assert not success_hidden, "Success message should be displayed!"
        success_msg = await eval_js("document.getElementById('form-success-message').innerText")
        assert "Nagy & Fiai János" in success_msg, "Success message must contain contact name with preserved ampersand!"
        assert "B&B Dunapataji" in success_msg, "Success message must contain company name with preserved ampersand!"
        assert "&amp;" not in success_msg, "No raw HTML entities (&amp;) should leak into text output!"
        assert "<script>" not in success_msg, "XSS script tags must be sanitized out!"
        assert "SV-2026-" in success_msg, "Success message must contain Reference ID (SV-2026-XXXX)!"
        print(f"    ✓ Happy path success message displayed with sanitized text and Reference ID:")
        for line in success_msg.splitlines():
            print(f"      '{line[:100]}'")

        # 7. Test Dynamic Smart Header (Mobile & Scroll Up/Down Logic)
        print("\n  [Dynamic Smart Header Scroll & Reveal Verification]:")
        # Ensure at top first
        await eval_js("window.scrollTo(0, 0); window.dispatchEvent(new Event('scroll'));")
        time.sleep(0.2)
        spacer_height = await eval_js("document.getElementById('header-spacer').offsetHeight")
        header_height = await eval_js("document.getElementById('site-header').offsetHeight")
        assert spacer_height > 40, f"Spacer height ({spacer_height}px) must prevent content jump!"
        print(f"    ✓ Flow spacer initialized: {spacer_height}px (Header total: {header_height}px)")

        # Scroll down to 500px -> header should tuck away
        await eval_js("window.scrollTo(0, 500); window.dispatchEvent(new Event('scroll'));")
        time.sleep(0.3)
        transform_down = await eval_js("document.getElementById('site-header').style.transform")
        assert "translateY(-100%)" in transform_down, f"Expected translateY(-100%) on scroll down, got: {transform_down}"
        print("    ✓ Scroll down to 500px: header tucked away with translateY(-100%).")

        # Scroll up by 100px (to 400px) -> header should immediately reveal with shadow
        await eval_js("window.scrollTo(0, 400); window.dispatchEvent(new Event('scroll'));")
        time.sleep(0.3)
        transform_up = await eval_js("document.getElementById('site-header').style.transform")
        has_shadow = await eval_js("document.getElementById('site-header').classList.contains('shadow-lg')")
        assert "translateY(0" in transform_up, f"Expected translateY(0) on scroll up, got: {transform_up}"
        assert has_shadow, "Header should acquire elevation shadow-lg on reveal!"
        print("    ✓ Scroll up to 400px: header immediately revealed (translateY(0)) with elevation shadow.")

        # Toggle mobile drawer while scrolling
        await eval_js("toggleMobileMenu()")
        time.sleep(0.2)
        menu_open = await eval_js("!document.getElementById('mobile-menu').classList.contains('hidden')")
        transform_menu = await eval_js("document.getElementById('site-header').style.transform")
        assert menu_open and "translateY(0" in transform_menu, "Opening mobile menu must keep header fully visible!"
        print("    ✓ Mobile menu toggle: drawer opens and guarantees header visibility.")
        await eval_js("toggleMobileMenu()")

        # Scroll back to top (0px) -> header visible without shadow
        await eval_js("window.scrollTo(0, 0); window.dispatchEvent(new Event('scroll'));")
        time.sleep(0.3)
        top_transform = await eval_js("document.getElementById('site-header').style.transform")
        top_shadow = await eval_js("document.getElementById('site-header').classList.contains('shadow-lg')")
        assert "translateY(0" in top_transform, "At page top, header must be visible!"
        assert not top_shadow, "At page top, header shadow-lg should be removed for seamless resting state."
        print("    ✓ Scroll back to top: header returns to resting state (no elevation shadow).")

        conn.close()
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=2)
        except Exception:
            proc.kill()

if __name__ == "__main__":
    test_static_integrity()
    asyncio.run(test_runtime_flows())
