from pages.base_page import BasePage
from services.locator_creators import create_class_locator
import services.utils as utils


class SearchResultsPage(BasePage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)


class SearchResultsPageLocators:
    pass
