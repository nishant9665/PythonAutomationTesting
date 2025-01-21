import time
from os import times
from time import thread_time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_HclInterview:

        def select_date(self,date,month_year,driver):
            driver=driver
            month_list = driver.find_elements(By.XPATH,"//div[@class='datepicker-days']//tr//th[@class='datepicker-switch']")
            print("All month",month_list)
            print("This is size ",len(month_list))
            for i in month_list:
                if month_year==month_list:
                    driver.find_element(By.XPATH,"//div[@class='datepicker-days']//tr//td[@class='day'][contains(text(),'"+date+"')]").click()
                else:
                    driver.find_element(By.XPATH,"//div[@class='datepicker-days']//tr//th[@class='datepicker-switch'][contains(text(),'')]/following::th[@class='next']").click()
                    time.sleep(3)

def test_link():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.delete_all_cookies()
    driver.get("https://formy-project.herokuapp.com/datepicker")
    driver.find_element(By.ID,"datepicker").click()
    time.sleep(1)
    print("This is clicked")
    th= Test_HclInterview()
    th.select_date("27","March 2025",driver)

    month_list = driver.find_elements(By.XPATH,"//div[@class='datepicker-days']//tr//th[@class='datepicker-switch'][contains(text(),'')]")
    # for i in month_list:
    #     if "February 2025"==month_list:
    #         driver.find_element(By.XPATH,"//div[@class='datepicker-days']//tr//td[@class='day'][contains(text(),'25')]").click()
    #
    #     else:
    #         driver.find_element(By.XPATH,"//div[@class='datepicker-days']//tr//th[@class='datepicker-switch'][contains(text(),'')]/following::th[@class='next']").click()


