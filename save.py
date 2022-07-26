from selenium.webdriver.common.by import By


class Save:

    save = (By.XPATH, "//input[@name='btnSave']")
    def __init__(self,driver):
        self.driver = driver
    def get_save(self):
        return self.driver.find_element(*Save.save).click()
