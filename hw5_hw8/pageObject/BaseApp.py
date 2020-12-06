from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObject.config.config import Config

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = Config.BASE_URL

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Can't find element by locator {locator}")