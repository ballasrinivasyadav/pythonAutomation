from selenium import webdriver
from selenium.webdriver.common.by import By

from admin import Admin
from loginPage import LoginPage
from up_Data import User_Password

class Test_Main():

    def test_main(self, setup):
        #user name entered
        user = User_Password(self.driver)
        user.get_username()
        #user password entered
        password = User_Password(self.driver)
        password.get_password()
        #login into account
        login = LoginPage(self.driver)
        login.login_page()
        #Admin Entered
        ad = Admin(self.driver)
        ad.get_admin()
        #Search
        search = Admin(self.driver)
        search.get_search()
        #Employee
        employee = Admin(self.driver)
        employee.get_employee()
        #####################################
        #Add Items
        # add_tems = Admin(self.driver)
        # add_tems.add()
