import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_Checkboxes():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.delete_all_cookies()
        driver.get('https://admin:admin@the-internet.herokuapp.com/')
        driver.find_element(By.XPATH,"//li//a[contains(text(),'Checkboxes')]").click()
        ele1_selected = driver.find_element(By.XPATH,"//input[@type='checkbox'][2]").is_selected()
        print("This is selected :",ele1_selected)

        ele2_enable = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]").is_enabled()
        print("This is selected :", ele2_enable)

        ele3_display = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]").is_displayed()
        print("This is selected :", ele3_display)