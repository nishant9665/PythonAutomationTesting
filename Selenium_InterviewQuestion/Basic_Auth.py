
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(20)
# ... Get the URL
ele_basicAuth = driver.find_element(By.XPATH,"//li//a[contains(text(),'Basic Auth')]")
ele_basicAuth.click()
# Handle Basic Auth Case
username = "admin"
password = "admin"
string_URL = "https://" + username + ":" + password + "@the-internet.herokuapp.com/basic_auth"

driver.get(string_URL)
print("This is title ", driver.title)









