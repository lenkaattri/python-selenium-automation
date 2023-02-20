from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service('C:/Users/lenaa/Automation/python-selenium-automation/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.amazon.com/")
driver.find_element(By.ID, 'nav-orders').click()

expected_text = 'Sign in'

actual_text = driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]').text
time.sleep(5)

assert actual_text == expected_text, 'fExpected {expected_text} but got {actual_text}'

#Verify email field present
assert driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'


driver.quit()


