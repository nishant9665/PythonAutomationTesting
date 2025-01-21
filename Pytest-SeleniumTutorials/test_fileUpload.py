import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_keyPress():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get('https://admin:admin@the-internet.herokuapp.com/')
        driver.find_element(By.XPATH, "//li//a[contains(text(),'File Upload')]").click()
        driver.find_element(By.ID,"file-upload").send_keys("C://Users//user//Downloads//menu.pdf")
        driver.find_element(By.ID,"file-submit").click()
        ele_text = driver.find_element(By.XPATH,"//div[@class='example']/h3")
        assert ele_text.text=="File Uploaded!"
        print("This is testcase pass message :",ele_text.text)
