from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.'
           'identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&mobileBrowserWeblabTreatment=C&openid.'
           'return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&prevRID=YQNW7KRRSTFC1S03B0Y7&openid.assoc_handle=usflex&openid.'
           'mode=checkid_setup&desktopBrowserWeblabTreatment=C&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.'
           'net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')


#Amazon logo
driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-logo"]')
#Create account
driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]')
#Your name field
driver.find_element(By.ID,'#ap_customer_name')
#Email field
driver.find_element(By.ID, '#ap_email')
#Password field
driver.find_element(By.ID, '#ap_password')
#Re-enter password field
driver.find_element(By.ID, '#ap_password_check')
#Create your Amazon account button
driver.find_element(By.ID, 'continue')
#Conditions of Use
driver.find_element(By.XPATH, '//a[contains(@href, "condition_of_use")]')
#Privacy Notice
driver.find_element(By.XPATH, '//a[contains(@href, "ap_register_notification_privacy_notice")]')
#Sign in
driver.find_element(By.XPATH, '//a[contains(@href, "openid")]')


driver.quit()