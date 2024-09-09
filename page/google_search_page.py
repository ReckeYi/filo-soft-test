from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import *
from page.locators import GoogleLocators


class GooglePage:

    def __init__(self, driver):
        self.driver = driver
        self.page_url = URL

    def open_page(self):
        self.driver.get(self.page_url)

    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(GoogleLocators.ACCEPT_COOKIES_BUTTON)
            ).click()
        except Exception as e:
            print(e, "Cookies banner not found or was closed")

    def search_phrase(self):
        search_box = self.driver.find_element(*GoogleLocators.SEARCH_BOX)
        search_box.send_keys(KEYWORD)
        search_box.send_keys(Keys.RETURN)

    def check_search_results(self):
        results = self.driver.find_elements(*GoogleLocators.SEARCH_RESULTS)
        matches = [result.text for result in results if KEYWORD.lower() in result.text.lower()]
        return matches

