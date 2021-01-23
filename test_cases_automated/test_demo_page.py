import pytest

from .page import DemoPage
from selenium.webdriver.common.by import By
from .locators import DemoPageLocators as DemoLocators
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


@pytest.mark.parametrize('wrapper', DemoPage.learn_more_wrappers)
def test_check_image_in_life_demo_wrappers_displayed(demo_page, wrapper):
    assert demo_page.find_element(wrapper).find_element(By.XPATH,
                                                        DemoLocators.BULLET_CIRCLE_SECTION_REL_XPATH
                                                        ).is_displayed()


@pytest.mark.parametrize('wrapper', DemoPage.learn_more_wrappers)
def test_check_header_in_life_demo_wrappers_exists(demo_page, wrapper):
    assert demo_page.find_element(wrapper).find_element(By.XPATH,
                                                        DemoLocators.SECTION_HEADER_REL_XPATH
                                                        ).text != ''


@pytest.mark.parametrize('wrapper', DemoPage.learn_more_wrappers)
def test_check_text_in_life_demo_wrappers_exists(demo_page, wrapper):
    assert demo_page.find_element(wrapper).find_element(By.XPATH,
                                                        DemoLocators.SECTION_TEXT_REL_XPATH
                                                        ).text != ''


@pytest.mark.parametrize('wrapper', DemoPage.learn_more_wrappers)
def test_check_button_in_life_demo_wrappers_exists(demo_page, wrapper):
    assert demo_page.find_element(wrapper).find_element(By.XPATH,
                                                        DemoLocators.SECTION_BUTTON_REL_XPATH
                                                        ).get_attribute('text') != ''


@pytest.mark.parametrize('wrapper', DemoPage.learn_more_wrappers)
def test_check_button_link_in_life_demo_wrappers_exists(demo_page, wrapper):
    link = demo_page.find_element(wrapper).find_element(By.XPATH,
                                                        DemoLocators.SECTION_BUTTON_REL_XPATH).get_attribute('href')

    assert link != ''
    assert get_url_status_code(link) == 200


