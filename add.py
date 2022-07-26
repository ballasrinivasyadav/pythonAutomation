from selenium.webdriver.common.by import By


class Add:
    aDD = (By.XPATH, "//input[@id='btnAdd']")

    # enter_Add = (By.XPATH, "//input[@id='btnAdd']")
    def __init__(self,driver):
        self.driver = driver

    def get_add(self):
        return self.driver.find_element(*Add.aDD).click()



