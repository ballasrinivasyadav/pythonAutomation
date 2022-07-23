from selenium.webdriver.common.by import By

# This is the first time,i am adding & changing the code
# Which i have changed will be displayed on the GitHub
# Actually, i am only changing the admin file rather than the other files.
# Just now , I have push my code in favour your need changes , so kindly check & revert.
# Okay guys, as per our discussion changed the code more reluctant & robust .
# Further, any needs please ping me in teams.
# Okay that's all for today.



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

##########################################
    # def add(self):
    #     return self.driver.find_element(*Admin.aDD).click()
