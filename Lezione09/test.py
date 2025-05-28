from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch() # Puoi usare anche p.firefox o
        p.webkit
        page = browser.new_page()
        page.goto("https://www.alfasoft.it")
        page.wait_for_load_state("networkidle", timeout=5000)
        page.screenshot(path="alfasoft_home.png")
        browser.close()

if __name__ == "__main__":
    main()