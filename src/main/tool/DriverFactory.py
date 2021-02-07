from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from fake_useragent import UserAgent


class DriverFactory:

    def __init__(self, chromedriver_path: str):
        self.__chromedriver_path = chromedriver_path
        chromeOptions = webdriver.ChromeOptions() 
        chromeOptions.add_argument("--no-sandbox") 
        chromeOptions.add_argument("--disable-setuid-sandbox") 

        chromeOptions.add_argument("--remote-debugging-port=0")  # this

        chromeOptions.add_argument("--disable-dev-shm-using") 
        chromeOptions.add_argument("--disable-gpu") 
        chromeOptions.add_argument("start-maximized") 
        chromeOptions.add_argument("disable-infobars") 
        
        chromeOptions.add_argument("--no-proxy-server") 
        chromeOptions.add_argument("--headless") 
        chromeOptions.add_argument("--log-path=/home/ubuntu/chrdrv.log") 

        ua = UserAgent()
        userAgent = ua.random
        print(userAgent)
        chromeOptions.add_argument(f'user-agent={userAgent}')

        self.__chromedriver_options = chromeOptions

    def getDriver(self, url) -> WebDriver:
        driver = webdriver.Chrome(executable_path=self.__chromedriver_path, chrome_options=self.__chromedriver_options, service_args=["--verbose", "--log-path=/home/ubuntu/chrdrv.log"])
        driver.delete_all_cookies()
        driver.execute_cdp_cmd('Network.enable', {})
        driver.execute_cdp_cmd('Network.setCookie', {'domain' : '.dns-shop.ru', 'name': 'city_path', 'value': 'nizhniy-novgorod', 'path' : '/'})
        #driver.add_cookie()
        driver.get(url)
        with open('page.html', 'w+') as f:
            f.write(driver.page_source)
            f.close()
        return driver

    def parse(self, url, parse_logic):
        driver = self.getDriver(url)
        data = parse_logic(driver)
        driver.quit()
        return data


def CSS_Search_Element(driver: WebDriver, css: str) -> WebElement:
    try:
        return WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
    except TimeoutException:
        driver.quit()
        raise

def CSS_Search_Elements(driver: WebDriver, css: str) -> WebElement:
    try:
        return WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css)))
    except TimeoutException:
        driver.quit()
        raise



