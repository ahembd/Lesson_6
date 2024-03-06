from selenium.webdriver import Keys


class Page:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        print('in base_page.open')
        self.driver.get(url)

    def find_element(self, *locator):
        print('in base_page.find_element, *locator == ' + str(*locator))
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        print('in base_page.find_elements')
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        print('in base_page.click, locator ==: ', locator)
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        print('in base_page.input_text, locator == ' + str(locator))
        self.driver.find_element(*locator).send_keys(text)
