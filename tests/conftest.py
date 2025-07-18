import pytest
from selenium import webdriver

from curl import *

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(home_page)
    yield driver
    driver.quit()
