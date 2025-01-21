import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_fileDownload():
            # Step 1: Set up the download directory and browser options
            download_dir = "C://Users/user/Downloads"

            chrome_options = Options()
            #chrome_options.add_argument("--headless")  # Optional: Run in headless mode
            chrome_options.add_experimental_option("prefs", {
                "download.default_directory": download_dir,  # Set the download directory
                "download.prompt_for_download": False,       # Disable the prompt for downloading
                "download.directory_upgrade": True,          # Upgrade the download directory
                "safebrowsing.enabled": True,                # Enable safe browsing
            })

            # Step 2: Initialize the WebDriver
            driver = webdriver.Chrome(options=chrome_options)

            # Step 3: Navigate to the page and trigger the download
            driver.get("https://admin:admin@the-internet.herokuapp.com/")  # Replace with the URL that triggers download
            driver.find_element(By.XPATH, "//li//a[contains(text(),'File Download')]").click()
            download_button = driver.find_element(By.XPATH,"//a[contains(text(),'example.json')]")  # Update with your actual selector
            download_button.click()

            # Wait for the file to download (you can adjust the wait time)
            time.sleep(5)

            # Step 4: Check if the file has been downloaded
            file_name = "example.json"  # Replace with your expected file name

            # Create the full file path
            file_path = os.path.join(download_dir, file_name)

            # Check if the file exists
            if os.path.exists(file_path):
                print(f"File '{file_name}' has been downloaded successfully!")
            else:
                print(f"File '{file_name}' not found.")

            # Close the browser
            driver.quit()
