import time
from dateutil import parser
import pandas as pd
from playwright.sync_api import Playwright, sync_playwright, expect
from datetime import datetime, timedelta


company = "Tata AIA"

today = datetime.now() - timedelta(days=1)
day = int(today.strftime("%d"))
month = int(today.strftime("%m"))
year = today.strftime("%Y")
date = [f"{day}", f"{month}", f"{year}"]

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # date = ["17","1", "2025" ]
    page.goto("https://apps.tataaia.com/ULNAV/funds/daily-Datwisenav.jsp")
    page.locator("#ddlTimePerioddd").select_option(date[0])
    page.locator("#ddlTimePeriodmm").select_option(date[1])
    page.locator("#ddlTimePeriodyy").select_option(date[2])
    page.get_by_role("button", name="Submit").click()
    time.sleep(2)

    # data = [[company, " "]]
    data = [[today.strftime("%d-%m-%Y")]]

    plan = "Tata AIA Individual Life Funds"
    # data.append([company, plan, f"{date[0]}-{date[1]}-{date[2]}"])
    for i in range(2, 58):
        fund = page.inner_html(f"#prodOver > div > div.nav_results.col-md-12 > div:nth-child(3) > div:nth-child({i}) > div:nth-child(1)").replace("&nbsp;", "")
        nav = page.inner_html(f"#prodOver > div > div.nav_results.col-md-12 > div:nth-child(3) > div:nth-child({i}) > div:nth-child(2)")
        # data.append([company, fund, nav])
        data.append([nav])
    plan = "Tata AIA Group Pension Funds"
    # data.append([company, plan, f"{date[0]}-{date[1]}-{date[2]}"])
    for i in range(2, 14):
        fund = page.inner_html(f"#prodOver > div > div.nav_results.col-md-12 > div:nth-child(5) > div:nth-child({i}) > div:nth-child(1)").replace("&nbsp;", "")
        nav = page.inner_html(f"#prodOver > div > div.nav_results.col-md-12 > div:nth-child(5) > div:nth-child({i}) > div:nth-child(2)")
        # data.append([company, fund, nav])
        data.append([nav])
    df = pd.DataFrame(data)
    df.to_csv(f"D:/Innover/Daily nav/Tata.csv", mode='w', header=False, index=False)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
