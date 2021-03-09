from .base_page import BasePage
from datetime import datetime
from selenium.webdriver.common.by import By


class LocationPage(BasePage):
    def print_todays_hours_of_operation(self):
        weekday_today = datetime.today().isoweekday()
        if weekday_today == 7:
            self.browser.find_element(By.CSS_SELECTOR, ".hours-IVyrp").click()
            Sun = self.browser.find_element(By.CSS_SELECTOR, "div:nth-of-type(1) > .times-fms3v")
            Sun2 = Sun.text
            print(f"Hours of operation: {Sun2}")
        elif weekday_today == 1:
            self.browser.find_element(By.CSS_SELECTOR, ".hours-IVyrp").click()
            Mon = self.browser.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > .times-fms3v")
            Mon2 = Mon.text
            print(f"Hours of operation: {Mon2}")
        elif weekday_today == 2:
            self.browser.find_element(By.CSS_SELECTOR, ".hours-IVyrp").click()
            Tues = self.browser.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > .times-fms3v")
            Tues2 = Tues.text
            print(f"Hours of operation: {Tues2}")
        elif weekday_today == 3:
            self.browser.find_element(By.CSS_SELECTOR, ".hours-IVyrp").click()
            Wen = self.browser.find_element(By.CSS_SELECTOR, "div:nth-of-type(4) > .times-fms3v")
            Wen2 = Wen.text
            print(f"Hours of operation: {Wen2}")
        elif weekday_today == 4:
            self.browser.find_element(By.CSS_SELECTOR, ".hours-IVyrp").click()
            Thur = self.browser.find_element(By.CSS_SELECTOR, "[class='time-35INk']")
            Thur2 = Thur.text
            print(f"Hours of operation: {Thur2}")
        elif weekday_today == 5:
            self.browser.find_element(By.CSS_SELECTOR, ".hours-IVyrp").click()
            Fri = self.browser.find_element(By.CSS_SELECTOR, "div:nth-of-type(6) > .times-fms3v")
            Fri2 = Fri.text
            print(f"Hours of operation: {Fri2}")
        elif weekday_today == 6:
            self.browser.find_element(By.CSS_SELECTOR, ".hours-IVyrp").click()
            Sat = self.browser.find_element(By.CSS_SELECTOR, "div:nth-of-type(7) > .times-fms3v")
            Sat2 = Sat.text
            print(f"Hours of operation: {Sat2}")







