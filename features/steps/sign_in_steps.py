from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on Returns and Orders')
def click_returns_and_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()
    sleep(1)


@then("Verify that {expected_result} is shown")
def verify_Sign_In(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]').text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@then('Verify that email input field is present')
def verify_email_field(context):
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'