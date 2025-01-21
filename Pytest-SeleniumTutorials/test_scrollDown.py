import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_dataTable():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.delete_all_cookies()
        driver.get('https://admin:admin@the-internet.herokuapp.com/')
        driver.implicitly_wait(10)
        # scroll down page by pixel-Approach 1
        #driver.execute_script("window.scrollBy(0,1000)","")
        #driver.execute_script("window.scrollBy(0,1000)", "")
        #driver.execute_script("window.scrollBy(0,1000)", "")
        #print("scroll down at the end .....................")

        # scroll down page still the element is visible
        #ele_scroll = driver.find_element(By.XPATH, "//li//a[contains(text(),'Forgot Password')]")
        #driver.execute_script("arguments[0].scrollIntoView();",ele_scroll)
        #print("scroll upto element is visible...................")

        # scroll down till end of the page
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        print("scroll upto element end...................")

