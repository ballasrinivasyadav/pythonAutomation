from selenium.webdriver.common.by import By


class Employee:

    employee_name = (By.XPATH, "(//input[@name='systemUser[employeeName][empName]'])[1]")


    def __init__(self,driver):
        self.driver = driver

    def get_employeeName(self):
        return self.driver.find_element(*Employee.employee_name).send_keys("Sania Shaheen")
