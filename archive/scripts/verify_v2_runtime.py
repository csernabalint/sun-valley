import os
import json
import re
import asyncio
import tornado.websocket
from bs4 import BeautifulSoup

HTML_PATH = r"C:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b\index_v2.html"
ASSETS_DIR = r"C:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b\assets"

def verify_static_assets():
    print("=== 1. VERIFYING STATIC ASSETS & REFERENCES ===")
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # 1. Find all img src
    img_srcs = [img.get("src") for img in soup.find_all("img") if img.get("src")]
    print(f"Found {len(img_srcs)} img tags in HTML:")
    for src in set(img_srcs):
        if src.startswith("assets/"):
            full_p = os.path.join(r"C:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b", src.replace("/", os.sep))
            assert os.path.exists(full_p), f"Asset missing: {full_p}"
            size = os.path.getsize(full_p)
            assert size > 1000, f"Asset too small or empty: {full_p} ({size} bytes)"
            print(f"  [OK] {src} ({size} bytes)")
        else:
            print(f"  [EXT] {src}")

    # 2. Check download links
    download_links = [a.get("href") for a in soup.find_all("a", download=True)]
    for href in download_links:
        full_p = os.path.join(r"C:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b", href.replace("/", os.sep))
        assert os.path.exists(full_p), f"Download asset missing: {full_p}"
        size = os.path.getsize(full_p)
        assert size > 1000, f"Download asset empty: {full_p}"
        print(f"  [OK DOWNLOAD] {href} ({size} bytes)")

    # 3. Check i18n keys
    data_i18n_nodes = [node.get("data-i18n") for node in soup.find_all(attrs={"data-i18n": True})]
    print(f"Found {len(data_i18n_nodes)} elements with data-i18n attributes")

    # Extract translations from script
    script_match = re.search(r"const translations\s*=\s*(\{.+?\n\s*\});", html, re.DOTALL)
    assert script_match, "translations object not found in script!"
    print("  [OK] Translations script block found")

    print("Static asset verification passed successfully!\n")

async def verify_browser_interactions():
    print("=== 2. VERIFYING RUNTIME INTERACTIONS VIA CHROME CDP ===")
    with open(r'C:\Users\csern\AppData\Local\Google\Chrome\User Data\DevToolsActivePort') as f:
        port = f.readline().strip()
        path = f.readline().strip()

    import tornado.httpclient
    req = tornado.httpclient.HTTPRequest(f"ws://127.0.0.1:{port}{path}", connect_timeout=15, request_timeout=15)
    conn = await tornado.websocket.websocket_connect(req, max_message_size=100*1024*1024)
    req_id = 1

    # Create new target for index_v2.html
    v2_url = "file:///C:/Users/csern/Desktop/sun%20valley/prototypes/sun-valley-b2b/index_v2.html"
    await conn.write_message(json.dumps({
        "id": req_id,
        "method": "Target.createTarget",
        "params": {"url": v2_url}
    }))
    create_resp = json.loads(await conn.read_message())
    target_id = create_resp["result"]["targetId"]
    print(f"Created target: {target_id}")

    # Attach to target
    req_id += 1
    await conn.write_message(json.dumps({
        "id": req_id,
        "method": "Target.attachToTarget",
        "params": {"targetId": target_id, "flatten": True}
    }))
    session_id = None
    while not session_id:
        m = json.loads(await conn.read_message())
        if m.get("method") == "Target.attachedToTarget":
            session_id = m.get("params", {}).get("sessionId")
        elif m.get("id") == req_id and "result" in m:
            session_id = m.get("result", {}).get("sessionId")

    print(f"Attached session: {session_id}")

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

    await asyncio.sleep(1.5) # allow DOM parse and Lucide icons init

    # Check 1: Title
    title = await call_eval("document.title")
    print(f"Page Title: {title}")
    assert "Sun Valley" in title

    # Check 2: Products rendered
    prod_count = await call_eval("document.querySelectorAll('#product-list > div').length")
    print(f"Rendered products in matrix: {prod_count}")
    assert prod_count == 6, f"Expected 6 products, got {prod_count}"

    # Check 3: Tab switching in Gastro-Catalog
    print("Testing tab switching...")
    t1_title = await call_eval("document.getElementById('cat-title').innerText")
    assert "Sütésálló" in t1_title, f"Tab 1 unexpected title: {t1_title}"
    print(f"  Tab 1 (bake-stable): {t1_title}")

    await call_eval("switchCatalogTab('spreadable')")
    t2_title = await call_eval("document.getElementById('cat-title').innerText")
    assert "Kenhető" in t2_title, f"Tab 2 unexpected title: {t2_title}"
    print(f"  Tab 2 (spreadable): {t2_title}")

    await call_eval("switchCatalogTab('extra-jam')")
    t3_title = await call_eval("document.getElementById('cat-title').innerText")
    assert "Extra" in t3_title, f"Tab 3 unexpected title: {t3_title}"
    print(f"  Tab 3 (extra-jam): {t3_title}")

    # Switch back
    await call_eval("switchCatalogTab('bake-stable')")

    # Check 4: Language switching (HU -> EN -> DE -> HU)
    print("Testing trilingual switching...")
    await call_eval("setLanguage('en')")
    en_hero = await call_eval("document.querySelector('h1').innerText")
    assert "No boil-out" in en_hero, f"EN headline unexpected: {en_hero}"
    print(f"  EN H1: {en_hero[:50]}...")

    await call_eval("setLanguage('de')")
    de_hero = await call_eval("document.querySelector('h1').innerText")
    assert "Kein Auskochen" in de_hero, f"DE headline unexpected: {de_hero}"
    print(f"  DE H1: {de_hero[:50]}...")

    await call_eval("setLanguage('hu')")
    hu_hero = await call_eval("document.querySelector('h1').innerText")
    assert "200 °C felett" in hu_hero, f"HU headline unexpected: {hu_hero}"
    print(f"  HU H1: {hu_hero[:50]}...")

    # Check 5: TDS Modal interaction
    print("Testing TDS modal opening & closing...")
    is_hidden_before = await call_eval("document.getElementById('tds-modal').classList.contains('hidden')")
    assert is_hidden_before is True, "Modal should be hidden initially"

    await call_eval("openTdsModal(1)") # open Kajszibarack
    is_visible = await call_eval("!document.getElementById('tds-modal').classList.contains('hidden')")
    modal_text = await call_eval("document.getElementById('tds-modal-content').innerText")
    assert is_visible is True, "Modal should be visible after openTdsModal"
    assert "Kajszibarack" in modal_text, "Modal should contain Kajszibarack"
    print(f"  Modal successfully opened with Kajszibarack spec!")

    await call_eval("closeTdsModal()")
    is_hidden_after = await call_eval("document.getElementById('tds-modal').classList.contains('hidden')")
    assert is_hidden_after is True, "Modal should be hidden after closeTdsModal"
    print(f"  Modal successfully closed!")

    # Check 6: Responsive Screenshots
    print("Taking responsive screenshots...")
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
                print(f"  Saved screenshot: {filename} ({len(img_data)} bytes)")
                break

    # Clean up target
    req_id += 1
    await conn.write_message(json.dumps({
        "id": req_id,
        "method": "Target.closeTarget",
        "params": {"targetId": target_id}
    }))
    conn.close()
    print("\nALL RUNTIME CDP VERIFICATIONS PASSED 100%!")

if __name__ == "__main__":
    verify_static_assets()
    asyncio.run(verify_browser_interactions())
