import pytest


@pytest.mark.order1
def test_search_for_js(start_web):
    index_page = start_web
    search_results = index_page.search_for("javascript")
    assert search_results.get_results_len() is not None,\
        "Hasn't been redirected to search results"
    assert search_results.get_results_len() == 10,\
        "Should be shown 10 results (in the first page)"
    assert search_results.is_first_page() is True,\
        "Should be the first page"
