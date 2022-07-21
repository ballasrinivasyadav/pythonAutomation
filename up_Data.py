from selenium.webdriver.common.by import By


class User_Password():

        def __init__(self, driver):
            self.driver = driver

        user_name = (By.ID, "txtUsername")
        user_password = (By.NAME, "txtPassword")

        def get_username(self):
            return self.driver.find_element(*User_Password.user_name).send_keys("Admin")

        def get_password(self):
            return self.driver.find_element(*User_Password.user_password).send_keys("admin123")
