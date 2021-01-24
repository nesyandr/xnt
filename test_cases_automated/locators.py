from selenium.webdriver.common.by import By


class DemoPageLocators(object):
    PROCURE_FREIGHT_BANNER = (By.ID, 'hs_cos_wrapper_module_1582720267661699')
    BANNER_CONTENT = (By.XPATH, '//*[@id="hs_cos_wrapper_module_1582720267661699"]/div/div/div/div/div/div[1]/h1/span')

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
    JOIN_US_BANNER_HEADER_REL_XPATH = './/div/div/div/div/div/h2'
    JOIN_US_BANNER_TEXT1_REL_XPATH = './/div/div/div/div/div/p[1]'
    JOIN_US_BANNER_TEXT2_REL_XPATH = './/div/div/div/div/div/p[2]/span'

    WHAT_WE_DO_BANNER = (By.ID, 'hs_cos_wrapper_module_1585244627489364')
    WHAT_WE_DO_BANNER_HEADER_REL_XPATH = './/div/div/div/div/div/div/div[2]/div[1]/h2'
    WHAT_WE_DO_BANNER_TEXT_REL_XPATH = './/div/div/div/div/div/div/div[2]/ul'

    OUR_VALUES_CONTAINER = (By.ID, 'hs_cos_wrapper_widget_27351556888')
    OUR_VALUES_CONTAINER_HEADER_REL_XPATH = './/div/div/div/div[1]'
    OUR_VALUES_CONTAINER_TAB_LINK1 = (By.XPATH,
                                      "//div[ @ id = 'hs_cos_wrapper_widget_27351556886']/div/div/div/ul/li[1]")
    OUR_VALUES_CONTAINER_TAB_LINK1_TEXT = (By.XPATH, '//*[ @ id = "Xenetaisone-1"]/div/div/div[2]')
    OUR_VALUES_CONTAINER_TAB_LINK2 = (By.XPATH,
                                      "//div[ @ id = 'hs_cos_wrapper_widget_27351556886']/div/div/div/ul/li[2]")
    OUR_VALUES_CONTAINER_TAB_LINK2_TEXT = (By.XPATH, '//*[ @ id = "Modernizationthroughdata-2"]/div/div/div[2]')
    OUR_VALUES_CONTAINER_TAB_LINK3 = (By.XPATH,
                                      "//div[ @ id = 'hs_cos_wrapper_widget_27351556886']/div/div/div/ul/li[3]")
    OUR_VALUES_CONTAINER_TAB_LINK3_TEXT = (By.XPATH, '//*[ @ id = "VarietyandFairness-3"]/div/div/div[2]')
    OUR_VALUES_CONTAINER_TAB_LINK4 = (By.XPATH,
                                      "//div[ @ id = 'hs_cos_wrapper_widget_27351556886']/div/div/div/ul/li[4]")
    OUR_VALUES_CONTAINER_TAB_LINK4_TEXT = (By.XPATH, '//*[ @ id = "TransparencybuildsTrust-4"]/div/div/div[2]]')

    GLOBAL_TRIBE_CONTAINER = (By.ID, 'hs_cos_wrapper_widget_27351556882')
    GLOBAL_TRIBE_OSLO = (By.XPATH, '//*[ @ id = "slick-slide00"]/div/div')
    GLOBAL_TRIBE_NEW_YORK = (By.XPATH, '//*[ @ id = "slick-slide01"]/div/div')
    GLOBAL_TRIBE_HAMBURG = (By.XPATH, '//*[ @ id = "slick-slide02"]/div/div')

    OPEN_ROLES_CONTAINER = (By.ID, 'hs_cos_wrapper_widget_27351556886')
    OPEN_ROLES_ROW_FLUID = (By.ID, "hs_cos_wrapper_widget_27351556888")
    OPEN_ROLES_ROW_FLUID_ROWS_CLASS_NAME = "accordion_group"
