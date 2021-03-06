from selenium.webdriver.chrome.webdriver import WebDriver
from src.main.tool.DriverFactory import CSS_Search_Element

def get_last_page(driver: WebDriver):
    try:
        result = CSS_Search_Element(driver, ".pagination-widget__page-link_last")
        last_page = result.find_element_by_xpath('..').get_attribute("data-page-number")
    except:
        last_page=1
    return int(last_page)
