import pytest
from selenium import webdriver

@pytest.fixture
def setup(request):

    driver = webdriver.Chrome(executable_path="C:\\Users\\Srinivas\\PycharmProjects\\src\\Driver\\chromedriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    request.cls.driver = driver