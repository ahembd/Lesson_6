from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self):
        self.input_text('coffee', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)





class MainPage(Page):

    def open_main(self):
        self.open('https://www.target.com/')