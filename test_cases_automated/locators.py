from selenium.webdriver.common.by import By


class DemoPageLocators(object):
    PROCURE_FREIGHT_BANNER = (By.ID, 'hs_cos_wrapper_module_1582720267661699')
    LEARN_MORE_CONTAINER = (By.ID, 'hs_cos_wrapper_module_1599651356652287')
    ONE_TO_ONE_DEMO = (By.XPATH, '//*[@id="hs_cos_wrapper_module_1599651356652287"]/div/div/div/div/div/span/div[1]')
    WATCH_VIDEOS = (By.XPATH, '//*[@id="hs_cos_wrapper_module_1599651356652287"]/div/div/div/div/div/span/div[2]')
    GROUP_LIVE_DEMO = (By.XPATH, '//*[@id="hs_cos_wrapper_module_1599651356652287"]/div/div/div/div/div/span/div[3]')
    SECTION_BULLET_CIRCLE_REL_XPATH = './/div/a/div'
    SECTION_HEADER_REL_XPATH = './/div/div/h3'
    SECTION_TEXT_REL_XPATH = './/div/div/p/span[1]'
    SECTION_BUTTON_REL_XPATH = './/div/div/div/a'

class CareersPageLocators(object):
    JOIN_US_BANNER = (By.ID, 'hs_cos_wrapper_module_158709745267770')
    WHAT_WE_DO_BANNER = (By.ID, 'hs_cos_wrapper_module_1585244627489364')
    OUR_VALUES_CONTAINER = (By.ID, 'hs_cos_wrapper_widget_27351556888')
    GLOBAL_TRIBE_CONTAINER = (By.ID, 'hs_cos_wrapper_widget_27351556882')
    OPEN_ROLES_CONTAINER = (By.ID, 'hs_cos_wrapper_widget_27351556886')
