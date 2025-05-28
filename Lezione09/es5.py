import time
from playwright.sync_api import sync_playwright

def extract_table_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            page.goto("https://the-internet.herokuapp.com/tables")
            
            # Extract data from Table 1
            table_data = []
            rows = page.locator("#table1 tbody tr")
            
            for row in rows.all():
                cells = row.locator("td")
                table_data.append({
                    "Last Name": cells.nth(0).text_content(),
                    "First Name": cells.nth(1).text_content(),
                    "Email": cells.nth(2).text_content(),
                    "Due": cells.nth(3).text_content(),
                    "Web Site": cells.nth(4).text_content()
                })
            
            # Print extracted data
            print("Table 1 Data:")
            for i, row in enumerate(table_data, 1):
                print(f"Row {i}: {row}")
                
            return table_data
            
        finally:
            time.sleep(5)
            browser.close()

if __name__ == "__main__":
    extract_table_data()