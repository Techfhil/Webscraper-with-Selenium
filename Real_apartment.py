import time
import os
import random
import pandas as pd 
from time import sleep
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Set Chrome options and other initial variables
chrome_Options = Options()
demo_time = 300

# Define your proxy here
PROXY = '193.168.30.1:8080'  # Host:Port

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument(f'--port-server={PROXY}')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Set the URL to scrape
Url = ''

# README.md: Optional sleep for initial page load
driver.get(Url)
time.sleep(demo_time)

# Click the "Load More" button multiple times
Load_more = driver.find_element(By.XPATH, )
for i in range(50):
    if i < 50:
        try:
            Load_more.click()
            sleep(5)
        except:
            pass
print("Page loaded successfully")

lnks = []

# Find and store the links to individual property pages
urls = driver.find_elements(By.XPATH, )
for url in urls: 
    new_links = url.get_attribute('href')
    lnks.append(new_links)

new_data = []

# Loop through the property links and scrape data
for links in lnks:
    driver.get(links)   

    # README.md: Extract property information using XPATHs
    property_name = driver.find_element(By.XPATH, )
    name = property_name.text

    property_location = driver.find_element(By.XPATH, )
    location = property_location.text

    property_description = driver.find_element(By.XPATH, )
    description = property_description.text

    property_price = driver.find_element(By.XPATH,)
    price = property_price.text

    property_features = driver.find_element(By.XPATH, )
    features = property_features.text

    Lease_Fees = driver.find_element(By.XPATH, )
    fees = Lease_Fees.text

    Lease_Details = driver.find_element(By.XPATH, )
    Details = Lease_Details.text

    Transit_Subway = driver.find_element(By.XPATH, )
    Subway = Transit_Subway.text

    agent_contact = driver.find_element(By.XPATH, )
    contact = agent_contact.get_attribute('href') 

    Transit_Airport = driver.find_element(By.XPATH, )
    Airport = Transit_Airport.text

    Rating = driver.find_element(By.XPATH, )
    Rate = Rating.text

    # README.md: Uncomment the following lines if you want to extract an email address
    # email_address = driver.find_element(By.XPATH, '')
    # email = email_address.get_attribute('href')

    data = {
        'property name': name,
        'property location': location,
        'property description': description,
        'property features': features,
        'Transit_Subway': Subway,
        'agent contact': contact,
        'Rating': Rate,
        # 'email address': email,
    } 

    time.sleep(random.uniform(5, 3))
    new_data.append(data)

# README.md: Create a DataFrame and save it to an Excel file
df = pd.DataFrame(new_data)
df.to_excel('real_estate.xlsx')
