import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
#@pytest.mark.parametrize('numberOfTime',range(5)) , same test case executed 5 time
def test_waitExplicitWait():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.delete_all_cookies()
        driver.get('https://admin:admin@the-internet.herokuapp.com/')
        wait = WebDriverWait(driver, timeout=10)
        #revealed = driver.find_element(By.ID, "revealed")
        driver.find_element(By.XPATH, "//li/a[contains(text(),'Dynamic Loading')]").click()
        driver.find_element(By.XPATH,"//div/a[contains(text(),'Example 1: Element on page that is hidden')]").click()
        driver.find_element(By.XPATH,"//div//button[contains(text(),'Start')]").click()
        loadingText = driver.find_element(By.ID,"loading").text
        print("This is line for loading :",loadingText)
        wait = WebDriverWait(driver, timeout=10)
        rr=  wait.until(ec.text_to_be_present_in_element((By.XPATH,"//div[@id='finish']//h4"),'Hello World!')) # true
        #rr=  wait.until(ec.text_to_be_present_in_element((By.XPATH,"//div[@id='finish']//h4"),'Hello World!XXX'))# return value does not evaluate to ``False``.
        rr=  wait.until(ec.visibility_of_element_located((By.ID,"finish")))# true
        print("This is output : ",rr.text) #This is output :  Hello World!
        rr=  wait.until(ec.presence_of_element_located((By.ID,"finish")))# true
        print("This is output : ",rr) #This is output :  This is output :  <selenium.webdriver.remote.webelement.WebElement



