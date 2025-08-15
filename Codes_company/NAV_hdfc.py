import re
import time
import pandas as pd
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.hdfclife.com/fund-performance")

    page.get_by_text("VIEW ALL", exact=True).click()
    page.get_by_role("link", name="HDFC Life Click 2 Retire").click()
    page.get_by_role("link", name="View All", exact=True).first.click()
    page.locator("li").filter(has_text="Debts").click()
    nav = page.locator(".tab2 > .product-wrap > div > .product-inner-list > .tab-wrap > .tab-content > .tab4 > .product-top-data > div > .product-data-txt").text_content()
    date = page.locator(".tab2 > .product-wrap > div > .product-inner-list > .tab-wrap > .tab-content > .tab4 > .product-top-data > div > .product-date-txt").first.text_content()
    data = [[date]]
    print(nav)
    data.append([nav])

    page.goto("https://www.hdfclife.com/fund-performance")
    page.get_by_text("VIEW ALL", exact=True).click()
    page.get_by_role("link", name="HDFC Life Smart Protect Plan").click()
    page.get_by_role("link", name="View All", exact=True).first.click()
    page.locator("li").filter(has_text="Debts").click()
    nav = page.locator(".tab2 > .product-wrap > .product-list > .product-inner-list > .tab-wrap > .tab-content > .tab4 > .product-top-data > div > .product-data-txt").text_content()
    print(nav)
    data.append([nav])

    page.goto("https://www.hdfclife.com/fund-performance")
    page.get_by_text("VIEW ALL", exact=True).click()
    page.get_by_role("link", name="HDFC Life Sampoorn Nivesh", exact=True).click()
    page.get_by_role("link", name="View All", exact=True).first.click()
    page.locator("li").filter(has_text="Debts").click()
    nav = page.locator(".tab2 > .product-wrap > div > .product-inner-list > .tab-wrap > .tab-content > .tab4 > .product-top-data > div > .product-data-txt").first.text_content()
    data.append([nav])
    nav = page.locator(".tab2 > .product-wrap > div:nth-child(3) > .product-inner-list > .tab-wrap > .tab-content > .tab4 > .product-top-data > div > .product-data-txt").text_content()
    print(nav)
    data.append([nav])

    page.goto("https://www.hdfclife.com/fund-performance")
    page.get_by_text("VIEW ALL", exact=True).click()
    page.locator("#fund-list-1").get_by_role("link", name="HDFC Life Click 2 Wealth").click()
    page.get_by_role("link", name="View All", exact=True).first.click()
    page.locator("li").filter(has_text="Debts").click()
    nav = page.locator(".tab2 > .product-wrap > div:nth-child(1) > .product-inner-list > .tab-wrap > .tab-content > .tab4 > .product-top-data > div > .product-data-txt").text_content()
    data.append([nav])
    nav = page.locator(".tab2 > .product-wrap > div:nth-child(2) > .product-inner-list > .tab-wrap > .tab-content > .tab4 > .product-top-data > div > .product-data-txt").text_content()
    print(nav)
    data.append([nav])


    df = pd.DataFrame(data)
    print(df)

    df.to_csv(f"D:/Innover/Daily nav/HDFC.csv", mode='w', header=False, index=False)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
