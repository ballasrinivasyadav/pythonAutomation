from selenium.webdriver.common.by import By


class Password:
    password = (By.XPATH, "//input[@id='systemUser_password']")

    def __init__(self,driver):
        self.driver = driver

    def get_password(self):
        return self.driver.find_element(*Password.password).send_keys("Sania@1234")
