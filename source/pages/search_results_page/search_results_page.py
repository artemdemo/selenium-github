import time
from pages.github_page import GithubPage
from services.locator_creators import create_class_locator
from pages.search_results_page.search_results_list import SearchResultsList
from pages.search_results_page.search_sort import SearchSort, SortOptions
from pages.components.pagination import Pagination
import services.utils as utils


class SearchResultsPage(GithubPage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.search_results_list = SearchResultsList(driver, timeout)
        self.pagination = Pagination(driver, timeout)
        self.search_sort = SearchSort(self.search_results_list.get_results_el(), timeout)

    def get_results_len(self):
        return self.search_results_list.results_len

    def is_first_page(self):
        return self.pagination.is_first_page()

    def sort_by_most_stars(self):
        self.search_sort.select_sort_option(SortOptions.MOST_STARS)
        # After selecting an option page will not immediately start to reload.
        # Therefore I'm waiting for 1 second in order to wait to it to kickstart the process.
        time.sleep(1)

        # And here I'm able to start to load for the RESULTS_CONTAINER
        utils.wait_for_element_to_load(self.driver, self.timeout, SearchResultsPageLocators.RESULTS_CONTAINER)
        return SearchResultsPage(self.driver, self.timeout)

    def get_current_sort_option(self):
        return self.search_sort.get_sort_option()

    def go_to_the_next_page(self):
        self.pagination.click_on_next()
        self.wait_to_load()
        # time.sleep(1)
        return SearchResultsPage(self.driver, self.timeout)


class SearchResultsPageLocators:
    RESULTS_CONTAINER = create_class_locator("codesearch-results")
    REPO_RESULT = create_class_locator("repo-list-item")
