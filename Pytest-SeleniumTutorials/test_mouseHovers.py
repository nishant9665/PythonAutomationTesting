import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_mouseOver():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.delete_all_cookies()
        driver.get('https://admin:admin@the-internet.herokuapp.com/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//li//a[contains(text(),'JQuery UI Menus')]").click()
        wait = WebDriverWait(driver, 10)
        src1 = driver.find_element(By.XPATH,"//li[@id='ui-id-3']")  #ui-id-4
        src2 = driver.find_element(By.ID, "ui-id-4")
        src1.click()
        wait.until(ec.element_to_be_clickable(src2))
        src2.click()
        #des1 =driver.find_element(By.ID,"ui-id-5")
        des1 = driver.find_element(By.XPATH,"//a[contains(text(),'PDF')]")
        wait.until(ec.element_to_be_clickable(des1))
        actChain = ActionChains(driver)
        actChain.move_to_element(src1).move_to_element(src2).move_to_element(des1).click().perform()
        # import os
        #
        # # file name with extension
        # file_name = os.path.basename('C:/Users/user/Downloads/menu.pdf')
        #
        # # file name without extension
        # print(os.path.splitext(file_name)[0])
