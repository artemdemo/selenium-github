from configuration import *
# Configuration as python file will be deprecated once there's an automation framework with a better solution
import pytest


@pytest.mark.order1
def test_search(start_web):
    index_page = start_web
    search_results = index_page.search_for("javascript")
    assert True, 'ok'
