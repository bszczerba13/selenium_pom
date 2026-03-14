from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from time import sleep

class Locators:
    FIRST_NAME = (By.ID, "customer_firstname")

class CreateAccountPage(BasePage):
    def choose_gender(self, gender):
        pass
    def enter_firstname(self, firstname):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(firstname)

    def _verify_page(self):
        sleep(3)