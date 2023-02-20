from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, '//span[@class="nav-cart-icon nav-sprite"]').click()
    sleep(1)


@then("Verify that {expected_result} is visible")
def verify_Sign_In(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, '//div[@class="a-row sc-your-amazon-cart-is-empty"]').text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

