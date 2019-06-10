import services.utils as utils
import services.elements as elements
from services.locator_creators import create_class_locator


class Pagination:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.__pagination_el = None
        self.__prev_page_el = None
        self.__next_page_el = None

    @property
    def __pagination(self):
        if self.__pagination_el is None:
            self.initialize()
        return self.__pagination_el

    @property
    def __prev_page(self):
        self.__prev_page_el = utils.create_element_if_needed(
            self.__prev_page_el,
            self.__pagination,
            self.timeout,
            PaginationLocators.PREV_PAGE
        )
        return self.__prev_page_el

    @property
    def __next_page(self):
        self.__next_page_el = utils.create_element_if_needed(
            self.__next_page_el,
            self.__pagination,
            self.timeout,
            PaginationLocators.NEXT_PAGE
        )
        return self.__next_page_el

    def initialize(self):
        self.__pagination_el = utils.find_element(
            self.driver,
            PaginationLocators.PAGINATION
        )

    def is_first_page(self):
        return elements.el_has_class(self.__prev_page, 'disabled')


class PaginationLocators:
    PAGINATION = create_class_locator("pagination")
    PREV_PAGE = create_class_locator("previous_page")
    NEXT_PAGE = create_class_locator("next_page")
