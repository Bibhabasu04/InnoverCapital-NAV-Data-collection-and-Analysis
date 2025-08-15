import re
import time
import pandas as pd
from playwright.sync_api import Playwright, sync_playwright, expect
from datetime import datetime, timedelta

today = datetime.now() - timedelta(days=1)
date = today.strftime("%d/%m/%Y")
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    choices = [172,173,180,181,187,188,191,193,194,197,802,803,811,835,849,867,873,901,902]
    list = [24]
    all = pd.DataFrame([])
    for j in list:
        # date = f"{j}/01/2025"
        print(date)
        data = [[date]]
        for choice in choices:
            page.goto("https://licindia.in/nav-history")
            page.locator("iframe[name=\"searchFrame\"]").content_frame.locator(
                "input[name=\"\\{actionForm\\.fromDate\\}\"]").click()
            page.locator("iframe[name=\"searchFrame\"]").content_frame.locator(
                "input[name=\"\\{actionForm\\.fromDate\\}\"]").fill(date)
            page.locator("iframe[name=\"searchFrame\"]").content_frame.locator(
                "input[name=\"\\{actionForm\\.toDate\\}\"]").click()
            page.locator("iframe[name=\"searchFrame\"]").content_frame.locator(
                "input[name=\"\\{actionForm\\.toDate\\}\"]").fill(date)

            page.locator("iframe[name=\"searchFrame\"]").content_frame.locator(
                "[id=\"wlw-select_key\\:\\{actionForm\\.planNo\\}\"]").select_option(f"{choice}")
            page.locator("iframe[name=\"searchFrame\"]").content_frame.get_by_role("button", name="Get NAV Value").click()
            time.sleep(1.5)
            table = page.locator("iframe[name=\"searchFrame\"]").content_frame.get_by_role("table")
            rows = table.locator("tr")
            # fund_data = []
            for row in rows.element_handles()[3:]:
                columns = row.query_selector_all("td")
                row_data = [col.inner_text() for col in columns]
                data.append([row_data[2]])
            # data.append(fund_data)
        df = pd.DataFrame(data)
        all = pd.concat([all, df], axis = 1, ignore_index = True)
    print(df)
    # all.to_csv(f"D:/Innover/lic_history.csv", mode = "w", header=False, index=False)
    # all.to_csv(f"D:/Innover/Daily nav/spare.csv", mode = "w", header=False, index=False)
    all.to_csv(f"D:/Innover/Daily nav/LIC.csv", mode = "w", header=False, index=False)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
