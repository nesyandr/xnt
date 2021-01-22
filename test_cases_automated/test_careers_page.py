import requests
import pytest

from .page import CareersPage


@pytest.fixture(scope="class")
def careers_page(browser):
    return CareersPage(browser)


@pytest.fixture(autouse=True)
def open_page(careers_page):
    careers_page.open_page()


@pytest.fixture(params=careers_page.sectionsA)
def section(request):
    return request.param


def test_careers_page_address_is_valid(careers_page):
    r = requests.get(careers_page.base_url).status_code
    try:
        assert r == 200
    except AssertionError:
        pytest.fail(f"URL {careers_page.base_url} couldn't be opened; Status code {r}")


def test_page_section_present(careers_page, section):
    assert careers_page.find_element(section)


