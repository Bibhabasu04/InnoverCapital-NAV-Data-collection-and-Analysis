import re
import time

import pandas as pd
from playwright.sync_api import Playwright, sync_playwright, expect
from datetime import datetime, timedelta

today = datetime.now() - timedelta(days=1)
date = today.strftime("%d/%m/%Y")
company = "Bharti AXA"
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.bhartiaxa.com/manage-funds")
    page.get_by_label("Select Fund").click()
    page.get_by_role("option", name="All").click()
    page.get_by_role("button", name="Tabular View").click()
    all = pd.DataFrame([])
    #choices = ["01", "02", "03", "06", "07", "08", "09", "10", "13", "14", "15", "16", "17", "20", "21", "22", "23", "24"]
    #for choice in choices:
    #data = [[f"{choice}/01/2025"]]
    data = [[date]]
    page.locator("input[name=\"fromDate\"]").click()
    page.locator("input[name=\"fromDate\"]").fill(f"{date}_")
    page.locator("input[name=\"toDate\"]").click()
    page.locator("input[name=\"toDate\"]").fill(f"{date}_")
    page.get_by_role("button", name="Show Results").click()
    time.sleep(1)
    table = page.locator("#tab-panel-1 > div > div > div > table")
    rows = table.locator("tr")
    for row in rows.element_handles()[1:]:
        columns = row.query_selector_all("td")
        row_data = [col.inner_text() for col in columns]
        # if choice == "01":
        #     data.append([company, row_data[2], row_data[3]])
        # else:
        data.append([row_data[3]])
    df = pd.DataFrame(data)
    # all = pd.concat([all, df], axis = 1)
    # print(all)
    # all.to_csv(f"D:/Innover/Daily nav/{company}.csv", mode = "w", header=False, index=False)
    df.to_csv(f"D:/Innover/Daily nav/BhartiAXA.csv", mode = "w", header=False, index=False)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
