from selenium.webdriver.common.by import By
from behave import given, when, then
import time

AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.XPATH, '//i[@class="hm-icon nav-sprite"]')
FOOTER_LINKS = (By.CSS_SELECTOR, 'table.navFooterMoreOnAmazon td.navFooterDescItem')
HEADER_LINKS = (By.CSS_SELECTOR, '#nav-xshop a.nav-a[data-csa-c-type="link"]')
BEST_SELLERS = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_bestsellers"]')
CUSTOMER_SERVICE = (By.XPATH, '//a[@data-csa-c-slot-id="nav_cs_3"]')

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Input text {search_word}')
def input_search_word(context, search_word):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)


@when('Click on search button')
def click_search(context):
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click on Best Sellers')
def click_bestsellers(context):
    context.driver.find_element(*BEST_SELLERS).click()


@when('Click on Customer Service')
def click_customer_service(context):
    context.driver.find_element(*CUSTOMER_SERVICE).click()


@then('Verify hamburger menu icon present')
def verify_ham_menu_present(context):
    element = context.driver.find_element(*HAM_MENU)
    print(element)

@then('Verify that footer has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
    print('Original Type: ', type(expected_amount))
    expected_amount = int(expected_amount)
    print('Type after converting: ', type(expected_amount))
    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    print(footer_links)
    print('\nLink count: ', len(footer_links))
    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links but got {len(footer_links)}'


@then('Verify that header has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    print('Original Type: ', type(expected_amount))
    expected_amount = int(expected_amount)
    print('Type after converting: ', type(expected_amount))
    header_links = context.driver.find_elements(*HEADER_LINKS)
    print(header_links)
    print('\nLink count: ', len(header_links))
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links but got {len(header_links)}'

