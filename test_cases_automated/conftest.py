import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
    yield driver
    driver.quit()
