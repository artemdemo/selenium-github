from pages.base_page import BasePage


class GithubPage(BasePage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.topMenu = None

    def search_for(self, text):
        if self.topMenu is None:
            from pages.components.top_menu import TopMenu
            self.topMenu = TopMenu(self.driver, self.timeout)
        return self.topMenu.search_for(text)
