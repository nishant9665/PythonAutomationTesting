from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


def check_broken_images(url):
    # Set up the WebDriver (using Chrome in this case)
    driver = webdriver.Chrome()  # Adjust this to your ChromeDriver path
    driver.get(url)

    # Find all img elements on the page
    images = driver.find_elements(By.TAG_NAME, 'img')

    broken_images = []

    # Loop through all images and check their status
    for img in images:
        src = img.get_attribute('src')
        if src:  # Check if src is not None
            try:
                response = requests.get(src)
                if response.status_code != 200:  # If the response is not 200 OK, it's broken
                    print(f"Broken image: {src} - Status code: {response.status_code}")
                    broken_images.append(src)
                else:
                    print(f"Working image: {src} - Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error with image: {src} - {e}")
                broken_images.append(src)

    driver.quit()

    # Return list of broken images
    return broken_images


# Test the function
url = 'https://the-internet.herokuapp.com/broken_images'  # Replace with the URL you want to check
broken_images = check_broken_images(url)

print(f"Broken images found: {broken_images}")
