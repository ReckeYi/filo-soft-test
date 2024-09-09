
def test_google_search(google_page):
    google_page.open_page()
    google_page.accept_cookies()
    google_page.search_phrase()
    assert google_page.check_search_results

