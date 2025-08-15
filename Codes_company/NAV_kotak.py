from playwright.sync_api import sync_playwright, expect
import pandas as pd
from datetime import datetime, timedelta


today = datetime.now() - timedelta(days=1)
date = today.strftime("%B %d, %Y")
company = "Kotak Life"

# def main():
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.kotaklife.com/fund-performance/nav-performance")
    page.get_by_role("link", name="Latest NAV").click()
    # page.get_by_role("link", name="Previous NAV").click()

    page.wait_for_selector("table", timeout=10000)
    page.get_by_role("heading", name=f"Unit Values as on {date}").click()


    # Extract table rows
    rows = page.locator("table tbody tr")
    # data = [[company, " "],["Fund", date]]
    data = [[date]]
    for row in rows.element_handles()[1:]:
        columns = row.query_selector_all("td")
        row_data = []
        for col in columns:
            row_data.append(col.inner_text())
        # print(row_data)
        if len(row_data) > 1 and len(data) < 49:
            data.append([row_data[1]])
    df = pd.DataFrame(data)
    # print(df)

    browser.close()

df.to_csv(f"D:/Innover/Daily nav/Kotak.csv", mode='w', header=False, index=False)



