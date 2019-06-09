from configuration import *
# Configuration as python file will be deprecated once there's an automation framework with a better solution
import pytest


@pytest.mark.order1
def test_search_for_js(start_web):
    index_page = start_web
    search_results = index_page.search_for("javascript")
    assert search_results.there_is_results_container(), "Hasn't been redirected to search results"
