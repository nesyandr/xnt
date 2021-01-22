from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


WAITING_TIMEOUT = 10  # seconds


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.waiting_timeout = 10

    def find_element(self, locator, time=WAITING_TIMEOUT):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=WAITING_TIMEOUT):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")


class BaseXenetaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://www.xeneta.com"

    def open_page(self):
        return self.driver.get(self.base_url)


class CareersPage(BaseXenetaPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://www.xeneta.com/careers"  # TODO make link concatenation?


class DemoPage(BaseXenetaPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://www.xeneta.com/demo"  # TODO make link concatenation?


