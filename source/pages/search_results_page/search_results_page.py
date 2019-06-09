from pages.github_page import GithubPage
from services.locator_creators import create_class_locator
from pages.search_results_page.search_results_list import SearchResultsList
from pages.components.pagination import Pagination


class SearchResultsPage(GithubPage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.search_results_list = SearchResultsList(driver, timeout)
        self.pagination = Pagination(driver, timeout)

    def get_results_len(self):
        return self.search_results_list.results_len

    def is_first_page(self):
        return self.pagination.is_first_page()


class SearchResultsPageLocators:
    RESULTS_CONTAINER = create_class_locator("codesearch-results")
    REPO_RESULT = create_class_locator("repo-list-item")
