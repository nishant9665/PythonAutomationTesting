import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_dropdown():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.delete_all_cookies()
        driver.get('https://admin:admin@the-internet.herokuapp.com/')
        driver.find_element(By.XPATH,"//li//a[contains(text(),'Dropdown')]").click()
        driver.find_element(By.ID,"dropdown").click()
        ele = Select(driver.find_element(By.ID,"dropdown"))
        ele.select_by_visible_text("Option 1")
        print("select_by_visible_text- done")
        ele.select_by_index(2)
        print("select_by_index- done")
        ele.select_by_value("1")
        print("select_by_value- done")

