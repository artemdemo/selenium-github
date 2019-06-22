from selenium.webdriver.common.keys import Keys
from services.locator_creators import create_class_locator, create_xpath_locator
import services.utils as utils
from pages.search_results_page.search_results_page import SearchResultsPage


class TopMenu:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.__header_el = None
        self.__search_input_el = None
        self.__home_link_el = None

    @property
    def __header(self):
        if self.__header_el is None:
            try:
                self.__header_el = utils.find_element(self.driver, TopMenuLocators.HEADER)
            except:
                self.__header_el = utils.find_element(self.driver, TopMenuLocators.HEADER_OLD)
        return self.__header_el

    def go_home(self):
        self.__home_link_el = utils.create_element_if_needed(
            self.__home_link_el,
            self.__header,
            self.timeout,
            TopMenuLocators.HOME_LINK,
        )
        self.__home_link_el.click()

    def search_for(self, text):
        self.__search_input_el = utils.create_element_if_needed(
            self.__search_input_el,
            self.__header,
            self.timeout,
            TopMenuLocators.SEARCH_INPUT,
        )
        self.__search_input_el.clear()
        self.__search_input_el.send_keys(text)
        self.__search_input_el.send_keys(Keys.RETURN)
        return SearchResultsPage(self.driver, self.timeout)


class TopMenuLocators:
    SEARCH_INPUT = create_class_locator("header-search-input")
    HEADER = create_class_locator("Header")
    HEADER_OLD = create_class_locator("Header-old")
    HOME_LINK = create_xpath_locator("//a[@aria-label='Homepage']")
