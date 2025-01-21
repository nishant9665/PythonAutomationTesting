from selenium import webdriver
from selenium.webdriver.common.by import By


def test_basicControlCommand():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        ele_display = driver.find_element(By.ID,"name").is_displayed()
        print("Text box is display and return true :",ele_display)

        ele_enable = driver.find_element(By.ID, "name").is_enabled()
        print("Text box is enable and return true :", ele_enable)

        driver.find_element(By.ID,"checkBoxOption1").click()
        eleSelect = driver.find_element(By.ID, "checkBoxOption1").is_selected()
        print("This is element is selected :",eleSelect)
