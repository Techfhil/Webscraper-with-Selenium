# Import necessary libraries
import time
import random
import pandas as pd
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Set up Chrome options with a proxy
chrome_options = Options()
PROXY = '193.168.20.1:8080'  # Host:Port for the proxy
chrome_options.add_argument(f'--proxy-server={PROXY}')

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Define the URL to scrape
Url = ''

# Open the URL in the browser
driver.get(Url)

# Scroll to load more results
for _ in tqdm(range(50)):
    try:
        load_more = driver.find_element(By.XPATH, )
        load_more.click()
        time.sleep(5)
    except:
        break

print("Pages loaded successfully")

# Extract store details
new_data = []
urls = driver.find_elements(By.XPATH, )
for url in tqdm(urls):
    url.location_once_scrolled_into_view
    url.click()
    time.sleep(random.uniform(4.6, 6.9))

    try:
        store_location = driver.find_element(By.XPATH, ).text
    except Exception as e:
        print("Error extracting store location:", e)
        store_location = "N/A"

    try:
        agent_contact = driver.find_element(By.XPATH, ).get_attribute('href')
    except Exception as e:
        print("Error extracting agent contact:", e)
        agent_contact = "N/A"

    data = {
        'store location': store_location,
        'agent contact': agent_contact
    }

    print("Extracted data:", data)  # Print extracted data for each link

    time.sleep(random.uniform(3, 5))

    new_data.append(data)

print("Data extraction complete")

# Convert data to DataFrame and save to Excel
df = pd.DataFrame(new_data)
print(df)  # Print DataFrame for verification
df.to_excel('grocer.xlsx', index=False)

# Close the browser
driver.quit()
