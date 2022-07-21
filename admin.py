from selenium.webdriver.common.by import By


class Admin:

    def __init__(self,driver):
        self.driver = driver
    admin = (By.ID,"menu_admin_viewAdminModule")
    send_admin = (By.CSS_SELECTOR,"div[class='box searchForm toggableForm'] li:nth-child(3)")
    sEARCH = (By.XPATH,"//input[@id = 'searchSystemUser_userName']")
    aDD = (By.XPATH,"//input[@id='btnAdd']")
    employee = (By.XPATH,"//input[@id='searchSystemUser_employeeName_empName']")

    def get_admin(self):
        return self.driver.find_element(*Admin.admin).click()

    def get_search(self):
        return self.driver.find_element(*Admin.sEARCH).send_keys("srinivas")

    def get_employee(self):
        return self.driver.find_element(*Admin.employee).send_keys("ananya dash")

    def add(self):
        return self.driver.find_element(*Admin.aDD).click()
