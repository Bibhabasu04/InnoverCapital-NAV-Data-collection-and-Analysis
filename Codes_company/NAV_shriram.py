import re
import time

import pandas as pd
from playwright.sync_api import Playwright, sync_playwright, expect
from datetime import  datetime, timedelta

today = datetime.now() - timedelta(days=1)
date = today.strftime("%d")
# date = 2

company = "Shri Ram Life Insurance"
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.shriramlife.com/services/nav-history")
    page.get_by_label("From Date*").click()
    page.get_by_text(f"{date}", exact=True).nth(1).click()
    page.get_by_label("To Date*").click()
    page.get_by_text(f"{date}", exact=True).first.click()

    # all = pd.DataFrame([f"{i}/01/2025" for i in range(1, 25)])
    data = []
    choices = ["Accelerator", "Balancer", "Conservator", "Conservator Gold"]
    for choice in choices:
        page.get_by_label("Fund Name*").click()
        page.get_by_text(choice, exact=True).click()
        print(choice)
        page.get_by_role("button", name="View History").click()
        time.sleep(1)
        # data = []
        # for i in range(1, 25):
        i = 1
        page_date = page.locator(f"body > app-root > main > app-nav-history > app-simple-form10 > section > div > div.cardWrapper.spacer--large > div > div > div.tableCard.relative.btnTopSpace--large.ng-star-inserted > table > tbody > tr:nth-child({i}) > td:nth-child(1)").text_content()
        nav = page.locator(f"body > app-root > main > app-nav-history > app-simple-form10 > section > div > div.cardWrapper.spacer--large > div > div > div.tableCard.relative.btnTopSpace--large.ng-star-inserted > table > tbody > tr:nth-child({i}) > td.text-right").text_content()
        # e_date = "body > app-root > main > app-nav-history > app-simple-form10 > section > div > div.cardWrapper.spacer--large > div > div > div.tableCard.relative.btnTopSpace--large.ng-star-inserted > table > tbody > tr:nth-child(24) > td:nth-child(1)"
        data.append([nav])
    df = pd.DataFrame(data).T
    # all = pd.concat([all, df], axis = 1)
    # all = all.T
    # all.to_csv(f"D:/Innover/Daily nav/{company}.csv", mode = "w", header=False, index=False)
    df.to_csv(f"D:/Innover/Daily nav/{company}.csv", mode = "w", header=False, index=False)


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
