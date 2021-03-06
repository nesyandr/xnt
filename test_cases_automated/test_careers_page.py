import pytest
from selenium.webdriver.common.by import By

from .locators import CareersPageLocators
from .page import BaseXenetaPage, CareersPage
from .utils import get_url_status_code


@pytest.fixture(scope="class")
def careers_page(browser):
    return CareersPage(browser)


@pytest.fixture(autouse=True)
def open_page(careers_page):
    careers_page.open_page()


def test_careers_page_address_is_valid(careers_page):
    assert get_url_status_code(careers_page.base_url) == 200


@pytest.mark.parametrize("section", CareersPage.sections)
def test_page_section_present(careers_page, section):
    assert careers_page.find_element(section)


@pytest.mark.parametrize('wrapper', CareersPage.join_us_banner_text)
def test_text_in_learn_more_wrapper_exist(careers_page, wrapper):
    assert careers_page.find_element(CareersPageLocators.JOIN_US_BANNER).find_element(By.XPATH, wrapper).text


@pytest.mark.parametrize('wrapper', CareersPage.what_we_do_section_text)
def test_text_in_what_we_do_wrapper_exist(careers_page, wrapper):
    assert careers_page.find_element(CareersPageLocators.WHAT_WE_DO_BANNER).find_element(By.XPATH, wrapper).text


def test_header_text_in_our_values_wrapper_exist(careers_page):
    assert careers_page.find_element(CareersPageLocators.OUR_VALUES_CONTAINER).find_element(
        By.XPATH, CareersPageLocators.OUR_VALUES_CONTAINER_HEADER_REL_XPATH).text


@pytest.mark.parametrize('tab_link', CareersPage.our_values_tab_links)
def test_tab_link_in_our_values_wrapper_exist(careers_page, tab_link):
    link = next(iter(tab_link.keys()))
    careers_page.find_element(link).click()
    careers_page.find_element(tab_link[link]).is_displayed()
    assert careers_page.find_element(tab_link[link]).text


@pytest.mark.parametrize('card', CareersPage.global_tribe_cards)
def test_text_global_tribe_cards_exist(careers_page, card):
    assert careers_page.find_element(card).text


def test_open_roles_table_is_not_empty(careers_page):
    open_roles = careers_page.find_element(
        CareersPageLocators.OPEN_ROLES_ROW_FLUID).find_elements(
        By.CLASS_NAME,
        CareersPageLocators.OPEN_ROLES_ROW_FLUID_ROWS_CLASS_NAME
    )
    assert open_roles

    for role in open_roles:
        assert role.text


@pytest.mark.parametrize('header_link', BaseXenetaPage.header_links)
def test_header_link_exist(careers_page, header_link):
    assert careers_page.find_element(header_link).is_displayed()


@pytest.mark.parametrize('footer_link', [
    *BaseXenetaPage.footer_social_networks,
    *BaseXenetaPage.footer_information,
    *BaseXenetaPage.footer_knowledge_base,
    *BaseXenetaPage.footer_company,
])
def test_footer_link_exist(careers_page, footer_link):
    assert careers_page.find_element(footer_link).is_displayed()
