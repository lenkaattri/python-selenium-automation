from selenium.webdriver.common.by import By
from behave import given, when, then
import time

CUSTOMER_SERVICE_RECTANGLES = (By.XPATH, '//div[@class="issue-card-wrapper"]')


@then('Verify that page body has {expected_amount} rectangles')
def verify_bestsellers_header_link_count(context, expected_amount):
    print('Original Type: ', type(expected_amount))
    expected_amount = int(expected_amount)
    print('Type after converting: ', type(expected_amount))
    customer_service_rectangles = context.driver.find_elements(*CUSTOMER_SERVICE_RECTANGLES)
    print(customer_service_rectangles)
    print('\nLink count: ', len(customer_service_rectangles))
    assert len(customer_service_rectangles) == expected_amount, f'Expected {expected_amount} links but got {len(customer_service_rectangles)}'