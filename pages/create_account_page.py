from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from time import sleep
from utils.custom_types import Gender
from selenium.webdriver.support.select import Select

class Locators:
    FIRST_NAME = (By.ID, "customer_firstname")
    GENDER_MALE = (By.XPATH, '//label[@for="id_gender1"]')
    GENDER_FEMALE = (By.XPATH, '//label[@for="id_gender2"]')
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    REGISTER_BTN = (By.ID, 'submitAccount')
    BIRTH_DAY_SELECT = (By.ID, "days")
    BIRTH_MONTH_SELECT = (By.ID, "months")
    BIRTH_YEAR_SELECT = (By.ID, "years")

class CreateAccountPage(BasePage):
    def choose_gender(self, gender):
        if gender == Gender.MALE:
            self.driver.find_element(*Locators.GENDER_MALE).click()
        else:
            self.driver.find_element(*Locators.GENDER_FEMALE).click()
    def enter_firstname(self, firstname):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(firstname)

    def enter_password(self, password):
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def select_date_of_birth(self, date_of_birth):
        birth_day = Select(self.driver.find_element(*Locators.BIRTH_DAY_SELECT))
        birth_day.select_by_value(str(date_of_birth.day))
        birth_month = Select(self.driver.find_element(*Locators.BIRTH_MONTH_SELECT))
        birth_month.select_by_value(str(date_of_birth.month))
        birth_year = Select(self.driver.find_element(*Locators.BIRTH_YEAR_SELECT))
        birth_year.select_by_value(str(date_of_birth.year))

    def get_entered_email(self):

        return self.driver.find_element(*Locators.EMAIL).get_attribute("value")

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.FIRST_NAME))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_BTN))
        sleep(3)