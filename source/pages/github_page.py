from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from services.locator_creators import create_class_locator
from services.custom_conditions import element_has_css_class, element_has_no_css_class


class GithubPage(BasePage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.__top_menu_instance = None

    @property
    def __top_menu(self):
        if self.__top_menu_instance is None:
            from pages.components.top_menu import TopMenu
            self.__top_menu_instance = TopMenu(self.driver, self.timeout)
        return self.__top_menu_instance

    def search_for(self, text):
        return self.__top_menu.search_for(text)

    def wait_to_load(self):
        WebDriverWait(self.driver, self.timeout).until(
            element_has_css_class(GithubPageLocators.LOADER_BAR, "is-loading")
        )
        WebDriverWait(self.driver, self.timeout).until(
            element_has_no_css_class(GithubPageLocators.LOADER_BAR, "is-loading")
        )


class GithubPageLocators:
    LOADER_BAR = create_class_locator("pjax-loader-bar")
