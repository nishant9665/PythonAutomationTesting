from selenium import webdriver
def test_allBrowser(cmdopt):
    #browserName = input("enter the name :")
    if cmdopt=="chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(driver.title)
        driver.quit()
    elif cmdopt=="firefox":
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


