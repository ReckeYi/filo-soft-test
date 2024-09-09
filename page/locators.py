from selenium.webdriver.common.by import By


class GoogleLocators:
    SEARCH_BOX = (By.NAME, "q")
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//*[@id='L2AGLb']/div")
    SEARCH_RESULTS = (By.XPATH, "//h3")
