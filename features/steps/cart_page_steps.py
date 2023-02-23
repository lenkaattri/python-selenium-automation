from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.CSS_SELECTOR, 'sc-active-cart li')


@when('Open cart page')
def click_cart_icon(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')



@then("Verify cart has {expected_count} item(s)")
def verify_Sign_In(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count} but got actual {actual_text}'

