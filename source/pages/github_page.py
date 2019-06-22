from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from services.locator_creators import create_class_locator
from services.custom_conditions import element_has_css_class, element_has_no_css_class


class GithubPage(BasePage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.topMenu = None

    def search_for(self, text):
        if self.topMenu is None:
            from pages.components.top_menu import TopMenu
            self.topMenu = TopMenu(self.driver, self.timeout)
        return self.topMenu.search_for(text)

    def wait_to_load(self):
        WebDriverWait(self.driver, self.timeout).until(
            element_has_css_class(GithubPageLocators.LOADER_BAR, "is-loading")
        )
        WebDriverWait(self.driver, self.timeout).until(
            element_has_no_css_class(GithubPageLocators.LOADER_BAR, "is-loading")
        )


class GithubPageLocators:
    LOADER_BAR = create_class_locator("pjax-loader-bar")
