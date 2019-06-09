from selenium.webdriver.common.keys import Keys
from services.locator_creators import create_class_locator
import services.utils as utils
from pages.search_results_page.search_results_page import SearchResultsPage


class TopMenu:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.search_input_el = None

    def search_for(self, text):
        self.search_input_el = utils.create_element_if_needed(
            self.search_input_el,
            self.driver,
            self.timeout,
            TopMenuLocators.SEARCH_INPUT,
        )
        self.search_input_el.send_keys(text)
        self.search_input_el.send_keys(Keys.RETURN)
        return SearchResultsPage(self.driver, self.timeout)


class TopMenuLocators:
    SEARCH_INPUT = create_class_locator("header-search-input")
