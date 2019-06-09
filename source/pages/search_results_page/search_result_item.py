import services.utils as utils
from services.locator_creators import create_tag_locator


class SearchResultItem:
    def __init__(self, search_result_el, timeout):
        self.search_result_el = search_result_el
        self.timeout = timeout
        self.title_el = None

    def get_title(self):
        self.title_el = utils.create_element_if_needed(
            self.title_el,
            self.search_result_el,
            self.timeout,
            SearchResultItemLocators.TITLE,
        )
        if self.title_el is not None:
            return self.title_el.text
        return None


class SearchResultItemLocators:
    TITLE = create_tag_locator("h3")
