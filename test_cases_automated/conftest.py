import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    # this options are needed for avoiding crashes inside docker container
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(chrome_options=chrome_options)
    yield driver
    driver.quit()


