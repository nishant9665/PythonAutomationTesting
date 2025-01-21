import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_keyPress():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get('https://admin:admin@the-internet.herokuapp.com/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//li//a[contains(text(),'Key Presses')]").click()
        act = ActionChains(driver)
        act.send_keys(Keys.TAB).perform()
        result = driver.find_element(By.ID, "result")
        wait = WebDriverWait(driver,10)
        wait.until(ec.visibility_of_element_located((By.ID,"result")))
        assert result.text == "You entered: TAB"