import time 
from playwright.sync_api import sync_playwright

def login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.goto("https://the-internet.herokuapp.com/login")
            
            page.fill("#username", "tomsmith")
            page.fill("#password", "SuperSecretPassword!")
            
            page.click("button[type='submit']")
            
            print("Login successful!")
            
        except Exception as e:
            print(f"Login failed: {e}")
            
        finally:
            time.sleep(3)
            browser.close()

if __name__ == "__main__":
    login()
    
    