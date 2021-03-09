from .base_page import BasePage
from selenium.webdriver.common.by import By

text02 = "Find WW Studios & Meetings Near You | WW USA"


class WorkShop(BasePage):
    def verify_title_matches_text002(self):
        assert self.browser.title.strip() == text02, ("Wrong title")

    def find_meeting_by_zip_code(self):
        self.browser.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > .toggleButton-2ikVW").click()
        input_zip = self.browser.find_element(By.ID, "location-search")
        input_zip.send_keys("10011")
        self.browser.find_element(By.ID, "location-search-cta").click()



