# Created by alberthembd at 2/27/24
# Created by svetlanalevinsohn at 1/27/24
Feature: Target.com search tests


  Scenario: User can search for clothes boys 1 on target
    Given Open Target main page
    When Search for clothes boys 1
    Then Search results for clothes boys 1 are shown
    Then Page URL has search term clothes boys 1


  Scenario: User can search for coffee on target
    Given Open Target main page
    When Search for coffee
    Then Search results for coffee are shown
    Then Page URL has search coffee


#  Scenario Outline: User can search for a product on target
#    Given Open Target main page
#    When Search for <search_word>
#    Then Search results for <expected_result> are shown
#    Then Page URL has search term <expected_part_url>
#    Examples:
#    |search_word    |expected_result    |expected_part_url    |
#    |coffee mug     |coffee mug         |coffee+mug           |
#    |coffee         |coffee             |coffee               |
#    |tea            |tea                |tea                  |


  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image