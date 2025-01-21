import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
def test_dropdown():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.delete_all_cookies()
        driver.get('https://admin:admin@the-internet.herokuapp.com/') #Frames
        driver.find_element(By.XPATH,"//li//a[contains(text(),'Frames')]").click()
        driver.find_element(By.XPATH,"//a[contains(text(),'iFrame')]").click()
        #driver.switch_to.frame("mce_0_ifr") # by using id ,working
        #driver.switch_to.frame("Rich Text Area") # TagName is not working , Switches focus to the specified frame, by index, name, or web element.
        #driver.switch_to.frame("tox-edit-area__iframe") # class name is not working
        #driver.switch_to.frame(0) # Working
        iframeWeb_element = driver.find_element(By.XPATH,"//iframe[@id='mce_0_ifr']")
        driver.switch_to.frame(iframeWeb_element)  # Working
        print("switched successfully")
