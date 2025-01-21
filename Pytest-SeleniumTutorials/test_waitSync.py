from selenium import webdriver
from selenium.webdriver.common.by import By


def test_waitScript():
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.refresh()
        name =driver.find_element(By.XPATH,"//tr[2]//td[1][contains(text(),'Rahul Shetty')]").text
        print("This is text : ",name)

