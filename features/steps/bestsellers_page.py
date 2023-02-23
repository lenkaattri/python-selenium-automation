from selenium.webdriver.common.by import By
from behave import given, when, then
import time

BESTSELLERS_HEADER_LINKS = (By.XPATH, '//*[contains(@id, "CardInstance")]/div/ul/li/div')


@then('Verify that bestsellers header has {expected_amount} links')
def verify_bestsellers_header_link_count(context, expected_amount):
    print('Original Type: ', type(expected_amount))
    expected_amount = int(expected_amount)
    print('Type after converting: ', type(expected_amount))
    bestsellers_header_links = context.driver.find_elements(*BESTSELLERS_HEADER_LINKS)
    print(bestsellers_header_links)
    print('\nLink count: ', len(bestsellers_header_links))
    assert len(bestsellers_header_links) == expected_amount, f'Expected {expected_amount} links but got {len(bestsellers_header_links)}'