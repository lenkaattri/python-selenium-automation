Feature: Amazon cart tests
  Scenario: User can see empty cart
    Given Open Amazon page
    When Click on cart icon
    Then Verify that Your Amazon Cart is empty is visible