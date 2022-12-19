# Created by marcaroca at 19/12/22
Feature: Sorting

  @immfly-1
  Scenario Outline: Sorting options
    Given User navigates to 'product_list' page
    Given User accepts the cookies
    When  User selects '<value>' sort option
    Then  User validates '<value>' sort option is selected
    Examples:
      | value    |
      | position |
      | name     |
      | price    |
      | new      |

  @immfly-2
  Scenario: Default value
    Given User navigates to 'product_list' page
    When  User accepts the cookies
    Then  User validates 'position' sort option is selected

  @immfly-3
  Scenario: Sorting by position
    Given User navigates to 'product_list' page
    Given User accepts the cookies
    When  User selects 'position' sort option
    Then  User validates url contains the expected sorting 'position'

  @immfly-4
  Scenario: Sorting by name
    Given User navigates to 'product_list' page
    Given User accepts the cookies
    When  User selects 'name' sort option
    Then  User validates url contains the expected sorting 'name'

  @immfly-5
  Scenario: Sorting by price
    Given User navigates to 'product_list' page
    Given User accepts the cookies
    When  User selects 'price' sort option
    Then  User validates url contains the expected sorting 'price'

  @immfly-6
  Scenario: Sorting by new arrival
    Given User navigates to 'product_list' page
    Given User accepts the cookies
    When  User selects 'new' sort option
    Then  User validates url contains the expected sorting 'new'
