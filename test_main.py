import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from add import Add
from admin import Admin
from confirmpage import ConfirmPage
from employeeName import Employee
from loginPage import LoginPage
from passwordPage import Password
from save import Save
from status import Status
from up_Data import User_Password
from userRole import UserRole
from username import Username


class Test_Main():

    def test_main(self, setup):
        # user name entered
        user = User_Password(self.driver)
        user.get_username()

        # user password entered
        password = User_Password(self.driver)
        password.get_password()

        # login into account
        login = LoginPage(self.driver)
        login.login_page()

        # Admin Entered
        ad = Admin(self.driver)
        ad.get_admin()

        # Search
        search = Admin(self.driver)
        search.get_search()

        # Employee
        employee = Admin(self.driver)
        employee.get_employee()

        # Add Items
        add_tems = Add(self.driver)
        add_tems.get_add()

        # User Role

        user_role = UserRole(self.driver)
        user_role.get_userRole()

        # Employee_name
        employee = Employee(self.driver)
        employee.get_employeeName()

        # User Name
        user_name = Username(self.driver)
        user_name.get_username()

        # Status
        status = Status(self.driver)
        status.get_status()

        #password
        passWord = Password(self.driver)
        passWord.get_password()

        #ConfirmPassword
        confirmPassword = ConfirmPage(self.driver)
        confirmPassword.get_confirmpassword()

        #Save
        save = Save(self.driver)
        save.get_save()