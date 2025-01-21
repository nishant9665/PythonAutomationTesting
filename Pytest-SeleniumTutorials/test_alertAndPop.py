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
        driver.find_element(By.XPATH, "//li//a[contains(text(),'JavaScript Alerts')]").click()
        driver.find_element(By.XPATH,"//li//button[@onclick='jsAlert()']").click()
        alt=driver.switch_to.alert
        print("here is alert accepted and alert text :", alt.text) #here is alert accepted and alert text : I am a JS Alert
        alt.accept() # here is alert accepted

        driver.find_element(By.XPATH,"//li//button[@onclick='jsConfirm()']").click()
        alt = driver.switch_to.alert
        print("here is Confirmation alert accepted and alert text-jsConfirm :", alt.text) #here is Confirmation alert accepted and alert text : I am a JS Confirm
        alt.accept()  # here is alert accepted
        print("here is alert accepted-jsConfirm")

        driver.find_element(By.XPATH, "//li//button[@onclick='jsConfirm()']").click()
        alt = driver.switch_to.alert
        print("here is alert text :", alt.text) #here is alert text : I am a JS Confirm
        alt.dismiss()
        print("here is alert cancel or dismiss-jsConfirm") #here is alert cancel or dismiss

        driver.find_element(By.XPATH, "//li//button[@onclick='jsPrompt()']").click()
        alt = driver.switch_to.alert
        alt.send_keys("Nishant Narwade- jsPrompt")
        print("send the data in pop text : Nishant -jsPrompt")
        alt.accept()
        print("Alert Accepted --jsPrompt")

