# Created by alberthembd at 2/27/24
Feature: Tests for main page UI

  Scenario Outline: Verify header in shown
    Given Open Target main page
    Then Verify header in shown
    Examples:

  Scenario: Verify header has correct amount links
    Given Open Target main page
    Then Verify header has 5 links