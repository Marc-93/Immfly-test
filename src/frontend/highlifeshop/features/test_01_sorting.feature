# Created by marcaroca at 19/12/22
Feature: Sorting

  @immfly-1
  Scenario: Sorting options
    Given User navigates to 'product_list' page
    Given User accepts the cookies
    When  User selects sorter selector
    Then  User validates sorting options