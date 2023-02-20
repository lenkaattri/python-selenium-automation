from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")


#2. Practice with locators.
#Create locators + search strategy for these page elements of Amazon Sign in page:

#Amazon logo
driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-logo"]')


#Email field
driver.find_element(By.ID, 'ap_email')


#Continue button
driver.find_element(By.XPATH, '//input[@id="continue"]')


#Need help link
driver.find_element(By.XPATH, '//span[@class="a-expander-prompt"]')


#Forgot your password link
driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-expand"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//a[@id="auth-fpp-link-bottom"]')


#Other issues with Sign-In link
driver.find_element(By.XPATH, '//a[@id="ap-other-signin-issues-link"]')


#Create your Amazon account button
driver.find_element(By.XPATH, '//a[@id="createAccountSubmit"]')


#Conditions of use link
driver.find_element(By.XPATH, '//a[contains(@href, "ap_signin_notification_condition_of_use")]')


#Privacy Notice link
driver.find_element(By.XPATH, '//a[contains(@href, "ap_signin_notification_privacy_notice")]')

#3. Create a test case for the Sign In page using python & selenium script.
#(Make sure to use Incognito browser mode when searching for locators)
#Test Case: Logged out user sees Sign in page when clicking Orders

driver.get('https://www.amazon.com/')
driver.find_element(By.ID, 'nav-orders').click()

expected_text = 'Sign in'
actual_text = driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]').text

assert actual_text == expected_text, 'fExpected {expected_text} but got {actual_text}'

#Verify email field present
assert driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'


driver.quit()
