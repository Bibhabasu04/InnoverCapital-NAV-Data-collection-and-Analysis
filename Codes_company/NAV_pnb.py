import glob
import re
import pandas as pd
from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

company = "Pnb Metlife"

today = datetime.now() #- timedelta(days=1)
start_month = today.strftime("%B")
todays_year = today.strftime("%Y")
todays_month = today.strftime("%b")
todays_date = int(today.strftime("%d"))

yesterday = today - timedelta(days=1)
yesterdays_year = yesterday.strftime("%Y")
yesterdays_month = yesterday.strftime("%b")
yesterdays_date = int(yesterday.strftime("%d"))
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.pnbmetlife.com/investments/track-fund-value.html")
    # page.locator("button").filter(has_text="×").nth(2).click()
    page.get_by_role("button", name="Close").click()
    page.locator("select[name=\"fundName\"]").select_option("All")
    page.locator("select[name=\"timePeriod\"]").select_option("range-of-period")


    # page.get_by_label("From Date").click()
    # try:
    #     page.get_by_role("cell", name=f"{yesterdays_date}").click()
    # except Exception:
    #     try:
    #         page.get_by_role("cell", name=f"{yesterdays_date}").nth(1).click()
    #     except Exception:
    #         print("Error in from-date selection")
    #
    # page.get_by_label("To Date").click()
    # try:
    #     page.get_by_role("cell", name=f"{todays_date}").click()
    # except Exception:
    #     try:
    #         page.get_by_role("cell", name=f"{todays_date}").nth(1).click()
    #     except Exception:
    #         print("Error in from-date selection")

    page.get_by_label("From Date").click()
    page.get_by_role("cell", name=f"{yesterdays_date}", exact=True).first.click()
    page.get_by_label("To Date").click()
    page.get_by_role("cell", name=f"{todays_date}", exact=True).first.click()


    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Show Table").click()
    page1 = page1_info.value
    page1.get_by_role("cell", name="Fund Name").click()

    date = "body > div.content-parsys.parsys > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2)"
    date = BeautifulSoup(page1.inner_html(date), 'html.parser').get_text()
    print(date)
    # data = [[company, " "],["Fund", date]]
    data = [[date]]

    rows = page1.locator("table tbody tr")
    n = len(rows.element_handles())
    k = int(n/2)
    for row in rows.element_handles():
        columns = row.query_selector_all("td")
        row_data = [col.inner_text() for col in columns]
        if len(row_data) != 0: # and len(data) <= 30:
            # data.append([company, row_data[0], row_data[2]])
            data.append([row_data[2]])
    df = pd.DataFrame(data)
    print(df.head)

    df.to_csv(f"D:/Innover/Daily nav/PNB.csv", mode='w', header=False, index=False)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
