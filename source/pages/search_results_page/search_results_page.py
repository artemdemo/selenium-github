from pages.github_page import GithubPage
from services.locator_creators import create_class_locator
import services.utils as utils


class SearchResultsPage(GithubPage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)


class SearchResultsPageLocators:
    pass
