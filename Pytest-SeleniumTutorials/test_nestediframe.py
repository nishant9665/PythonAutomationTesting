import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
def test_dropdown():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.delete_all_cookies()
        driver.get('https://admin:admin@the-internet.herokuapp.com/') #Frames
        driver.find_element(By.XPATH, "//li//a[contains(text(),'Frames')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Nested Frames')]").click()
        driver.switch_to.frame("frame-top")
        print("This is switched to top frame")
        driver.switch_to.default_content() # return to default page
        print("This is switched to default page ")
        driver.switch_to.frame("frame-bottom")
        print("This is switched to bottom page ")
        print("Again start from begin so cant jump near or preceding or sibling framework directly------------------------------------")
        driver.switch_to.default_content()  # return to default page
        print("This is switched to default page ")
        driver.switch_to.frame("frame-top")
        print("This is switched to top frame")
        driver.switch_to.frame("frame-left")
        print("This is switched to left frame") #frame-middle
        print("Again start from begin so cant jump near or preceding or sibling framework directly------------------------------------")
        driver.switch_to.default_content()  # return to default page
        print("This is switched to default page ")
        driver.switch_to.frame("frame-top")
        print("This is switched to top frame")
        driver.switch_to.frame("frame-middle")
        print("This is switched to frame-middle frame")
        print("Again start from begin so cant jump near or preceding or sibling framework directly ------------------------------------")
        driver.switch_to.default_content()  # return to default page
        print("This is switched to default page ")
        driver.switch_to.frame("frame-top")
        print("This is switched to top frame")
        driver.switch_to.frame("frame-right")
        print("This is switched to frame-middle frame")
