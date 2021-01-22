import requests
import pytest

from .page import DemoPage


@pytest.fixture(scope="class")
def demo_page(browser):
    return DemoPage(browser)


@pytest.fixture(autouse=True)
def open_page(demo_page):
    demo_page.open_page()


def test_demo_page_address_is_valid(demo_page):
    try:
        r = requests.get(demo_page.base_url).status_code
    except Exception:
        pytest.fail(f"URL {demo_page.base_url} can't  be opened")

    assert r.status_code == 200


@pytest.mark.parametrize("section", DemoPage.sections)
def test_page_section_present(demo_page, section):
    assert demo_page.find_element(section)


