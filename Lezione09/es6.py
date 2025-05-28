import os
import time
import random
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

def enter_hours(username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        try:
            page.goto("https://dipendenti.alfasoft.it/")
            
            # Login
            email_field = page.locator('[formcontrolname="email"]')
            email_field.fill(username)
            
            password_field = page.locator('[formcontrolname="password"]')
            password_field.fill(password)
            
            page.click('button[type="submit"] >> text=Login')

            # Rendicontazione
            page.wait_for_selector('mat-radio-group', state="visible", timeout=5000)

            # random choice (1=smartWorking or 2=working from office)
            choices = [1, 2]
            selected_value = random.choice(choices)
            
            # Click the randomly selected radio button
            radio_selector = f'mat-radio-button[value="{selected_value}"]'
            page.click(radio_selector)
            page.click('button >> text=Rendicontazione Istantanea')
            
        finally:
            time.sleep(5)
            browser.close()

if __name__ == "__main__":
    
    load_dotenv()
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    enter_hours(EMAIL, PASSWORD)