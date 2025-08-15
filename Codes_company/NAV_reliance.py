import re
import time

import pandas as pd
from playwright.sync_api import Playwright, sync_playwright, expect
from datetime import datetime, timedelta

today = datetime.now() - timedelta(days=1)
yesterday = today - timedelta(days=1)
day = today.strftime("%d-%m-%Y")
date = int(today.strftime("%d"))
ye_date = int(yesterday.strftime("%d"))

company = "Reliance Nippon"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # choices = [1, 2, 3, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24]
    choices = [date]
    page.goto("https://www.reliancenipponlife.com/fund-performance-history")
    total = pd.DataFrame([])
    for choice in choices:
        print(f"{choice}-01-2025")
        try:
            page.get_by_role("button", name="").click()
        except Exception as e:
            print("Error")
        page.locator("#fromDate").click()
        page.get_by_role("cell", name=f"{ye_date}", exact=True).first.click()
        page.locator("#toDate").click()
        page.get_by_role("cell", name=f"{choice}", exact=True).first.click()
        # page.locator("#fromDate").click()
        # page.get_by_role("cell", name="30").click()
        # page.locator("#toDate").click()
        # page.get_by_role("cell", name="1", exact=True).first.click()
        page.get_by_role("button", name="go").click()
        data = [[day]]
        # page.locator("ul").filter(has_text="01 Jan 2025 Life Pure Equity Fund 1").get_by_role("listitem").first.click()
        for i in range(2, 85):
            fund = page.locator(f"#div_nav_data > ul:nth-child({i}) > li:nth-child(2) > span").text_content()
            nav = page.locator(f"#div_nav_data > ul:nth-child({i}) > li:nth-child(3) > span").text_content()
            # print(nav)
            data.append([nav])
        df = pd.DataFrame(data)
        total = pd.concat([total, df], axis = 1)
    print(total)
    total.to_csv(f"D:/Innover/Daily nav/{company}.csv", mode = "w", header=False, index=False)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
