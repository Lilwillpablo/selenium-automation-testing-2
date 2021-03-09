from .page.search_zip_10011_page import Search10011
import pytest


@pytest.mark.validation
def test_name_title_on_search_page_matches_with_meeting_page_and_print(browser):
    link = "https://www.weightwatchers.com/us/find-a-workshop/search?search=10011"
    page = Search10011(browser, link)
    page.open()
    page.verify_name_title_on_search_page_matches_with_meeting_page_and_print_name_title_distance()