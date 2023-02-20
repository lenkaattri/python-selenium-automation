from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/")

#click on cart icon
driver.find_element(By.XPATH, '//span[@class="nav-cart-icon nav-sprite"]').click()

#check if the cart is empty
number = driver.find_element(By.XPATH, '//span[@class="nav-cart-count nav-cart-0 nav-progressive-attribute nav-progressive-content"]').text
print(number)

#input product into search field
search = driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('365 Everyday Value Organic Peppermint Tea')

#click on search button
driver.find_element(By.ID, 'nav-search-submit-button').click()

#click any product
driver.find_element(By.XPATH, '//span[@class="a-size-base-plus a-color-base a-text-normal"]').click()
time.sleep(59)

#add to cart
driver.find_element(By.ID, '#add-to-cart-button').click()

#check the cart
number = driver.find_element(By.XPATH, '//span[@class="nav-cart-count nav-cart-1 nav-progressive-attribute nav-progressive-content"]').text
print(number)


driver.quit()