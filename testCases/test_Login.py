import pytest
from selenium import webdriver
from selenium.webdriver.common.bidi.cdp import logger
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utils.readProperties import ReadConfig
from utils.customLogger import LogGen

# pytest -v -s -n=2  .\test_Login.py ------------- for parallel execution
# -n count is based on how method is defined in testcases if your passing more then it's not throwing the exceptions
class Test_001_Login:
    baseurl =  ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.driver=setup
        self.logger.info("start test cases -  browser launch")
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        assert act_title =="Your store. Login"
        if act_title=="Your store. Login":
            assert True
            self.logger.info("TC-homepage Passed")
            self.driver.close()
        else:
            #self.driver.save_screenshot("C:\\Nishant_Study\\nopcommerce\\nopcommerceAdmin\\ScreenShot\\"+"Home_PageTitle.png")
            self.driver.close()
            self.logger.info("TC-homepage failed")
            assert False


    def test_Login(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        logger.info("Login page start with browser")
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickOnLogin()
        act_title = self.driver.title
        print(act_title)
        #assert act_title=="Dashboard / nopCommerce administration"
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            logger.info("Login page test case passed")
            self.driver.close()
        else:
          #  self.driver.save_screenshot("C:\\Nishant_Study\\nopcommerce\\nopcommerceAdmin\\ScreenShot\\"+"test_LoginPageTitle.png")
            self.driver.close()
            logger.info("Login page test case failed")
            assert False
