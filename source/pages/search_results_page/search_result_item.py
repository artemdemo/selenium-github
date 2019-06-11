import services.utils as utils
from services.locator_creators import create_tag_locator


class SearchResultItem:
    def __init__(self, search_result_el, timeout):
        self.__search_result_el = search_result_el
        self.__timeout = timeout
        self.__title_el = None

    def get_title(self):
        self.__title_el = utils.create_element_if_needed(
            self.__title_el,
            self.__search_result_el,
            self.__timeout,
            SearchResultItemLocators.TITLE,
        )
        return self.__title_el.text


class SearchResultItemLocators:
    TITLE = create_tag_locator("h3")
