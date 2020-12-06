from pageObject.BaseApp import BasePage
from pageObject.config.config import Config
from selenium.webdriver.common.by import By

class GLCareersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_site(self):
        BasePage.go_to_site(self)

    def click_on_the_cookies_allow_button(self):
        return self.find_element(Config.LOCATOR_ALLOW_COOKIES_BUTON,time=5).click()
    
    def check_word(self):
        return self.find_element(Config.LOCATOR_FILD_NAME_PROFESSINS)
        
    def enter_word(self, word):
        search_field = self.find_element(Config.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(Config.LOCATOR_SEARCH_BUTON,time=5).click()