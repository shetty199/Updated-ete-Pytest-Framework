import pytest
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    user_name=(By.XPATH, "//*[@id='loginUserID']")
    password=(By.XPATH, "//*[@id='loginPassword']")
    login_click=(By.XPATH, "//*[@id='login_in_to_portal']")

    def username(self):
        return self.driver.find_element(*LoginPage.user_name)

    def password1(self):
        return self.driver.find_element(*LoginPage.password)

    def log_click(self):
        return self.driver.find_element(*LoginPage.login_click)

