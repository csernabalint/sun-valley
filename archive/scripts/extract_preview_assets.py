import asyncio
import json
import base64
import os
import tornado.websocket

ASSETS_TO_DOWNLOAD = [
    '/sun-valley-logo.png',
    '/apricot-hero.png',
    '/familiar-jams-group.png',
    '/exotic-fruits-fresh-v2.png',
    '/technology-baking-pastry-v2.png',
    '/technology-freezing-cake.png',
    '/technology-pumpable-doughnut.png',
    '/custom-recipe-jam-sizes.png',
    '/catalog-extra-jam.png',
    '/catalog-spreadable.png',
    '/catalog-bake-stable.png',
    '/Sun_Valley_B2B_Prospektus_V1_4.pptx'
]

OUTPUT_DIR = r'c:\Users\csern\Desktop\sun valley\prototypes\sun-valley-b2b\assets'

class CDPClient:
    def __init__(self, conn):
        self.conn = conn
        self.req_id = 0
        self.pending = {}

    async def call(self, method, params=None, session_id=None):
        self.req_id += 1
        cid = self.req_id
        req = {"id": cid, "method": method, "params": params or {}}
        if session_id:
            req["sessionId"] = session_id
        await self.conn.write_message(json.dumps(req))

        while True:
            raw = await self.conn.read_message()
            if raw is None:
                raise RuntimeError("Connection closed by browser")
            msg = json.loads(raw)
            if msg.get("id") == cid:
                return msg

async def run():
    with open(r'C:\Users\csern\AppData\Local\Google\Chrome\User Data\DevToolsActivePort') as f:
        port = f.readline().strip()
        path = f.readline().strip()

    ws_url = f"ws://127.0.0.1:{port}{path}"
    print(f"Connecting to browser CDP: {ws_url}")
    conn = await tornado.websocket.websocket_connect(ws_url, max_message_size=100*1024*1024)
    client = CDPClient(conn)

    # 1. Get targets
    targets_resp = await client.call("Target.getTargets")
    targets = targets_resp.get("result", {}).get("targetInfos", [])

    preview_target = None
    for t in targets:
        if "chatgpt.site" in t.get("url", ""):
            preview_target = t
            break

    if not preview_target:
        print("ERROR: ChatGPT preview page target not found!")
        conn.close()
        return

    print(f"Found preview target: {preview_target['targetId']} ({preview_target['url']})")

    # 2. Attach to target
    attach_resp = await client.call("Target.attachToTarget", {
        "targetId": preview_target["targetId"],
        "flatten": True
    })
    session_id = attach_resp.get("result", {}).get("sessionId")
    print(f"Attached with sessionId: {session_id}")

    # 3. Extract page HTML for inspection
    html_resp = await client.call("Runtime.evaluate", {
        "expression": "document.documentElement.outerHTML",
        "returnByValue": True
    }, session_id=session_id)
    page_html = html_resp.get("result", {}).get("result", {}).get("value", "")
    with open(r'c:\Users\csern\Desktop\sun valley\preview_page_dump.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    print(f"Saved preview_page_dump.html ({len(page_html)} chars)")

    # 4. Download each asset using fetch in the page context
    for asset_path in ASSETS_TO_DOWNLOAD:
        filename = os.path.basename(asset_path)
        out_path = os.path.join(OUTPUT_DIR, filename)
        print(f"Fetching {asset_path}...")

        js_code = f"""
        (async () => {{
            try {{
                const res = await fetch('{asset_path}');
                if (!res.ok) return {{ error: res.status + ' ' + res.statusText }};
                const blob = await res.blob();
                return await new Promise((resolve, reject) => {{
                    const reader = new FileReader();
                    reader.onloadend = () => resolve({{ data: reader.result }});
                    reader.onerror = reject;
                    reader.readAsDataURL(blob);
                }});
            }} catch (e) {{
                return {{ error: e.toString() }};
            }}
        }})()
        """

        res_msg = await client.call("Runtime.evaluate", {
            "expression": js_code,
            "awaitPromise": True,
            "returnByValue": True
        }, session_id=session_id)

        eval_result = res_msg.get("result", {}).get("result", {}).get("value", {})

        if not eval_result:
            print(f"  FAILED {asset_path}: empty eval result -> {res_msg}")
            continue

        if "error" in eval_result:
            print(f"  FAILED {asset_path}: {eval_result['error']}")
            continue

        data_url = eval_result.get("data", "")
        if "," in data_url:
            header, b64_data = data_url.split(",", 1)
            file_bytes = base64.b64decode(b64_data)
            with open(out_path, "wb") as out_f:
                out_f.write(file_bytes)
            print(f"  SUCCESS -> {filename} ({len(file_bytes)} bytes)")
        else:
            print(f"  FAILED {asset_path}: unexpected data URL format")

    conn.close()
    print("All assets processed!")

if __name__ == "__main__":
    asyncio.run(run())
