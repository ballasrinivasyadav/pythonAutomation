import pytest
from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    log = (By.ID,"btnLogin")

    def login_page(self):
        return self.driver.find_element(*LoginPage.log).click()

