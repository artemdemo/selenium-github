from pages.github_page import GithubPage
from source.pages.repo_page.repo_page_head import RepoPageHead


class RepoPage(GithubPage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
        self.__head = RepoPageHead(driver, timeout)

    @property
    def title(self):
        return self.__head.title


