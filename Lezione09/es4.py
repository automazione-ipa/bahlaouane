import os
import time
from playwright.sync_api import sync_playwright

def test_file_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            with open("test_file.txt", "w") as f:
                f.write("This is a test file for upload")
            
            page.goto("https://the-internet.herokuapp.com/upload")
            
            page.set_input_files("#file-upload", "test_file.txt")
            page.click("#file-submit")
            
            assert page.is_visible("h3:has-text('File Uploaded!')")
            filename = page.text_content("#uploaded-files")
            assert filename == "test_file.txt"
            print("File uploaded successfully")
            
        finally:
            time.sleep(5)
            browser.close()
            os.remove("test_file.txt")

if __name__ == "__main__":
    test_file_upload()