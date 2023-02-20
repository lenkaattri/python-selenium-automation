from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.amazon.com/')

# By CSS, using ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')

# By CSS, using class
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag-lop')
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag-lop')
# multiple classes
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag.icp-nav-flag-us.icp-nav-flag-lop')

# By CSS, using attributes (except ID and Class)
driver.find_element(By.CSS_SELECTOR, 'a[data-csa-c-content-id="nav_cs_bestsellers"]')
driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
# multiple attributes
driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"][tabindex="0"]')

# class + attribute
driver.find_element(By.CSS_SELECTOR, 'a.nav-a[data-csa-c-content-id="nav_cs_bestsellers"]')

# using contains(*=)
driver.find_element(By.CSS_SELECTOR, 'a[href*="?ref_=nav_cs_bestsellers"]')

# the code below is not working, check later

#driver.find_element(By.CSS_SELECTOR, '#legalTextRow a[href*=condition_of_use]')

# CSS, from parent to child
#driver.find_element(By.CSS_SELECTOR, '#legalTextRow a[href*=condition_of_use]')
#driver.find_element(By.CSS_SELECTOR, 'div.a-section #legalTextRow a[href*=condition_of_use]')

# By XPATH backwards (from child to parent)
#driver.find_element(By.XPATH, '//*[./a(@href, "ap_signin_notification_condition_of_use")]')
