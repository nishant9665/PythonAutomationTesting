from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/") #Loads a web page in the current browser session.
driver.maximize_window()
driver.implicitly_wait(5)
print("Site is launching")
