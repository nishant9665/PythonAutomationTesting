import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_doubleClick():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get('https://testautomationpractice.blogspot.com/')
        driver.implicitly_wait(10)
        #driver.find_element(By.ID, "item-4").click()
        ele_doubel= driver.find_element(By.XPATH,"//button[contains(text(),'Copy Text')]")
        driver.execute_script("arguments[0].scrollIntoView();",ele_doubel)
        act_Chain = ActionChains(driver)
        wait = WebDriverWait(driver,10)
        wait.until(ec.visibility_of_element_located((By.XPATH,"//button[contains(text(),'Copy Text')]")))
        act_Chain.double_click(ele_doubel)
        print("This is double click on text ")
        ele_double_text = driver.find_element(By.ID, "field2")
        wait.until(ec.visibility_of_element_located((By.ID, "field2")))
        textis = ele_double_text.text
        print("This is text :",textis)