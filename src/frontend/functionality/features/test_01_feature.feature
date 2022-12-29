# Created by marcaroca at 19/12/22
Feature: Feature

  @qase-id
  Scenario Outline: Test
    Given Preconditions
    Given User action <action>
    Then  User validations
    Examples:
      | action |
      | 1      |
      | 2      |
