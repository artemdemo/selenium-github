from pages.github_page import GithubPage
from services.locator_creators import create_class_locator
from pages.search_results_page.search_results_list import SearchResultsList


class SearchResultsPage(GithubPage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.search_results_list = SearchResultsList(driver, timeout)

    def get_results_len(self):
        return self.search_results_list.results_len


class SearchResultsPageLocators:
    RESULTS_CONTAINER = create_class_locator("codesearch-results")
    REPO_RESULT = create_class_locator("repo-list-item")
