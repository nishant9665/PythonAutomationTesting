from selenium import webdriver
from selenium.webdriver.common.by import By


def test_checkBox():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(20)
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkbox1 = driver.find_element(By.XPATH,"//form//input[@type='checkbox'][1]")
    checkbox2 = driver.find_element(By.XPATH, "//form//input[@type='checkbox'][2]")
    if checkbox1.is_selected():
        print("This is checked already")
    else:
        if checkbox2.is_selected():
            print("This is not checked")

