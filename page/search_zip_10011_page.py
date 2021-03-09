from .base_page import BasePage
from selenium.webdriver.common.by import By


class Search10011(BasePage):

    def verify_name_title_on_search_page_matches_with_meeting_page_and_print_name_title_distance(self):
        distance = self.browser.find_element(By.CLASS_NAME, "distance-OhP63").text
        search_title1 = self.browser.find_element(By.CSS_SELECTOR, ".address-3-YC0 > div:nth-of-type(1)").text
        search_title2 = self.browser.find_element(By.CSS_SELECTOR, ".address-3-YC0 > div:nth-of-type(2)").text
        print(f"distance= {distance} location= {search_title1}, {search_title2}")
        self.browser.find_element(By.CLASS_NAME, "linkUnderline-1_h4g").click()
        page_title1 = self.browser.find_element(By.CSS_SELECTOR, ".address-2PZwW > div:nth-of-type(1)").text
        page_title2 = self.browser.find_element(By.CSS_SELECTOR, ".address-2PZwW > div:nth-of-type(2)").text
        assert search_title1 == page_title1, ("Not equal")
        assert search_title2 == page_title2, ("Not equal")

