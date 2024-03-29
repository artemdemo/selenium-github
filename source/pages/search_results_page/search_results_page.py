from pages.github_page import GithubPage
from services.locator_creators import create_class_locator
from pages.search_results_page.search_results_list import SearchResultsList
from pages.search_results_page.search_sort import SearchSort, SortOptions
from pages.components.pagination import Pagination


class SearchResultsPage(GithubPage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.search_results_list = SearchResultsList(driver, timeout)
        self.pagination = Pagination(driver, timeout)
        self.search_sort = SearchSort(self.search_results_list.get_results_el(), timeout)

    @property
    def current_page_number(self):
        return self.pagination.current_page_number

    @property
    def results_len(self):
        return self.search_results_list.results_len

    def get_nth_result(self, result_number):
        return self.search_results_list[result_number]

    def open_nth_result(self, result_number):
        result = self.search_results_list[result_number]
        result.open_repo_page()
        from source.pages.repo_page.repo_page import RepoPage
        return RepoPage(self.driver, self.timeout)

    def is_first_page(self):
        return self.pagination.is_first_page()

    def sort_by_most_stars(self):
        self.search_sort.select_sort_option(SortOptions.MOST_STARS)
        self.wait_to_load()
        return SearchResultsPage(self.driver, self.timeout)

    def get_current_sort_option(self):
        return self.search_sort.get_sort_option()

    def go_to_the_next_page(self):
        self.pagination.click_on_next()
        self.wait_to_load()
        return SearchResultsPage(self.driver, self.timeout)


class SearchResultsPageLocators:
    REPO_RESULT = create_class_locator("repo-list-item")
