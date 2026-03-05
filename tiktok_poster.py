from playwright.sync_api import sync_playwright

def upload_tiktok(video):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.tiktok.com/login")

        input("Login then press enter")

        page.goto("https://www.tiktok.com/upload")

        page.set_input_files("input[type=file]", video)

        page.click("button:has-text('Post')")

        browser.close()
