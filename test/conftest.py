import pytest
from selenium import webdriver

from page.google_search_page import GooglePage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def google_page(driver):
    return GooglePage(driver)
