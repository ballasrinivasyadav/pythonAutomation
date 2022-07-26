from selenium.webdriver.common.by import By

class ConfirmPage:

    confirmpassword = (By.XPATH, "//input[@id='systemUser_confirmPassword']")

    def __init__(self,driver):
        self.driver = driver

    def get_confirmpassword(self):
        return self.driver.find_element(*ConfirmPage.confirmpassword).send_keys("Sania@1234")


