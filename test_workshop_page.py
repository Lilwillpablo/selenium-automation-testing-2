from .page.workshop_page import WorkShop
import pytest


@pytest.mark.xfail
def test_title_matches_text002(browser):
    link = "https://www.weightwatchers.com/us/find-a-workshop/"
    page = WorkShop(browser, link)
    page.open()
    page.verify_title_matches_text002()


@pytest.mark.functional
def test_find_meeting(browser):
    link = "https://www.weightwatchers.com/us/find-a-workshop/"
    page = WorkShop(browser, link)
    page.open()
    page.find_meeting_by_zip_code()
