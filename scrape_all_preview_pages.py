import asyncio
import json
import tornado.websocket
from bs4 import BeautifulSoup

PAGES = ['/', '/termekek', '/egyedi-receptura', '/cegunkrol']

async def scrape_pages():
    with open(r'C:\Users\csern\AppData\Local\Google\Chrome\User Data\DevToolsActivePort') as f:
        port = f.readline().strip()
        path = f.readline().strip()

    conn = await tornado.websocket.websocket_connect(f"ws://127.0.0.1:{port}{path}", max_message_size=100*1024*1024)
    req_id = 1

    await conn.write_message(json.dumps({"id": req_id, "method": "Target.getTargets"}))
    targets = json.loads(await conn.read_message())["result"]["targetInfos"]
    preview_target = [t for t in targets if "chatgpt.site" in t.get("url", "")][0]

    req_id += 1
    await conn.write_message(json.dumps({
        "id": req_id,
        "method": "Target.attachToTarget",
        "params": {"targetId": preview_target["targetId"], "flatten": True}
    }))
    session_id = None
    while not session_id:
        msg = json.loads(await conn.read_message())
        if msg.get("method") == "Target.attachedToTarget":
            session_id = msg.get("params", {}).get("sessionId")
        elif msg.get("id") == req_id and "result" in msg:
            session_id = msg.get("result", {}).get("sessionId")

    all_content = {}

    for page in PAGES:
        url = f"https://preview-48e02ae0823cb68d1fccb4f5.vecseiandras11.chatgpt.site{page}"
        print(f"Navigating to {url}...")
        req_id += 1
        await conn.write_message(json.dumps({
            "id": req_id,
            "sessionId": session_id,
            "method": "Page.navigate",
            "params": {"url": url}
        }))
        while True:
            m = json.loads(await conn.read_message())
            if m.get("id") == req_id:
                break

        await asyncio.sleep(2) # let it render

        req_id += 1
        await conn.write_message(json.dumps({
            "id": req_id,
            "sessionId": session_id,
            "method": "Runtime.evaluate",
            "params": {"expression": "document.documentElement.outerHTML", "returnByValue": True}
        }))
        while True:
            m = json.loads(await conn.read_message())
            if m.get("id") == req_id:
                html = m.get("result", {}).get("result", {}).get("value", "")
                all_content[page] = html
                break

    with open(r'c:\Users\csern\Desktop\sun valley\all_preview_pages.json', 'w', encoding='utf-8') as f:
        json.dump(all_content, f, ensure_ascii=False, indent=2)

    print("All pages scraped successfully!")
    conn.close()

if __name__ == "__main__":
    asyncio.run(scrape_pages())
