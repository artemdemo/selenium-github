import pytest
from selenium import webdriver
from configuration import *
from pages.index_page.index_page import IndexPage
from pages.github_page import GithubPage
import time
from datetime import datetime

timeout = 5
relevant_invocations = {'setup', 'call', 'teardown'}


def initialize_driver(site_url):
    chrome_options = webdriver.ChromeOptions()
    # TODO: While running in DOCKER should be headless
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument(
        '--no-sandbox'  # Required when running as root user. Otherwise you would get no sandbox errors.
    )
    chrome_options.add_argument("--window-size=1024,768")
    chrome_options.add_argument('--ignore-credentials')
    drv = webdriver.Chrome(options=chrome_options,
                           service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    drv.get(site_url)
    return drv


driver = initialize_driver(site_url)


@pytest.fixture(scope='function')
def start_web():
    index_page = IndexPage(driver, timeout)
    yield index_page
    github_page = GithubPage(driver, timeout)
    github_page.go_home()


@pytest.fixture(scope='module')
def manage_driver_and_cleanup():
    yield driver
    try:
        # Here is the place to define garbage collection,
        # after your tests are done.
        pass
    finally:
        driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    if rep.when in relevant_invocations and rep.failed:
        driver.save_screenshot(f"screenshot_{rep.nodeid}_{datetime.fromtimestamp(time.time())}.png".replace(" ", "_"))
    setattr(item, "rep_" + rep.when, rep)
