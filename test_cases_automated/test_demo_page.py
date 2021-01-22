import requests
import pytest

from .locators import DemoPageLocators as DemoLocators
from .page import DemoPage


@pytest.fixture(scope="class")
def demo_page(browser):
    return DemoPage(browser)


@pytest.fixture(autouse=True)
def open_page(demo_page):
    demo_page.open_page()


@pytest.fixture(
                params=[DemoLocators.PROCURE_FREIGHT_BANNER,
                        DemoLocators.LEARN_MORE_CONTAINER])
def section(request):
    return request.param


def test_demo_page_address_is_valid(demo_page):
    r = requests.get(demo_page.base_url).status_code
    try:
        assert r == 200
    except AssertionError:
        pytest.fail(f"URL {demo_page.base_url} couldn't be opened; Status code {r}")


def test_page_section_present(demo_page, section):
    assert demo_page.find_element(section)


