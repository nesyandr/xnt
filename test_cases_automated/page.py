from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import CareersPageLocators as CareerLocators
from .locators import DemoPageLocators as DemoLocators

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
    sections = [
        CareerLocators.JOIN_US_BANNER,
        CareerLocators.WHAT_WE_DO_BANNER,
        CareerLocators.OUR_VALUES_CONTAINER,
        CareerLocators.GLOBAL_TRIBE_CONTAINER,
        CareerLocators.OPEN_ROLES_CONTAINER
    ]

    join_us_banner_text = [
        CareerLocators.JOIN_US_BANNER_HEADER_REL_XPATH,
        CareerLocators.JOIN_US_BANNER_TEXT1_REL_XPATH,
        CareerLocators.JOIN_US_BANNER_TEXT2_REL_XPATH,
    ]

    what_we_do_section_text = [
        CareerLocators.WHAT_WE_DO_BANNER_HEADER_REL_XPATH,
        CareerLocators.WHAT_WE_DO_BANNER_TEXT_REL_XPATH

    ]

    our_values_tab_links = [
        {CareerLocators.OUR_VALUES_CONTAINER_TAB_LINK1:
             CareerLocators.OUR_VALUES_CONTAINER_TAB_LINK1_TEXT},
        {CareerLocators.OUR_VALUES_CONTAINER_TAB_LINK2:
             CareerLocators.OUR_VALUES_CONTAINER_TAB_LINK2_TEXT},
        {CareerLocators.OUR_VALUES_CONTAINER_TAB_LINK3:
             CareerLocators.OUR_VALUES_CONTAINER_TAB_LINK3_TEXT},
        {CareerLocators.OUR_VALUES_CONTAINER_TAB_LINK4:
             CareerLocators.OUR_VALUES_CONTAINER_TAB_LINK4_TEXT}
    ]

    global_tribe_cards = [
        CareerLocators.GLOBAL_TRIBE_OSLO,
        CareerLocators.GLOBAL_TRIBE_NEW_YORK,
        CareerLocators.GLOBAL_TRIBE_HAMBURG
    ]

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://www.xeneta.com/careers"  # TODO make link concatenation?


class DemoPage(BaseXenetaPage):
    sections = [
        DemoLocators.PROCURE_FREIGHT_BANNER,
        DemoLocators.LEARN_MORE_CONTAINER
    ]

    learn_more_wrappers = [
        DemoLocators.ONE_TO_ONE_DEMO,
        DemoLocators.WATCH_VIDEOS,
        DemoLocators.GROUP_LIVE_DEMO
    ]

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://www.xeneta.com/demo"  # TODO make link concatenation?
