from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/home/ubuntu/Загрузки/tmp/chromedriver')
driver.get("https://www.globallogic.com/ua/careers/") 

elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")))
elem.click()
elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//span[text()='Інженерів']")))
elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//section[@id='hero']/div/div/div/div/div/div/div/form/div/div/input[@id='by_keyword']")))
elem.send_keys("QA")
elem.send_keys(Keys.RETURN) 
elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//p[text()='QA Automation engineer IRC104770']")))#print to console header of first result"

print("QA Automation engineer IRC104770")
driver.close()