from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from utils.custom_types import Gender

class Locators:
    FIRST_NAME = (By.ID, "customer_firstname")
    GENDER_MALE = (By.XPATH, '//label[@for="id_gender1"]')
    GENDER_FEMALE = (By.XPATH, '//label[@for="id_gender2"]')

class CreateAccountPage(BasePage):
    def choose_gender(self, gender):
        if gender == Gender.MALE:
            self.driver.find_element(*Locators.GENDER_MALE).click()
        else:
            self.driver.find_element(*Locators.GENDER_FEMALE).click()
    def enter_firstname(self, firstname):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(firstname)

    def _verify_page(self):
        sleep(3)