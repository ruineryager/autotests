from selenium.webdriver.common.by import By


class Product:
    def __init__(self, browser):
        self.browser = browser

    def check(self, title):
        title = self.browser.find_element(By.CSS_SELECTOR, 'h2')
        assert title.text

    def check_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count
