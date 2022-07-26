from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class UserRole:

    userRole = (By.XPATH, "//select[@id='systemUser_userType']")

    def __init__(self,driver):
        self.driver = driver


    def get_userRole(self):
        sel = Select(self.driver.find_element(*UserRole.userRole))
        return sel.select_by_visible_text("Admin")