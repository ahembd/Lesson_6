from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Google page')
def open_google(context):
    print("Opening Google page")
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    print('product search.inputsearch')
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    print('click on search icon')
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'


@given("Open target product A-88063497 page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given Open target product A-88063497 page')


@then("Verify user can click through colors")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Verify user can click  through colors')


@then("Page URL has search term coffee")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Page URL has search term coffee')


@then("Page URL has search term coffee+mug")
def step_impl(context):
     """
     :type context: behave.runner.Context
     """
     raise NotImplementedError(u'STEP: Then Page URL has search term coffee+mug')

