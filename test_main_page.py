from .page.main_page import MainPage
import pytest


@pytest.mark.xfail
def test_title_matches_text001(browser):
    link = "https://www.weightwatchers.com/us/"
    page = MainPage(browser, link)
    page.open()
    page.verify_title_matches_text001()


@pytest.mark.functional
def test_move_to_workshop_page(browser):
    link = "https://www.weightwatchers.com/us/"
    page = MainPage(browser, link)
    page.open()
    page.move_to_workshop_page()



