import asyncio
import os
import threading
from http.server import SimpleHTTPRequestHandler
import socketserver
from playwright.async_api import async_playwright

class QuietServer(socketserver.TCPServer):
    allow_reuse_address = True

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

PORT = 8789

def run_server():
    with QuietServer(("", PORT), QuietHandler) as httpd:
        httpd.serve_forever()

async def verify():
    # Start local HTTP server in background thread
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    await asyncio.sleep(0.5)

    test_url = f"http://localhost:{PORT}/index.html"
    print(f"Testing URL: {test_url}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(test_url, wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)

        # 1. Initial State: Should be Hungarian
        initial_lang = await page.evaluate("currentLang")
        print(f"Initial currentLang: {initial_lang}")
        assert initial_lang == "hu", f"Expected 'hu', got {initial_lang}"

        # 2. Switch to English
        print("Switching language to EN...")
        await page.evaluate("setLanguage('en')")
        
        # Verify cookie and localStorage
        cookies_str = await page.evaluate("document.cookie")
        ls_lang = await page.evaluate("localStorage.getItem('sv_lang')")
        print(f"Document cookie: {cookies_str}")
        print(f"LocalStorage sv_lang: {ls_lang}")
        assert "sv_lang=en" in cookies_str, f"Cookie missing sv_lang=en! Got: {cookies_str}"
        assert ls_lang == "en", f"LocalStorage missing sv_lang=en! Got: {ls_lang}"

        # 3. Accept Cookies
        print("Accepting cookies...")
        await page.evaluate("acceptCookies()")
        cookies_str_after = await page.evaluate("document.cookie")
        ls_consent = await page.evaluate("localStorage.getItem('sv_cookie_consent')")
        print(f"Document cookie after accept: {cookies_str_after}")
        print(f"LocalStorage sv_cookie_consent: {ls_consent}")
        assert "sv_cookie_consent=accepted" in cookies_str_after, "Cookie missing sv_cookie_consent=accepted!"
        assert ls_consent == "accepted", "LocalStorage missing sv_cookie_consent!"

        # 4. Reload page to test persistence
        print("Reloading page to test persistence...")
        await page.reload(wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)

        reloaded_lang = await page.evaluate("currentLang")
        print(f"Reloaded currentLang: {reloaded_lang}")
        assert reloaded_lang == "en", f"Expected language to persist as 'en', got {reloaded_lang}!"

        # Check if button state and DOM text reflects EN
        btn_en_class = await page.evaluate("document.getElementById('lang-en').className")
        print(f"Button EN class: {btn_en_class}")
        assert "bg-[#a3392e]" in btn_en_class, "EN button is not highlighted after reload!"

        # Check cookie banner is hidden because consent was saved
        banner_classes = await page.evaluate("document.getElementById('cookie-banner').className")
        assert "opacity-0" in banner_classes, "Cookie banner should stay hidden when already accepted!"

        # 5. Switch back to Hungarian and reload
        print("Switching back to Hungarian...")
        await page.evaluate("setLanguage('hu')")
        await page.reload(wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)
        reloaded_lang_hu = await page.evaluate("currentLang")
        print(f"Reloaded currentLang after switching back: {reloaded_lang_hu}")
        assert reloaded_lang_hu == "hu", f"Expected 'hu', got {reloaded_lang_hu}"

        await browser.close()
        print("\n>>> ALL COOKIE AND LANGUAGE PERSISTENCE TESTS PASSED! <<<")

if __name__ == "__main__":
    asyncio.run(verify())
