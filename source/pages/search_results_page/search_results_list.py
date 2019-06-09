from services.locator_creators import create_class_locator
import services.utils as utils
from pages.search_results_page.search_result_item import SearchResultItem


class SearchResultsList:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.__results_container_el = None
        self.__results = None
        self.initialize_results()

    @property
    def __results_container(self):
        self.__results_container_el = utils.create_element_if_needed(
            self.__results_container_el,
            self.driver,
            self.timeout,
            SearchResultsListLocators.RESULTS_CONTAINER
        )
        return self.__results_container_el

    @property
    def results_len(self):
        if self.__results is not None:
            return len(self.__results)
        return None

    def initialize_results(self):
        result_els = utils.find_elements(
            self.__results_container,
            SearchResultsListLocators.REPO_RESULT
        )
        if result_els is not None:
            self.__results = [SearchResultItem(result_el, self.timeout) for result_el in result_els]


class SearchResultsListLocators:
    RESULTS_CONTAINER = create_class_locator("codesearch-results")
    REPO_RESULT = create_class_locator("repo-list-item")
