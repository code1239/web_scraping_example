import json
import logging
import configparser
from selenium.webdriver.common.by import By
from selenium import webdriver


# Configure logging settings
logging.basicConfig(filename='scraping_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the website
config = configparser.ConfigParser()
config.read('config.ini')
url  = config['commands']['WEBSITE_URL']
driver.get(url)
logging.info(f"Opening the website: {url}")

# Find all image elements on the page
images = driver.find_elements(By.TAG_NAME, 'img')

# Extract the src attribute from each image
image_src_list = [image.get_attribute('src') for image in images]
logging.info("Extracting image sources")

#Save image links to JSON file
with open('image_sources.json', 'w') as json_file:
    json.dump(image_src_list, json_file, indent=4)
logging.info("Saved image sources to image_sources.json")

# Close the browser
driver.quit()
logging.info("Browser closing...")
