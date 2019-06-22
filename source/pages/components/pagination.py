import services.utils as utils
import services.elements as elements
from services.locator_creators import create_class_locator, create_xpath_locator


class Pagination:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.__pagination_el = None
        self.__prev_page_el = None
        self.__next_page_el = None
        self.__current_page_el = None

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

    @property
    def __current_page(self):
        self.__current_page_el = utils.create_element_if_needed(
            self.__current_page_el,
            self.__pagination,
            self.timeout,
            PaginationLocators.CURRENT_PAGE
        )
        return self.__current_page_el

    @property
    def current_page_number(self):
        return int(self.__current_page.text, 10)

    def __nth_child(self, child_num):
        pagination_children_els = utils.find_elements(
            self.__pagination,
            create_xpath_locator(".//*")
        )
        return pagination_children_els[child_num]

    def initialize(self):
        self.__pagination_el = utils.find_element(
            self.driver,
            PaginationLocators.PAGINATION
        )

    def is_first_page(self):
        first_page_el = self.__nth_child(1)
        prev_is_disabled = elements.el_has_class(self.__prev_page, 'disabled')
        first_is_current = elements.el_has_class(first_page_el, 'current')
        return prev_is_disabled and first_is_current

    def click_on_next(self):
        self.__next_page.click()


class PaginationLocators:
    PAGINATION = create_class_locator("pagination")
    PREV_PAGE = create_class_locator("previous_page")
    NEXT_PAGE = create_class_locator("next_page")
    CURRENT_PAGE = create_class_locator("current")
