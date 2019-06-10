from enum import Enum
import services.utils as utils
from services.locator_creators import create_class_locator, create_tag_locator


class SearchSort:
    def __init__(self, search_sort_el, timeout):
        self.__search_sort_el = search_sort_el
        self.__timeout = timeout
        self.__select_menu_el = None

    @property
    def __select_menu(self):
        if self.__select_menu_el is None:
            self.initialize()
        return self.__select_menu_el

    def initialize(self):
        self.__select_menu_el = utils.find_element(
            self.__search_sort_el,
            SearchSortLocators.SELECT_MENU
        )

    def select_sort_option(self, sort_option):
        self.__select_menu.click()
        option_el = utils.get_first_element_with_text(self.__select_menu,
                                                      self.__timeout,
                                                      SearchSortLocators.SELECT_MENU_ITEM,
                                                      sort_option.value)
        option_el.click()

    def get_sort_option(self):
        summary_el = utils.find_element(
            self.__search_sort_el,
            SearchSortLocators.SELECT_SUMMARY
        )
        name_el = utils.find_element(
            summary_el,
            SearchSortLocators.SELECT_SUMMARY_NAME
        )
        return name_el.text


class SortOptions(Enum):
    BEST_MATCH = "Best match"
    MOST_STARS = "Most stars"
    FEWEST_STARS = "Fewest stars"
    MOST_FORKS = "Most forks"
    FEWEST_FORKS = "Fewest forks"
    RECENTLY_UPDATED = "Recently updated"
    LEAST_RECENTLY_UPDATED = "Least recently updated"


class SearchSortLocators:
    SELECT_MENU = create_class_locator("select-menu")
    SELECT_MENU_ITEM = create_class_locator("select-menu-item")
    SELECT_SUMMARY = create_class_locator("select-menu-button")
    SELECT_SUMMARY_NAME = create_tag_locator("span")
