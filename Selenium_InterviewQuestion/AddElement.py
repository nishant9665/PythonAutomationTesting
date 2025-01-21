from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(30)

#title = driver.title() #'str' object is not callable
title = driver.title
print(title)

addRemoveElement = driver.find_element(By.XPATH,"//li//a[contains(text(),'Add/Remove Elements')]")
#addRemoveElement.click #Statement seems to have no effect and can be replaced with a function call to have effect
addRemoveElement.click() # non-return method should be written in this format ()
time.sleep(5)

driver.find_element(By.XPATH,"//button[contains(text(),'Add Element')]").click()
delElement = driver.find_element(By.XPATH,"//button[contains(text(),'Delete')]")
if delElement.is_displayed:
    print("yes it display")
    delElement.click()
    if delElement.is_displayed:
        print("Element is deleted")
else:
    print("Element is not display")
