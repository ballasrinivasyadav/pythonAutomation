from selenium.webdriver.common.by import By


class Username:


    username = (By.XPATH, "//input[@id='systemUser_userName']")

    def __init__(self,driver):
        self.driver = driver


    def get_username(self):
        return self.driver.find_element(*Username.username).send_keys("Srinivas")



