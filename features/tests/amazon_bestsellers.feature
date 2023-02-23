# Created by lenaa at 2/23/2023
Feature: Amazon Bestsellers tests

  Scenario: User can see header links
    Given Open Amazon page
    When Click on Best Sellers
    Then Verify that bestsellers header has 5 links