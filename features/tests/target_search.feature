# Created by alberthembd at 2/27/24
# Created by svetlanalevinsohn at 1/27/24
Feature: Target.com search tests

  Scenario Outline: User can search for boys clothes on target
    Given Open Target main page
    When Search for boys clothes
    Then Search results for boys clothes are shown
    Then Page URL has search term <expected_part_url>
    Examples:
      | product      | expected_result | expected_part_url |
      | boys clothes | boys clothes    | boys+clothes      |

  Scenario Outline: User can search for coffee on target
    Given Open Target main page
    When Search for coffee
    Then Search results for <expected_result> are shown
    Then Page URL has search term <expected_part_url>
    Examples:
      | product | expected_result | expected_part_url |
      | coffee  | coffee          | coffee            |


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