import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_windowsHandle():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.delete_all_cookies()
        driver.get('https://admin:admin@the-internet.herokuapp.com/')  # Frames
        st=driver.current_window_handle
        print("This is current windows :",st)
        driver.find_element(By.XPATH, "//li//a[contains(text(),'Multiple Windows')]").click()
        driver.find_element(By.XPATH,"//div[@class='example']/a").click()
        l1 = driver.window_handles
        print("This is type of title :",type(l1))
        for i in range(len(l1)): #Returns the handles of all windows within the current session.
            print(l1[i],driver.title)

