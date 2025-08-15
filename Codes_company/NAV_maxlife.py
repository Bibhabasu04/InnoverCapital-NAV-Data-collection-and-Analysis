import glob
import re
import pandas as pd
from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

today = datetime.now() - timedelta(days=1)
date = today.strftime("%d %B %Y")
day = int(today.strftime("%d"))
month = today.strftime("%B")
year = today.strftime("%Y")
count = 0
company = "Max Life Insurance"
# data = [[company, " "],['Fund', date]]
data = [[date]]

def close_ads(webpage):
    try:
        webpage.locator("#bread-crumb-wrapper-container path").nth(2).click()
    except Exception as e:
        # print("Error", end = " ")
        print(" ", end=" ")

def get(page):
    global count, data
    close_ads(page)
    # plan = "#bread-crumb-wrapper-container > main > div > div.jsx-3153974416.w-full.page-container > div > div.jsx-368459968.fundpeformanceWrapper > div.jsx-368459968.selectBoxWrapper > div.jsx-368459968.first-selectbox > div.CustomSelectBox_custom-select-container__yF1RU.undefined > div > div"
    # fund = "#bread-crumb-wrapper-container > main > div > div.jsx-3153974416.w-full.page-container > div > div.jsx-368459968.fundpeformanceWrapper > div.jsx-368459968.selectBoxWrapper > div.jsx-368459968.second-selectbox > div.CustomSelectBox_custom-select-container__yF1RU.undefined > div > div"
    # nav = "#bread-crumb-wrapper-container > main > div > div.jsx-3153974416.w-full.page-container > div > div.jsx-368459968.fundpeformanceWrapper > div.jsx-368459968.nav-status-wrapper > div.jsx-368459968.current-nav > div.jsx-368459968.value"
    # nav = "#bread-crumb-wrapper-container > main > div > div.jsx-3153974416.w-full.page-container > div > div.jsx-3072576809.fundpeformanceWrapper > div.jsx-3072576809.nav-status-wrapper > div.jsx-3072576809.current-nav > div.jsx-3072576809.value"
    nav = "#bread-crumb-wrapper-container > main > div > div.jsx-3153974416.w-full.page-container > div.jsx-2562724715.flex.flex-wrap.w-full.lead-page.bg-default > div.jsx-4119301322.fundpeformanceWrapper > div.jsx-4119301322.nav-status-wrapper > div.jsx-4119301322.current-nav > div.jsx-4119301322.value"
    # plan = BeautifulSoup(page.inner_html(plan), "html.parser").get_text()
    # fund = BeautifulSoup(page.inner_html(fund), "html.parser").get_text()
    nav = BeautifulSoup(page.inner_html(nav), "html.parser").get_text().replace(f"as on {day} {month} {year}", "")
    if count == 0:
        print(nav)
    # nav = nav.replace(f"as on {date}", "")
    count += 1
    print(f"{count}", end = " ")
    # data.append([company, f"{plan} - {fund}", nav])
    data.append([nav])
    # close_ads(page)

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://www.maxlifeinsurance.com/customer-servicing/fund-performance-result")
    page.locator("#bread-crumb-wrapper-container span").nth(1).click()
    #
    page.set_default_timeout(3000)
    context.set_default_timeout(3000)

    ########################

    page.get_by_text("Max Life Life Maker Premium").click()
    page.locator("#bread-crumb-wrapper-container span").nth(2).click()
    page.get_by_text("Balance Fund").click()
    page.get_by_role("button", name="Submit").click()
    get(page)

    page.locator("div").filter(has_text=re.compile(r"^Fund TypeBalance Fund$")).locator("span").click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    
    page.locator("div").filter(has_text=re.compile(r"^Fund TypeConservative Fund$")).locator("span").click()
    page.get_by_text("Secure Fund").click()
    get(page)
    
    page.locator("div").filter(has_text=re.compile(r"^Fund TypeSecure Fund$")).locator("span").click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    
    page.locator("div").filter(has_text=re.compile(r"^Fund TypeGrowth Fund$")).locator("span").click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    #########################

    page.locator("div").filter(has_text=re.compile(r"^Plan NameMax Life Life Maker Premium$")).locator("span").click()
    page.get_by_text("Max Life Smart Assure").click()
    page.locator("div:nth-child(3) > .CustomSelectBox_custom-select-container__yF1RU > .CustomSelectBox_select-input__pOkG2 > .CustomSelectBox_select-arrow__kJUgN").click()
    page.get_by_text("Balance Fund").click()

    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Fund TypeBalance Fund$")).locator("span").click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Fund TypeConservative Fund$")).locator("span").click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Fund TypeSecure Fund$")).locator("span").click()
    page.get_by_text("Dynamic Opportunities Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Fund TypeDynamic Opportunities Fund$")).locator("span").click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Fund TypeGrowth Fund$")).locator("span").click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    


    ###########################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Smart Assure$")).first.click()
    page.get_by_text("Max Life SMART Steps").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()

    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    #############################

    page.locator("div").filter(has_text=re.compile(r"^Max Life SMART Steps$")).first.click()
    page.get_by_text("Max Life Fast Track Super").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()

    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Diversified Equity Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Diversified Equity Fund$")).first.click()
    page.get_by_text("Discontinuance Fund Individual").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Discontinuance Fund Individual$")).first.click()
    page.get_by_text("Dynamic Bond Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Dynamic Bond Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("High Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^High Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund II").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund II$")).first.click()
    page.get_by_text("Midcap Momentum Index Fund", exact=True).click()
    get(page)
    

    page.get_by_text("Midcap Momentum Index Fund", exact=True).click()
    page.get_by_text("NIFTY Alpha 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^NIFTY Alpha 50 Fund$")).first.click()
    page.get_by_text("Nifty 500 Momentum 50 Fund", exact=True).click()
    get(page)
    

    page.get_by_text("Nifty 500 Momentum 50 Fund", exact=True).click()
    page.get_by_text("Nifty Momentum Quality 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Nifty Momentum Quality 50 Fund$")).first.click()
    page.get_by_text("NIFTY Smallcap Quality Index Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Fund TypeNIFTY Smallcap Quality Index Fund$")).locator("span").click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Super Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Pure Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Pure Growth Fund$")).first.click()
    page.get_by_text("Sustainable Equity Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Sustainable Equity Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Secure Plus Fund").click()
    get(page)
    

    ##########################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Fast Track Super$")).first.click()
    page.get_by_text("Max Life Fast Track", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()

    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Super Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Secure Plus Fund").click()
    get(page)
    

    ##########################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Fast Track$")).first.click()
    page.get_by_text("Max Life Smart Invest Pension Super").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()

    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Pension Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Pension Secure Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    ###############################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Smart Invest Pension Super$")).first.click()
    page.get_by_text("Max Life Flexi Wealth Advantage Plan", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balanced Fund", exact=True).click()

    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balanced Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Diversified Equity Fund", exact=True).click()
    get(page)
    

    page.get_by_text("Diversified Equity Fund", exact=True).click()
    page.get_by_text("Discontinuance fund individual").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Discontinuance fund individual$")).first.click()
    page.get_by_text("Dynamic Bond Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Dynamic Bond Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("High Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^High Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund II").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund II$")).first.click()
    page.get_by_text("Midcap Momentum Index Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Midcap Momentum Index Fund$")).first.click()
    page.get_by_text("NIFTY Alpha 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^NIFTY Alpha 50 Fund$")).first.click()
    page.get_by_text("Nifty 500 Momentum 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Nifty 500 Momentum 50 Fund$")).first.click()
    page.get_by_text("Nifty Momentum Quality 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Nifty Momentum Quality 50 Fund$")).first.click()
    page.get_by_text("NIFTY Smallcap Quality Index Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^NIFTY Smallcap Quality Index Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Super Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Pure Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Pure Growth Fund$")).first.click()
    page.get_by_text("Sustainable Equity Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Sustainable Equity Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Secure Plus Fund").click()
    get(page)
    

    ########################################

    page.locator("div").filter(has_text=re.compile(r"^Plan NameMax Life Flexi Wealth Advantage Plan$")).locator("span").click()
    page.get_by_text("Max Life Life Maker Platinum").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()

    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    ########################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Life Maker Platinum$")).first.click()
    page.get_by_text("Max Life Online Savings Plan", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balanced Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balanced Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Diversified Equity Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Diversified Equity Fund$")).first.click()
    page.get_by_text("Dynamic Bond Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Dynamic Bond Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("High Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^High Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund II").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund II$")).first.click()
    page.get_by_text("Midcap Momentum Index Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Midcap Momentum Index Fund$")).first.click()
    page.get_by_text("NIFTY Alpha 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^NIFTY Alpha 50 Fund$")).first.click()
    page.get_by_text("Nifty 500 Momentum 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Nifty 500 Momentum 50 Fund$")).first.click()
    page.get_by_text("Nifty Momentum Quality 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Nifty Momentum Quality 50 Fund$")).first.click()
    page.get_by_text("NIFTY Smallcap Quality Index Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^NIFTY Smallcap Quality Index Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Super Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Pure Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Pure Growth Fund$")).first.click()
    page.get_by_text("Sustainable Equity Fund", exact=True).click()
    get(page)
    

    #####################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Online Savings Plan$")).first.click()
    page.get_by_text("Max Life SMART Xpress").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balanced Fund", exact=True).click()

    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balanced Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Dynamic Opportunities Fund").click()
    get(page)
    

    page.get_by_text("Dynamic Opportunities Fund").click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("High Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^High Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Super Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Secure Plus Fund").click()
    get(page)
    

    ###################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life SMART Xpress$")).first.click()
    page.get_by_text("Max Life Maxis Super").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()

    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Discontinuance Fund Individual").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Discontinuance Fund Individual$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("High Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^High Growth Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    ###################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Maxis Super$")).first.click()
    page.get_by_text("Max Life Shubh Invest").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()

    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    ###################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Shubh Invest$")).first.click()
    page.get_by_text("Max Life SMART Invest Pension Plus").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()

    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Pension Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Pension Secure Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    ##########################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life SMART Invest Pension Plus$")).first.click()
    page.get_by_text("Max Life Life Maker Pension").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Pension Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Pension Secure Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    #####################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Life Maker Pension Plan$")).first.click()
    page.get_by_text("Max Life Smart Flexi Protect").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Diversified Equity Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Diversified Equity Fund$")).first.click()
    page.get_by_text("Discontinuance fund individual").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Discontinuance fund individual$")).first.click()
    page.get_by_text("Dynamic Bond Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Dynamic Bond Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("High Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^High Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund II").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund II$")).first.click()
    page.get_by_text("Midcap Momentum Index Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Midcap Momentum Index Fund$")).first.click()
    page.get_by_text("NIFTY Alpha 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^NIFTY Alpha 50 Fund$")).first.click()
    page.get_by_text("Nifty 500 Momentum 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Nifty 500 Momentum 50 Fund$")).first.click()
    page.get_by_text("Nifty Momentum Quality 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Nifty Momentum Quality 50 Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Super Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Pure Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Pure Growth Fund$")).first.click()
    page.get_by_text("Sustainable Equity Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Sustainable Equity Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Secure Plus Fund").click()
    get(page)
    

    #######################################

    page.get_by_text("Max Life Smart Flexi Protect").click()
    page.get_by_text("Max Life Flexi Wealth Plus").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balanced Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balanced Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Diversified Equity Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Diversified Equity Fund$")).first.click()
    page.get_by_text("Discontinuance fund individual").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Discontinuance fund individual$")).first.click()
    page.get_by_text("Dynamic Bond Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Dynamic Bond Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("High Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^High Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund II").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund II$")).first.click()
    page.get_by_text("Midcap Momentum Index Fund", exact=True).click()
    get(page)
    

    page.get_by_text("Midcap Momentum Index Fund", exact=True).click()
    page.get_by_text("Nifty 500 Momentum 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Nifty 500 Momentum 50 Fund$")).first.click()
    page.get_by_text("NIFTY Alpha 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^NIFTY Alpha 50 Fund$")).first.click()
    page.get_by_text("Nifty Momentum Quality 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Nifty Momentum Quality 50 Fund$")).first.click()
    page.get_by_text("NIFTY Smallcap Quality Index Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^NIFTY Smallcap Quality Index Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Super Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Pure Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Pure Growth Fund$")).first.click()
    page.get_by_text("Sustainable Equity Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Sustainable Equity Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Secure Plus Fund").click()
    get(page)
    

    ###################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Flexi Wealth Plus$")).first.click()
    page.get_by_text("Max Life Life Maker Gold").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balanced Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balanced Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    ########################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Life Maker Gold$")).first.click()
    page.get_by_text("Max Life Shiksha Plus Super").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Discontinuance Fund Individual").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Discontinuance Fund Individual$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("High Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^High Growth Fund$")).first.click()
    page.get_by_text("Midcap Momentum Index Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Midcap Momentum Index Fund$")).first.click()
    page.get_by_text("NIFTY Alpha 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^NIFTY Alpha 50 Fund$")).first.click()
    page.get_by_text("Nifty 500 Momentum 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Nifty 500 Momentum 50 Fund$")).first.click()
    page.locator("li").filter(has_text=re.compile(r"^Nifty 500 Momentum 50 Fund$")).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Nifty 500 Momentum 50 Fund$")).first.click()
    page.get_by_text("Nifty Momentum Quality 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Nifty Momentum Quality 50 Fund$")).first.click()
    page.get_by_text("NIFTY Smallcap Quality Index Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^NIFTY Smallcap Quality Index Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Super Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Secure Plus Fund").click()
    get(page)
    

    ##################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Shiksha Plus Super$")).first.click()
    page.get_by_text("Max Life Top Gear").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    #############################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Top Gear$")).first.click()
    page.get_by_text("Max Life Flexi Fortune").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Super Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Secure Plus Fund").click()
    get(page)
    

    #####################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Flexi Fortune$")).first.click()
    page.get_by_text("Max Life Unit Builder", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Dynamic Opportunities Fund").click()
    get(page)
    

    ################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Unit Builder$")).first.click()
    page.get_by_text("Max Life Capital Builder").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("High Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^High Growth Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    ################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Capital Builder$")).first.click()
    page.get_by_text("Max Life Amsure Magic Builder").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Dynamic Opportunities Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Dynamic Opportunities Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    ##################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Amsure Magic Builder$")).first.click()
    page.get_by_text("Max Life Platinum Wealth Plan").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Diversified Equity Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Diversified Equity Fund$")).first.click()
    page.get_by_text("Discontinuance Fund Individual").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Discontinuance Fund Individual$")).first.click()
    page.get_by_text("Dynamic Bond Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Dynamic Bond Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("High Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^High Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund II").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund II$")).first.click()
    page.get_by_text("Midcap Momentum Index Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Midcap Momentum Index Fund$")).first.click()
    page.get_by_text("NIFTY Alpha 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^NIFTY Alpha 50 Fund$")).first.click()
    page.get_by_text("Nifty 500 Momentum 50 Fund", exact=True).click()
    get(page)
    

    page.get_by_text("Nifty 500 Momentum 50 Fund", exact=True).click()
    page.get_by_text("Nifty Momentum Quality 50 Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Nifty Momentum Quality 50 Fund$")).first.click()
    page.get_by_text("NIFTY Smallcap Quality Index Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^NIFTY Smallcap Quality Index Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Super Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Pure Growth Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Pure Growth Fund$")).first.click()
    page.get_by_text("Sustainable Equity Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Sustainable Equity Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Secure Plus Fund").click()
    get(page)
    

    ######################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Platinum Wealth Plan$")).first.click()
    page.get_by_text("Max Life Shiksha Plus", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Dynamic Opportunities Fund").click()
    get(page)
    

    page.get_by_text("Dynamic Opportunities Fund").click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    ######################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Shiksha Plus$")).first.click()
    page.get_by_text("Max Life Life Invest Plan").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("li").filter(has_text="Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    ###################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Life Invest Plan$")).first.click()
    page.get_by_text("Max Life Forever Young").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Pension Preserver Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Pension Preserver Fund$")).first.click()
    page.get_by_text("Pension Maximiser Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Pension Maximiser Fund$")).first.click()
    page.get_by_text("Discontinuance Fund Pension").click()
    get(page)
    

    ###################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Forever Young Pension Plan$")).first.click()
    page.get_by_text("Max Life Unit Builder Plus").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Dynamic Opportunities Fund").click()
    get(page)
    

    page.get_by_text("Dynamic Opportunities Fund").click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    ##############################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Unit Builder Plus$")).first.click()
    page.get_by_text("Max Life Shiksha Plus II").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Super Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Secure Plus Fund").click()
    get(page)
    

    ######################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Shiksha Plus II$")).first.click()
    page.get_by_text("Max Life Fortune Builder").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Dynamic Opportunities Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Dynamic Opportunities Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    #############################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Fortune Builder$")).first.click()
    page.get_by_text("Unclaimed Policyholder Account").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    #############################

    page.locator("div").filter(has_text=re.compile(r"^Unclaimed Policyholder Account$")).first.click()
    page.get_by_text("Max Life SMART Invest Pension", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Pension Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Pension Secure Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Growth Super Fund Pension").click()
    get(page)
    

    #####################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life SMART Invest Pension$")).first.click()
    page.get_by_text("Max Life Amsure Secure").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.get_by_text("Guaranteed Dynamic Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Guaranteed Dynamic Fund$")).first.click()
    page.get_by_text("Guaranteed Income Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Guaranteed Income Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund").click()
    get(page)
    

    ########################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Amsure Secure Returns Builder$")).first.click()
    page.get_by_text("Max Life Life Maker Unit").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    #################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Life Maker Unit Linked Investment plan$")).first.click()
    page.get_by_text("Max Life Maxis", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    page.get_by_text("Secure Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Secure Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Growth Fund$")).first.click()
    page.get_by_text("Money Market Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Money Market Fund$")).first.click()
    page.get_by_text("Growth Super Fund", exact=True).click()
    get(page)
    

    ##################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Maxis$")).first.click()
    page.get_by_text("Max Life Group Superannuation").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()

    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    ####################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Group Superannuation$")).first.click()
    page.get_by_text("Max Life Group Gratuity", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    ######################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Group Gratuity$")).first.click()
    page.get_by_text("Max Life Group Gratuity Plus").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.get_by_text("Bond Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Bond Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    #################################

    page.locator("div").filter(has_text=re.compile(r"^Max Life Group Gratuity Plus$")).first.click()
    page.get_by_text("Max Life Group Gratuity Premier Plan").click()
    page.locator("div").filter(has_text=re.compile(r"^Fund Type$")).first.click()
    page.get_by_text("Balance Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Balance Fund$")).first.click()
    page.get_by_text("Bond Fund", exact=True).click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Bond Fund$")).first.click()
    page.locator("#bread-crumb-wrapper-container").get_by_text("Conservative Fund").click()
    get(page)
    

    page.locator("div").filter(has_text=re.compile(r"^Conservative Fund$")).first.click()
    page.get_by_text("Growth Fund", exact=True).click()
    get(page)
    

    ###############################

    df = pd.DataFrame(data)
    # print(df)
    # csv_files = glob.glob("*.csv")  # List of CSV files in the current directory
    # if csv_files:
    #     csv_file_path = csv_files[0]  # Use the first found CSV file
    #     # Append data with a blank line above
    #     with open(csv_file_path, 'a') as file:
    #         file.write('\n')  # Add a blank line
    #     df.to_csv(csv_file_path, mode='a', header=False, index=False)

    df.to_csv(f"D:/Innover/Daily nav/Maxlife.csv", mode='w', header=False, index=False)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
