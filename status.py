from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Status:

    status = (By.XPATH, "//select[@id='systemUser_status']")

    def __init__(self,driver):
        self.driver = driver


    def get_status(self):

        sel = Select(self.driver.find_element(*Status.status))
        return sel.select_by_visible_text("Enabled")





