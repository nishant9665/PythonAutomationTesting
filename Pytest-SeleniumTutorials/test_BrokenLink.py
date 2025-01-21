import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.excelRead_util import read_excel_data


# Step 2: Define the test using pytest.mark.parametrize
@pytest.mark.parametrize("username, password", read_excel_data("TestData.xlsx").values)
def test_login(username, password):
    print("This is user name :",username)
    print("This is password  :", password)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get('https://admin:admin@the-internet.herokuapp.com/')
    driver.find_element(By.XPATH, "//li//a[contains(text(),'Broken Images')]").click()