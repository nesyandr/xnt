import requests
import pytest

from .page import DemoPage


def test_demo_page_address_is_valid(browser):
    r = requests.get(DemoPage(browser).base_url).status_code
    try:
        assert r == 200
    except AssertionError:
        pytest.fail(f"URL {DemoPage(browser).base_url} couldn't be opened; Status code {r}")


