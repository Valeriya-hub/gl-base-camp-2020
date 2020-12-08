from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/home/ubuntu/Загрузки/tmp/chromedriver')
driver.get("https://www.google.com/")
elem = driver.find_element_by_xpath(".//input[@name='q' and @type='text']")  
elem.send_keys("selenium install ubuntu python") 
elem.send_keys(Keys.RETURN)  
elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//h3/span[text()='pip install selenium - PyPI']")))
elem.click()
elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN) 
elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//h3/span[text()='amazon-selenium']")))
elem.click()
elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//div/h1")))
assert "amazon-selenium 0.1.2"  in driver.page_source
driver.close()