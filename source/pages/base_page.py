from abc import ABC


class BasePage(ABC):
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    def get_page_title(self):
        return self.driver.title
