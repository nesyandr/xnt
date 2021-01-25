from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from test_cases_automated import locators

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
    header_links = [
        locators.PageHeaderLocators.OUR_CUSTOMERS,
        locators.PageHeaderLocators.PLATFORM,
        locators.PageHeaderLocators.RESOURCES,
        locators.PageHeaderLocators.COMPANY,
        locators.PageHeaderLocators.SIGN_IN,
        locators.PageHeaderLocators.GET_DEMO,
    ]

    footer_social_networks = [
        locators.PageFooterLocators.SOCIAL_NETWORKS_FACEBOOK,
        locators.PageFooterLocators.SOCIAL_NETWORKS_TWITTER,
        locators.PageFooterLocators.SOCIAL_NETWORKS_YOUTUBE,
        locators.PageFooterLocators.SOCIAL_NETWORKS_INSTAGRAM
    ]

    footer_information = [
        locators.PageFooterLocators.INFORMATION_HEADER,
        locators.PageFooterLocators.INFORMATION_SHIPPERS,
        locators.PageFooterLocators.INFORMATION_FREIGHT_FORWARDERS,
        locators.PageFooterLocators.INFORMATION_CARRIERS
    ]

    footer_knowledge_base = [
        locators.PageFooterLocators.KNOWLEDGE_BASE_HEADER,
        locators.PageFooterLocators.KNOWLEDGE_BASE_CUSTOMER_COMMUNITY,
        locators.PageFooterLocators.KNOWLEDGE_BASE_XENETA_PLATFORM,
        locators.PageFooterLocators.KNOWLEDGE_BASE_RESOURCES,
        locators.PageFooterLocators.KNOWLEDGE_BASE_PARTNER_DIRECTORY
    ]

    footer_company = [
        locators.PageFooterLocators.COMPANY_HEADER,
        locators.PageFooterLocators.COMPANY_CAREERS,
        locators.PageFooterLocators.COMPANY_NEWS,
        locators.PageFooterLocators.COMPANY_CONTACT_US,
        locators.PageFooterLocators.COMPANY_PRESS_ROOM
    ]

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://www.xeneta.com"

    def open_page(self):
        return self.driver.get(self.base_url)


class CareersPage(BaseXenetaPage):
    sections = [
        locators.CareersPageLocators.JOIN_US_BANNER,
        locators.CareersPageLocators.WHAT_WE_DO_BANNER,
        locators.CareersPageLocators.OUR_VALUES_CONTAINER,
        locators.CareersPageLocators.GLOBAL_TRIBE_CONTAINER,
        locators.CareersPageLocators.OPEN_ROLES_CONTAINER
    ]

    join_us_banner_text = [
        locators.CareersPageLocators.JOIN_US_BANNER_HEADER_REL_XPATH,
        locators.CareersPageLocators.JOIN_US_BANNER_TEXT1_REL_XPATH,
        locators.CareersPageLocators.JOIN_US_BANNER_TEXT2_REL_XPATH,
    ]

    what_we_do_section_text = [
        locators.CareersPageLocators.WHAT_WE_DO_BANNER_HEADER_REL_XPATH,
        locators.CareersPageLocators.WHAT_WE_DO_BANNER_TEXT_REL_XPATH

    ]

    our_values_tab_links = [
        {locators.CareersPageLocators.OUR_VALUES_CONTAINER_TAB_LINK1:
             locators.CareersPageLocators.OUR_VALUES_CONTAINER_TAB_LINK1_TEXT},
        {locators.CareersPageLocators.OUR_VALUES_CONTAINER_TAB_LINK2:
             locators.CareersPageLocators.OUR_VALUES_CONTAINER_TAB_LINK2_TEXT},
        {locators.CareersPageLocators.OUR_VALUES_CONTAINER_TAB_LINK3:
             locators.CareersPageLocators.OUR_VALUES_CONTAINER_TAB_LINK3_TEXT},
        {locators.CareersPageLocators.OUR_VALUES_CONTAINER_TAB_LINK4:
             locators.CareersPageLocators.OUR_VALUES_CONTAINER_TAB_LINK4_TEXT}
    ]

    global_tribe_cards = [
        locators.CareersPageLocators.GLOBAL_TRIBE_OSLO,
        locators.CareersPageLocators.GLOBAL_TRIBE_NEW_YORK,
        locators.CareersPageLocators.GLOBAL_TRIBE_HAMBURG
    ]

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://www.xeneta.com/careers"  # TODO make link concatenation?


class DemoPage(BaseXenetaPage):
    sections = [
        locators.DemoPageLocators.PROCURE_FREIGHT_BANNER,
        locators.DemoPageLocators.LEARN_MORE_CONTAINER
    ]

    learn_more_wrappers = [
        locators.DemoPageLocators.ONE_TO_ONE_DEMO,
        locators.DemoPageLocators.WATCH_VIDEOS,
        locators.DemoPageLocators.GROUP_LIVE_DEMO
    ]

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://www.xeneta.com/demo"  # TODO make link concatenation?
