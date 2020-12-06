from pageObject.BaseApp import BasePage
from selenium.webdriver.common.by import By
from pageObject.config.config import Config
from array import *

class GLCareersResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_first_result(self):
        first_result = self.find_element(Config.LOCATOR_FIRST_RESULT)
        return first_result.text