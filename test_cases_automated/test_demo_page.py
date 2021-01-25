import time

import pytest
from selenium.webdriver.common.by import By

from .locators import DemoPageLocators
from .page import BaseXenetaPage, DemoPage
from .utils import get_url_status_code


@pytest.fixture(scope="class")
def demo_page(browser):
    return DemoPage(browser)


@pytest.fixture(autouse=True)
def open_page(demo_page):
    demo_page.open_page()


def test_demo_page_address_is_valid(demo_page):
    assert get_url_status_code(demo_page.base_url) == 200


@pytest.mark.parametrize('section', DemoPage.sections)
def test_demo_page_section_present(demo_page, section):
    assert demo_page.find_element(section)


def test_procure_freight_content_exists(demo_page):
    assert demo_page.find_element(DemoPageLocators.BANNER_CONTENT).text


@pytest.mark.parametrize('wrapper', DemoPage.learn_more_wrappers)
def test_image_in_life_demo_wrappers_displayed(demo_page, wrapper):
    assert demo_page.find_element(wrapper).find_element(By.XPATH,
                                                        DemoPageLocators.SECTION_BULLET_CIRCLE_REL_XPATH
                                                        ).is_displayed()


@pytest.mark.parametrize('wrapper', DemoPage.learn_more_wrappers)
def test_header_in_life_demo_wrappers_exists(demo_page, wrapper):
    assert demo_page.find_element(wrapper).find_element(By.XPATH,
                                                        DemoPageLocators.SECTION_HEADER_REL_XPATH
                                                        ).text


@pytest.mark.parametrize('wrapper', DemoPage.learn_more_wrappers)
def test_text_in_life_demo_wrappers_exists(demo_page, wrapper):
    assert demo_page.find_element(wrapper).find_element(By.XPATH,
                                                        DemoPageLocators.SECTION_TEXT_REL_XPATH
                                                        ).text


@pytest.mark.parametrize('wrapper', DemoPage.learn_more_wrappers)
def test_button_in_life_demo_wrappers_exists(demo_page, wrapper):
    assert demo_page.find_element(wrapper).find_element(By.XPATH,
                                                        DemoPageLocators.SECTION_BUTTON_REL_XPATH
                                                        ).get_attribute('text')


@pytest.mark.parametrize('wrapper', DemoPage.learn_more_wrappers)
def test_button_link_in_life_demo_wrappers_valid(browser, demo_page, wrapper):
    wrapper = demo_page.find_element(wrapper).find_element(By.XPATH,
                                                           DemoPageLocators.SECTION_BUTTON_REL_XPATH)
    wrapper.is_displayed()
    # TODO add a better way to wait until element attribute's state change
    time.sleep(0.5)
    assert wrapper.get_attribute('href')
    assert get_url_status_code(wrapper.get_attribute('href')) == 200


@pytest.mark.parametrize('header_link', BaseXenetaPage.header_links)
def test_header_link_exist(demo_page, header_link):
    assert demo_page.find_element(header_link).is_displayed()


@pytest.mark.parametrize('footer_link', [
    *BaseXenetaPage.footer_social_networks,
    *BaseXenetaPage.footer_information,
    *BaseXenetaPage.footer_knowledge_base,
    *BaseXenetaPage.footer_company,
])
def test_footer_link_exist(demo_page, footer_link):
    assert demo_page.find_element(footer_link).is_displayed()
