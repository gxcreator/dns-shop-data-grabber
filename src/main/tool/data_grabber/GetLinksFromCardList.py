from selenium.webdriver.chrome.webdriver import WebDriver
from src.main.tool.DriverFactory import CSS_Search_Elements
from src.main.tool.parser.PriceParser import PriceParser
from src.main.tool.DriverFactory import CSS_Search_Element

def get_links_price_from_card_list(driver: WebDriver) -> [(str, (int, str))]:
    items = CSS_Search_Elements(driver, "div.catalog-item")
    lp: [(str, str, (int, str))] = []

    for item in items:
        a_element = item.find_element_by_css_selector(".product-info__title-link>a")
        link = a_element.get_attribute("href")
        text = a_element.text
        #price = PriceParser(CSS_Search_Element(driver, ".product-min-price__current").text)
        #print(item)
        price = PriceParser(item.find_element_by_css_selector("div.product-min-price__current").text)

        print("--- Parsed item: " + str(text) + " " + str(link) + " " + str(price[0]))

        lp.append((text, link,price))
        #print(lp)
    return lp
