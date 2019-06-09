from pages.github_page import GithubPage


class IndexPage(GithubPage):
    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)
