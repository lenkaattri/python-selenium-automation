# Created by lenaa at 2/20/2023
Feature: Amazon search tests

  Scenario Outline: User can search for coffee on Amazon
    Given Open Amazon page
    When Input text <search_word>
    When Click on search button
    Then Verify that text <search_result> is shown
    Examples:
    |search_word   |search_result  |
    |coffee        |"coffee"       |
    |tea           |"tea"          |
    |mug           |"mug"          |



  Scenario: User can search for table on Amazon
    Given Open Amazon page
    When Input text table
    When Click on search button
    Then Verify that text "table" is shown


  Scenario: User  can add a product to the cart
    Given Open Amazon page
    When Input text Litehouse Freeze Dried Mint
    When Click on search button
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)