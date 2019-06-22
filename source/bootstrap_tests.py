

def test_search_for_js(start_web, manage_driver_and_cleanup):
    index_page = start_web
    search_results = index_page.search_for("javascript")
    assert search_results.results_len is not None,\
        "Hasn't been redirected to search results"
    assert search_results.results_len == 10, \
        "Should be shown 10 results (in the first page)"
    assert search_results.is_first_page() is True,\
        "Should be the first page"

    search_results = search_results.sort_by_most_stars()
    assert search_results.get_current_sort_option() == "Most stars",\
        "Results should be sorted by `Most stars`"

    search_results = search_results.go_to_the_next_page()
    assert search_results.is_first_page() is False, \
        "Shouldn't be the first page"
    assert search_results.results_len == 10, \
        "Should be shown 10 results"
    assert search_results.current_page_number == 2, \
        "Should be page number 2"


def test_search_for_vuejs(start_web, manage_driver_and_cleanup):
    index_page = start_web
    search_results = index_page.search_for("javascript vuejs/vue")

    assert search_results.results_len == 10, \
        "Should be shown 10 results"

    first_result = search_results.get_nth_result(0)
    assert first_result.title == "vuejs/vue", \
        "First result title should be `vuejs/vue`"
