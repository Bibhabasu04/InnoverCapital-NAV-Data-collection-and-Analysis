import glob
import re
import time

import pandas as pd
from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup

company = "ICICI Prudential"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.iciciprulife.com/fund-performance/all-products-fund-performance-details.html")
    date = BeautifulSoup(page.inner_html("#fund-perform-table > thead > tr > th:nth-child(1) > span > span"), "html.parser").get_text()
    print(date)
    #
    page.get_by_role("link", name="Debt").click()
    rows = page.locator("tr")
    print("debt", len(rows.element_handles()))
    # data = [[company, " "],["Fund", date]]
    data = [[date]]
    for row in rows.element_handles()[1:]:
        columns = row.query_selector_all("td")
        row_data = [col.inner_text() for col in columns]

        # print("1")
        if len(row_data) != 0:
            row_data[0] = f"{row_data[0]}".replace("\n", " ")
            # data.append([company, f"Debt - {row_data[0]}", row_data[3]])
            data.append([row_data[2]])
    time.sleep(5)
    page.get_by_role("link", name="Balanced").click()
    rows = page.locator("tr")
    print("balanced", len(rows.element_handles()))
    for row in rows.element_handles()[1:]:
        columns = row.query_selector_all("td")
        row_data = [col.inner_text() for col in columns]
        # print("2")
        if len(row_data) != 0:
            row_data[0] = f"{row_data[0]}".replace("\n", " ")
            # data.append([company, f"Balanced - {row_data[0]}", row_data[3]])
            data.append([row_data[2]])

    df = pd.DataFrame(data)
    df.to_csv(f"D:/Innover/Daily nav/ICICI.csv", mode='w', header=False, index=False)

    # # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
