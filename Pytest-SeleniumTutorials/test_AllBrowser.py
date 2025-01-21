from selenium import webdriver
def test_allBrowser():
    browserName = input("enter the name :")
    if browserName=="chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(driver.title)
        driver.quit()
    elif browserName=="firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(driver.title)
        driver.quit()
    else:
        driver = webdriver.Ie()
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(driver.title)
        driver.quit()


