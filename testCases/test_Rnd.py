import pytest
from selenium import webdriver
from selenium.webdriver.common.bidi.cdp import logger
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utils.readProperties import ReadConfig
from utils.customLogger import LogGen

# pytest -v -s -n=2  .\test_Login.py ------------- for parallel execution
# -n count is based on how method is defined in testcases if your passing more then it's not throwing the exceptions
class Test_001_Rnd:
    def test_rndPageTitle(self,setup):
        self.driver=setup
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get('https://admin:admin@the-internet.herokuapp.com/')
        self.driver.find_element(By.XPATH, "//li//a[contains(text(),'Form Authentication')]").click()
        ele_userName = self.driver.find_element(By.ID, "username")
        ele_password = self.driver.find_element(By.ID, "password")
        submit_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        ele_userName.clear()
        ele_userName.send_keys("nishant")
        ele_password.clear()
        ele_password.send_keys("lkdlksaj")
        submit_btn.click()
        ele_error = self.driver.find_element(By.XPATH, "//div[@id='flash']")
        ele_error_text = ele_error.text
        print("This is original text ", ele_error_text)
        assert ele_error_text == "Your username is invalid!\n×'"


