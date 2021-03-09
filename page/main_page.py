from .base_page import BasePage

text01 = "WW (Weight Watchers): Weight Loss & Wellness Help | WW USA"


class MainPage(BasePage):
    def verify_title_matches_text001(self):
        assert self.browser.title.strip() == text01, ("Wrong title")
