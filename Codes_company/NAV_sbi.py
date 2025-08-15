import glob
import re

import pandas as pd
from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup

company = "SBI"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.sbilife.co.in/services-check-nav")
    page.locator("#NAVSnapshot").get_by_role("link", name="Proceed").click()
    page.locator("#NAVSnapshotDiv").get_by_role("heading", name="NAV Snapshot").text_content()
    date = BeautifulSoup(page.inner_html("#NAVSnapshotTable > thead > tr:nth-child(2) > td:nth-child(3)"), "html.parser").get_text()
    # data = [[company, " "],["Fund", date]]
    data = [[date]]
    for i in range(3, 43):
        fund = BeautifulSoup(page.inner_html(f"#NAVSnapshotTable > thead > tr:nth-child({i}) > td:nth-child(1)"), "html.parser").get_text()
        nav =  BeautifulSoup(page.inner_html(f"#NAVSnapshotTable > thead > tr:nth-child({i}) > td:nth-child(3)"), "html.parser").get_text()
        # data.append([company, fund, nav])
        data.append(([nav]))
    df = pd.DataFrame(data)
    df.to_csv(f"D:/Innover/Daily nav/SBI.csv", mode='w', header=False, index=False)


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
