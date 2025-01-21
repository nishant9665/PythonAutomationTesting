from selenium import webdriver
def test_basicCommand():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print("This is first url title :",driver.title)
        driver.get("https://admin-demo.nopcommerce.com/admin/")
        print("This is 2nd url title :", driver.title)
        driver.back()
        print("This is first url title :", driver.title)
        driver.forward()
        print("This is 2nd url title :", driver.title)
        driver.refresh()
        print("This is 2nd url title :", driver.title)
