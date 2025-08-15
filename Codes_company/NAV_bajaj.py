import glob
import re
import time
#
# from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
#
#
# company = "Bajaj Allianz Life"
#
today = datetime.now() - timedelta(days=1)
yesterday = today - timedelta(days=1)
todays_date = today.strftime("%Y-%m-%d")
yesterdays_date = yesterday.strftime("%Y-%m-%d")
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.bajajallianzlife.com/fund-performance.html")
#     # data = [[company, " "],["Fund", todays_date]]
#     data = [[todays_date]]
#     page.locator("#start_date_nav").fill(todays_date)
#     page.locator("#end_date_nav").fill(todays_date)
#     # page.locator("#start_date_nav").fill("2025-01-01")
#     # page.locator("#end_date_nav").fill("2025-01-29")
#
#
#
#     funds = ["Accelerator M-C Pension Fund",
#              "Accelerator Mid Cap Fund - 2",
#              "Accelerator Mid-Cap Fund",
#              "Asset Allocation Fund",
#              "Asset Allocation Fund Ii",
#              "Asset Allocation Pension Fund",
#              "Assured Return Fund",
#              "Balanced Equity Fund",
#              "Blue Chip Equity Fund",
#              "Bond Fund",
#              "Bond Pension Fund",
#              "Builder Bond Fund",
#              "Cash Fund",
#              "Cash Plus Fund",
#              "Cash Plus Pension",
#              "Debt Fund",
#              "Debt Plus Fund",
#              "Debt Plus Pension",
#              "Discontinue Pension Pol Fund",
#              "Discontinued Life Policy Fund",
#              "Dynamic Asset Allocation Fund",
#              "Equity Fund",
#              "Equity Gain Fund",
#              "Equity Growth Fund",
#              "Equity Growth Fund - 2",
#              "Equity Growth Pension Fund",
#              "Equity Index Fund",
#              "Equity Index Fund Ii",
#              "Equity Index Pension",
#              "Equity Index Pension Fund Ii",
#              "Equity Midcap Fund",
#              "Equity Midcap Plus",
#              "Equity Plus Fund",
#              "Equity Plus Pension",
#              "Flexi Cap Fund",
#              "Group Asset Allocation Fund",
#              "Group Asset Allocation Fund Ii",
#              "Group Balanced Gain Fund Ii",
#              "Group Blue Chip Fund",
#              "Group Debt Fund",
#              "Group Debt Fund Ii",
#              "Group Debt Fund Iii",
#              "Group Employee Care Vip Ii",
#              "Group Equity Fund",
#              "Group Equity Index Fund",
#              "Group Growth Fund Ii",
#              "Group Liquid Fund Ii",
#              "Group Shadow Fund Gss",
#              "Group Shadow Fund Nss",
#              "Group Superann Secure Iii",
#              "Life Long Gain",
#              "Liquid Fund",
#              "Long Term Debt Solution Fund",
#              "Midcap Index Fund",
#              "Nifty 200 Alpha 30 Index Fund",
#              "Nifty 200 Momentum 30 Index Fund",
#              "Nifty Alpha 50 Index Fund",
#              "Pension Builder Fund",
#              "Premier Eq Gain Fund",
#              "Premier Equity Fund",
#              "Premier Equity Growth",
#              "Pure Eq Fund",
#              "Pure Stock Fund",
#              "Pure Stock Fund Ii",
#              "Pure Stock Pension Fund",
#              "Secure Gain Fund",
#              "Shadow Fund - Bsy",
#              "Shadow Fund Csc",
#              "Small Cap Fund",
#              "Smallcap Quality Index Fund",
#              "Stable Gain Fund",
#              "Sustainable Equity Fund",
#              "Unclaimed Fund"]
#
#     for fund in funds:
#         page.locator("#fund_name_nav").select_option(fund)
#         page.get_by_role("button", name="SUBMIT").click()
#         time.sleep(2)
#         rows = page.locator("#navtable").locator("tr")
#         for row in rows.element_handles():
#             columns = row.query_selector_all("td")
#             row_data = [col.inner_text() for col in columns]
#             if len(row_data) != 0:
#                 # data.append([company, fund , row_data[1]])
#                 data.append([row_data[1]])
#     df = pd.DataFrame(data)
#     # print(df)
#     # csv_files = glob.glob("*.csv")  # List of CSV files in the current directory
#     # if csv_files:
#     #     csv_file_path = csv_files[0]  # Use the first found CSV file
#     #     # Append data with a blank line above
#     #     with open(csv_file_path, 'a') as file:
#     #         file.write('\n')  # Add a blank line
#     #     df.to_csv(csv_file_path, mode='a', header=False, index=False)
#     df.to_csv(f"D:/Innover/Daily nav/Bajaj.csv", mode='w', header=False, index=False)
#     # df.to_csv(f"D:/Innover/Daily nav/spare.csv", mode='w', header=False, index=False)
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
#
#
# #tab2C > div > div.fundheading_wrapper > div:nth-child(1) > p.navfund_name


import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.bajajallianzlife.com/fund-performance.html")
    page.locator("#fund_name_nav").select_option("ULIF02610/07/06BONDFUNDLI116")
    page.locator("#fund_nav_start_date").fill(todays_date)
    try:
        page.locator("div").filter(has_text=re.compile(r"^X$")).click()
    except Exception:
        print("No ad")
    page.get_by_role("button", name="Submit").click()
    nav = page.locator("#navtable > table > tbody > tr > td:nth-child(2)").text_content()
    date = page.locator("#navtable > table > tbody > tr > td:nth-child(1)").text_content()
    print(date, nav)
    data = [date, nav]
    df = pd.DataFrame(data)
    print(df)
    df.to_csv(f"D:/Innover/Daily nav/Bajaj.csv", mode='w', header=False, index=False)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
