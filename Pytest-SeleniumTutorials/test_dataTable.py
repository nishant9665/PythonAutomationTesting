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
        driver.find_element(By.XPATH, "//li//a[contains(text(),'Sortable Data Tables')]").click()
        row_element = driver.find_elements(By.XPATH,"//table[@id='table1']//tbody//tr")
        col_element = driver.find_elements(By.XPATH, "//table[@id='table1']//tbody//tr[1]//td")
        print("last Name","firstName", "       email","             Due","           website","                  action")
        for row in range(1,len(row_element)+1):
            for col in range(1,len(col_element)+1):
                print(driver.find_element(By.XPATH,"//table[@id='table1']//tbody//tr["+str(row)+"]//td["+str(col)+"]").text,end="       ")
            print()

