import time
from playwright.sync_api import sync_playwright

def test_dynamic_elements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
            
            # Add 3 elements
            for _ in range(3):
                page.click("button[onclick='addElement()']")
            
            delete_buttons = page.locator(".added-manually")
            count = delete_buttons.count()
            
            assert count == 3, f"Expected 3 elements, found {count}"
            print("Successfully added and verified 3 elements")
            
            
            
        except Exception as e:
            print(f"Test failed: {e}")
            
        finally:
            time.sleep(5)
            browser.close()

if __name__ == "__main__":
    test_dynamic_elements()