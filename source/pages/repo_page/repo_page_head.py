from services.locator_creators import create_class_locator, create_tag_locator
import source.services.utils as utils


class RepoPageHead:
    def __init__(self, driver, timeout):
        self.__driver = driver
        self.__timeout = timeout
        self.__title_el = None
        self.__head_el = utils.create_element_if_needed(
            self.__title_el,
            self.__driver,
            self.__timeout,
            RepoPageHeadLocators.REPOHEAD,
        )

    @property
    def title(self):
        self.__title_el = utils.create_element_if_needed(
            self.__title_el,
            self.__driver,
            self.__timeout,
            RepoPageHeadLocators.TITLE,
        )
        return self.__title_el.text


class RepoPageHeadLocators:
    REPOHEAD = create_class_locator("repohead-details-container")
    TITLE = create_tag_locator("h1")
