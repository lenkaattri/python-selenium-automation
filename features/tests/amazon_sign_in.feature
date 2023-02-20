# Created by lenaa at 2/20/2023
Feature: Amazon Sign In tests
  Scenario: User can see Sign In header and email input field
    Given Open Amazon page
    When Click on Returns and Orders
    Then Verify that Sign in is shown
    Then Verify that email input field is present
