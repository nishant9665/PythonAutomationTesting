from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

def check_broken_links(url):
    # Set up the WebDriver (using Chrome in this case)
    driver = webdriver.Chrome()  # Adjust this to your ChromeDriver path
    driver.get(url)

    # Find all links on the page
    links = driver.find_elements(By.TAG_NAME, 'a')

    broken_links = []

    # Loop through all links and check their status
    for link in links:
        href = link.get_attribute("href")
        if href:  # Check if the href is not None
            try:
                response = requests.get(href)
                if response.status_code != 200:  # If the response is not 200 OK, mark as broken
                    print(f"Broken link: {href} - Status code: {response.status_code}")
                    broken_links.append(href)
                else:
                    print(f"Working link: {href} - Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error with link: {href} - {e}")
                broken_links.append(href)

    driver.quit()

    # Return list of broken links
    return broken_links


# Test the function
url = 'https://demoqa.com/links'  # Replace with the URL you want to check
broken_links = check_broken_links(url)

print(f"Broken links found: {broken_links}")
