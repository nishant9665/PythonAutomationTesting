import time
import pytest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


# Step 1: Function to read data from Excel
def read_excel_data(file_path):
    path = "C://Nishant_Study//nopcommerce//nopcommerceAdmin//TestData//"+file_path
    df = pd.read_excel(path)
    return df


# Step 2: Define the test using pytest.mark.parametrize
@pytest.mark.parametrize("username, password", read_excel_data("TestData.xlsx").values)
def test_login(username, password):
    print("This is user name :",username)
    print("This is password  :", password)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get('https://admin:admin@the-internet.herokuapp.com/')
    driver.find_element(By.XPATH, "//li//a[contains(text(),'Form Authentication')]").click()
    ele_userName = driver.find_element(By.ID,"username")
    ele_password = driver.find_element(By.ID, "password")
    submit_btn=driver.find_element(By.XPATH,"//button[@type='submit']")
    ele_userName.clear()
    ele_userName.send_keys(username)
    ele_password.clear()
    ele_password.send_keys(password)
    submit_btn.click()
    ele_error = driver.find_element(By.XPATH,"//div[@id='flash']")
    ele_error_text=ele_error.text
    print("This is original text ",ele_error_text)
    assert ele_error_text=="You logged into a secure area!"

