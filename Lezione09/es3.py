import time
from playwright.sync_api import sync_playwright

def handle_checkboxes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.goto("https://the-internet.herokuapp.com/checkboxes")
            
            # Get all checkboxes
            checkboxes = page.locator("input[type='checkbox']")
            checkbox_count = checkboxes.count()
            
            print(f"Found {checkbox_count} checkboxes on the page")
            time.sleep(2)
            
            # Select only unchecked checkboxes
            for i in range(checkbox_count):
                checkbox = checkboxes.nth(i)
                if not checkbox.is_checked():
                    checkbox.check()
                
            unchecked_count = page.locator("input[type='checkbox']:not(:checked)").count()
            assert unchecked_count == 0, f"{unchecked_count} checkboxes remain unchecked"
            print("All checkboxes are now checked")
            
        except Exception as e:
            print(f"Error occurred: {e}")
            
        finally:
            time.sleep(5)
            browser.close()

if __name__ == "__main__":
    handle_checkboxes()