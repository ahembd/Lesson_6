from selenium.webdriver.common.by import By
from behave import given, when, then

CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
VIEW_CART_BUTTON = (By.XPATH, "//*[@id='addToCartButtonOrTextIdFor12954151']")


@when('Open cart page')
def open_cart(context):
    print("in open_cart")
    context.driver.get('https://www.target.com/cart')


# @when('Confirm Add to Cart button from side navigation')
# def add_to_cart_from_side_navigation(context):
#     print("in add_to_cart")
#     context.driver.find_element(*VIEW_CART_BUTTON)


@then('Very cart has 1 item(s)')
def verify_cart_amount(context):
    print("in verify_cart_amount")


@then('Verify cart has correct product')
def verify_product_name(context):
    print("in verify_product_name")
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print('actual_name == ' + actual_name)
    print('context.product_name == ' + context.product_name)
    # assert context.product_name == actual_name, f"Expected {context.product_name} but got {actual_name}"


@then('Verify cart has correct multiple products')
def verify_product_names(context):
    # Grab title text of every product in the cart and store in actual_names:
    actual_names = [product.text for product in context.driver.find_elements(*CART_ITEM_TITLE)]
    # Sort lists before verification:
    context.product_names.sort()
    actual_names.sort()
    assert context.product_names == actual_names, f'Expected {context.product_names} did not match {actual_names}'


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    print('In verify cart has {amount} item(s), amount == ' + str(amount))
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert amount in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    print('in verify cart is empty')
    actual_text = context.driver.find_element(*CART_HEADER).text
    print('actual_text == ' + actual_text)
    assert 'Your cart is empty' == actual_text, f"Expected 'Your cart is empty' but got {actual_text}"

