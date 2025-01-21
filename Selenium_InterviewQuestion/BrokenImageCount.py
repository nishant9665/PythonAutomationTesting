import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://the-internet.herokuapp.com/")
driver.implicitly_wait(20)
broken_Image = driver.find_element(By.XPATH,"//li//a[contains(text(),'Broken Images')]")
broken_Image.click()

ele_imageList=driver.find_elements(By.XPATH,"//div[@class='example']//img")
print(ele_imageList)

count =0
for image_name in ele_imageList:
    eleImage_link = image_name.get_attribute("src")# //body//h1
    driver.get(eleImage_link)
    ele_linktext = driver.find_element(By.XPATH,"//body//h1").text
   # eleBroken_txt = linktext.get_attribute("h1")
    print(ele_linktext)
    time.sleep(5)
    driver.close()

    if ele_linktext == "Not Found":
        count=count+1
        print("Not working link are : "+eleImage_link)
    else:
        print("Working link are :",eleImage_link)

print("Broken link count is ",count)

