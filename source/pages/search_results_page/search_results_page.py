from pages.github_page import GithubPage
from services.locator_creators import create_class_locator
import services.utils as utils


class SearchResultsPage(GithubPage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)

    def there_is_results_container(self):
        element = utils.find_element(self.driver, SearchResultsPageLocators.RESULTS_CONTAINER)
        return element is not None


class SearchResultsPageLocators:
    RESULTS_CONTAINER = create_class_locator("codesearch-results")
