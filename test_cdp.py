import asyncio
import json
import tornado.websocket

async def test():
    with open(r'C:\Users\csern\AppData\Local\Google\Chrome\User Data\DevToolsActivePort') as f:
        port = f.readline().strip()
        path = f.readline().strip()
    
    ws_url = f"ws://127.0.0.1:{port}{path}"
    print("Connecting to:", ws_url)
    conn = await tornado.websocket.websocket_connect(ws_url)
    print("Connected successfully!")
    
    # Send Target.getTargets
    msg = {"id": 1, "method": "Target.getTargets", "params": {}}
    await conn.write_message(json.dumps(msg))
    
    resp = await conn.read_message()
    data = json.loads(resp)
    print("Targets count:", len(data.get("result", {}).get("targetInfos", [])))
    for t in data.get("result", {}).get("targetInfos", []):
        if t.get("type") == "page":
            print(f"Page: {t.get('title')} -> {t.get('url')}")
            
    conn.close()

if __name__ == "__main__":
    asyncio.run(test())
