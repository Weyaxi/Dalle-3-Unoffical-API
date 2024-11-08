from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import datetime
import logging
import requests
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

options = ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")
driver = Chrome(options=options)
cookie_value = "<your_cookie>"


def get_time():
    return datetime.datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")

def get_time_save():
    return datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")

def download_images(urls, save_folder):
    save_folder = save_folder[:225]  # Limit folder name length
    try:
        timestamp_folder = os.path.join(save_folder, get_time_save())
        os.makedirs(timestamp_folder, exist_ok=True)

        for index, url in enumerate(urls):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()

                filename = os.path.join(timestamp_folder, f"{save_folder} ({index + 1}).png")
                with open(filename, 'wb') as file:
                    file.write(response.content)

                logging.info(f'{get_time()} Image downloaded successfully: "{filename}"')
            except requests.exceptions.RequestException as e:
                logging.error(f"Failed to download image from {url}: {e}")
    except Exception as e:
        logging.critical(f"General error in downloading images: {e}")

def open_website(query):
    try:
        driver.get('https://www.bing.com/images/create')
        logging.info(f"{get_time()} Bing Image Creator opened")

        # Add the required cookie
        driver.add_cookie({"name": "_U", "value": cookie_value})
        driver.refresh()
        logging.info(f"{get_time()} Cookie added and page refreshed")

        # Input query and search
        input_box = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#sb_form_q')))
        input_box.send_keys(query)
        input_box.send_keys(Keys.RETURN)
        logging.info(f"{get_time()} Query sent: {query}")

        return True
    except Exception as e:
        logging.critical(f"Error opening website: {e}")
        return False

def get_urls():
    try:
        # Wait for image elements to load
        image_elements = WebDriverWait(driver, 600).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "mimg"))
        )
        # Extract URLs, skipping invalid ones (like blob URLs)
        urls = [
            element.get_attribute("src")
            for element in image_elements
            if element.get_attribute("src") and not element.get_attribute("src").startswith("blob:")
        ]
        return list(set(urls))  # Remove duplicates
    except Exception as e:
        logging.critical(f"Error while extracting image URLs: {e}")
        return []
        
