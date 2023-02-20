# Created by lenaa at 2/20/2023
Feature: Amazon search tests

  Scenario: User can search for coffee on Amazon
    Given Open Amazon page
    When Input text coffee
    When Click on search button
    Then Verify that text "coffee" is shown


  Scenario: User can search for table on Amazon
    Given Open Amazon page
    When Input text table
    When Click on search button
    Then Verify that text "table" is shown