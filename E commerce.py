import os
import random
from random import uniform
import time
from time import sleep
import pandas as pd 
import selenium
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
waiting_time = 1
demo_time = 300

# Define your proxy here
PROXY = "192.168.30:8080"  # HOST:PORT

chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_argument(f'--host -server={PROXY}')

# Initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Set the URL to scrape
# README.md: Make sure to customize the following URL
URL = ''

# Open the URL
driver.get(URL)

# README.md: Optional sleep for initial page load
time.sleep(demo_time)

new_list = []
condition = 'TRUE'

# Loop to extract product links
while condition:
    product_List = driver.find_elements_by_class_name('')

    for el in product_List:
        ppp = el.find_elements_by_tag_name('h4')[-1]
        pp1 = ppp.find_element_by_tag_name('a')
        new_list.append(pp1.get_property('href'))

    try:
        driver.find_element_by_class_name('page_link').click()
        # README.md: Optional sleep after clicking "Load More"
        time.sleep(random.uniform(2.5))
    except:
        pass

from tqdm import tqdm

all_data = []

# Loop to extract data from each product link
for i in new_list:
    driver.get(i)

    # README.md: Extract property information using XPATHs
    property_name = driver.find_element(By.XPATH, '')  # Add XPATH for property name
    name = property_name.text

    property_features = driver.find_element(By.XPATH, '')  # Add XPATH for property features
    propertyy = property_features.text

    property_location = driver.find_element(By.XPATH, '')  # Add XPATH for property location
    location = property_location.text

    Data = {
        'property name': name,
        'property_features': propertyy,
        'property_location': location,
    }
    all_data.append(Data)

# Create a DataFrame and save it to an Excel file
df = pd.DataFrame(all_data)
df.to_excel('ecommerce_data.xlsx')
