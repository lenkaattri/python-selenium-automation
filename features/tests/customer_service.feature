# Created by lenaa at 2/23/2023
Feature: Amazon Customer Service

  Scenario: User can see rectangles with info
    Given Open Amazon page
    When Click on Customer Service
    Then Verify that page body has 10 rectangles