import pandas as pd
import pytest


def read_excel_data(file_path):
    path="C://Nishant_Study//nopcommerce//nopcommerceAdmin//TestData//TestData.xlsx"
    df = pd.read_excel(path)
    return df

#@pytest.mark.parametrize("username, password", read_excel_data("TestData.xlsx").values)
def test_dataDrivenByExcelSheet():
        print(read_excel_data("tp").values)
        print("---------------------------------selenium code start--------------------")
        print("This is username :")
        print("This is password :")
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        # driver.delete_all_cookies()
        # driver.get('https://admin:admin@the-internet.herokuapp.com/')
        # driver.find_element(By.XPATH, "//li//a[contains(text(),'Form Authentication')]").click()
        # userName = driver.find_element(By.ID,"username")
        # password = driver.find_element(By.ID, "password")
        # submit_btn=driver.find_element(By.XPATH,"//button[@type='submit']")
