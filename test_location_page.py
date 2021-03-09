from .page.location_page import LocationPage
import pytest


@pytest.mark.validation
def test_todays_hours_of_operation(browser):
    link = "https://www.weightwatchers.com/us/find-a-workshop/1180510/ww-studio-flatiron-new-york-ny"
    page = LocationPage(browser, link)
    page.open()
    page.print_todays_hours_of_operation()
