from selenium.webdriver.common.by import By

class Config():
    BASE_URL = "https://www.globallogic.com/ua/careers/"
    
    LOCATOR_ALLOW_COOKIES_BUTON = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    LOCATOR_FILD_NAME_PROFESSINS = (By.XPATH, ".//span[text()='Інженерів']")
    LOCATOR_SEARCH_FIELD = (By.XPATH, ".//section[@id='hero']/div/div/div/div/div/div/div/form/div/div/input[@id='by_keyword']")
    LOCATOR_SEARCH_BUTON = (By.XPATH, ".//section[1]/div/div/div/div/div/div/div/form/div/button")
    LOCATOR_FIRST_RESULT = (By.XPATH, ".//div/div[2]/a/div/div/div[1]/p[1]")

    DATA_FOR_ENTER_WORLD = "QA"
    DATA_FOR_CHECK_WORDS = "Jobs Found"