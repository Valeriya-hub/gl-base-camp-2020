import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="/home/ubuntu/Загрузки/tmp/chromedriver")
    yield driver
    driver.quit()