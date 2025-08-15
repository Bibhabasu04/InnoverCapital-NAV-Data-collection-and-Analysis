import glob
import re

import pandas as pd
from playwright.sync_api import Playwright, sync_playwright, expect

company = "HDFC Life"


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.hdfclife.com/fund-performance")
    page.get_by_role("link", name="View All", exact=True).first.click()
    page.locator("li").filter(has_text="Debts").click()

    date = page.locator(
        ".tab2 > .product-wrap > div > .product-inner-list > .tab-wrap > .tab-content > .tab9 > .product-top-data > div > .product-date-txt").first.text_content()

    # data = [[company, " "],["Fund", date]]
    data = []

    page.get_by_role("heading", name="Bond Fund").click()
    nav = (page.locator(
        ".tab2 > .product-wrap > div > .product-inner-list > .tab-wrap > .tab-content > .tab9 > .product-top-data > div > .product-data-txt").first.text_content())
    data.append([nav])
    # data.append([company, "Bond Fund (Debt)", nav])

    page.get_by_role("heading", name="Liquid Fund").click()
    nav = page.locator(
        ".tab2 > .product-wrap > div:nth-child(2) > .product-inner-list > .tab-wrap > .tab-content > .tab9 > .product-top-data > div > .product-data-txt").text_content()
    data.append([nav])
    # data.append([company, "Liquid Fund (Debt)", nav])

    page.get_by_role("heading", name="Bond Plus Fund").click()
    nav = page.locator(
        ".tab2 > .product-wrap > div:nth-child(3) > .product-inner-list > .tab-wrap > .tab-content > .tab9 > .product-top-data > div > .product-data-txt").text_content()
    data.append([nav])
    # data.append([company, "Bond Plus Fund (Debt)", nav])

    page.locator("li").filter(has_text="Hybrid").click()

    page.get_by_role("heading", name="Balanced Fund").click()
    nav = page.locator(
        ".tab3 > .product-wrap > div > .product-inner-list > .tab-wrap > .tab-content > .tab9 > .product-top-data > div > .product-data-txt").first.text_content()
    # data.append([company, "Balanced Fund (Hybrid)", nav])
    data.append([nav])

    page.get_by_role("heading", name="Secure Advantage Fund").click()
    nav = page.locator(
        ".tab3 > .product-wrap > div:nth-child(2) > .product-inner-list > .tab-wrap > .tab-content > .tab9 > .product-top-data > div > .product-data-txt").text_content()
    data.append([nav])
    # data.append([company, "Secure Advantage Fund (Hybrid)", nav])

    df = pd.DataFrame(data)
    # print(df)

    # csv_files = glob.glob("*.csv")  # List of CSV files in the current directory
    # if csv_files:
    #     csv_file_path = csv_files[0]  # Use the first found CSV file
    #     # Append data with a blank line above
    #     with open(csv_file_path, 'a') as file:
    #         file.write('\n')  # Add a blank line
    #     df.to_csv(csv_file_path, mode='a', header=False, index=False)
    df.to_csv(f"D:/Innover/Daily nav/HDFC.csv", mode='w', header=False, index=False)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


