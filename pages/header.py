from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self, search_input):
        print('in context.header.search_product')
        self.input_text(search_input, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)