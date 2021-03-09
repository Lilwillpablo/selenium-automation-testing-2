from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what,
                               timeout=4):  # dont forget to commenting up  self.browser.implicitly_wait(timeout) in __init__
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what,
                       timeout=4):  # dont forget to commenting up  self.browser.implicitly_wait(timeout) in __init__
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def move_to_workshop_page(self):
        self.browser.find_element(By.CSS_SELECTOR, ".NavigationSlice_secondaryWrapper__paGIp .Menu_list-item__1F0Km:nth-of-type(1) .MenuItem_menu-item__link__2qTtx").click()
        self.browser.find_element(By.CSS_SELECTOR, "[data-e2e-name='unlimited_workshops'] > span:nth-of-type(1)").click()
        time.sleep(10)
