from features.pages.base_page import Page
from features.pages.header import Header
from features.pages.main_page import MainPage
from features.pages.search_results_page import SearchResultsPage

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)