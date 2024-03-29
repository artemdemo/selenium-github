from services.locator_creators import create_class_locator
import services.utils as utils
from pages.search_results_page.search_result_item import SearchResultItem


class SearchResultsList:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.__results_container_el = None
        self.__results_list = None

    def __getitem__(self, key):
        return self.__results_list[key]

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
    def __results(self):
        if self.__results_list is None:
            self.initialize()
        return self.__results_list

    @property
    def results_len(self):
        return len(self.__results)

    def get_results_el(self):
        return self.__results_container

    def initialize(self):
        result_els = utils.find_elements(
            self.__results_container,
            SearchResultsListLocators.REPO_RESULT
        )
        self.__results_list = [SearchResultItem(result_el, self.timeout) for result_el in result_els]


class SearchResultsListLocators:
    RESULTS_CONTAINER = create_class_locator("codesearch-results")
    REPO_RESULT = create_class_locator("repo-list-item")
