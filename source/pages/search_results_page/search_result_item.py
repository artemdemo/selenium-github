import services.utils as utils
import services.elements as elements
from services.locator_creators import create_tag_locator, create_class_locator


class SearchResultItem:
    def __init__(self, search_result_el, timeout):
        self.__search_result_el = search_result_el
        self.__timeout = timeout
        self.__title_el = None
        self.__stars_el = None

    @property
    def __title(self):
        self.__title_el = utils.create_element_if_needed(
            self.__title_el,
            self.__search_result_el,
            self.__timeout,
            SearchResultItemLocators.TITLE,
        )
        return self.__title_el

    @property
    def __stars(self):
        if self.__stars_el is None:
            star_svg_el = utils.find_element(
                self.__search_result_el,
                SearchResultItemLocators.OCTICON_STAR,
            )
            self.__stars_el = elements.get_parent_of_el(star_svg_el)
        return self.__stars_el

    @property
    def title(self):
        return self.__title.text

    @property
    def stars(self):
        return self.__stars.text

    def open_repo_page(self):
        title_link_el = utils.find_element(
            self.__title,
            SearchResultItemLocators.TITLE_LINK,
        )
        title_link_el.click()


class SearchResultItemLocators:
    TITLE = create_tag_locator("h3")
    TITLE_LINK = create_tag_locator("a")
    OCTICON_STAR = create_class_locator("octicon-star")
