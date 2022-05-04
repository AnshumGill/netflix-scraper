from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import logging
import time

# Netflix Homepage URL
netflix_url="https://www.netflix.com/in/title/81309354"

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')

with webdriver.Chrome(service=Service(executable_path="chromedriver.exe"),options=chrome_options) as driver:
    driver.get(netflix_url)
    logging.info("Netflix Homepage Openend")
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "additional-video-wrapper")))
        driver.find_element(by=By.CLASS_NAME,value="additional-video-wrapper").find_element(by=By.TAG_NAME,value="button").click()
        logging.info("Checking if Video is playing")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "VideoContainer")))
        video_container=driver.find_element(by=By.CLASS_NAME,value="VideoContainer")
        WebDriverWait(video_container, 10).until(EC.presence_of_element_located((By.TAG_NAME, "video")))
        video=video_container.find_element(by=By.TAG_NAME,value="video")
        time.sleep(3)
        if(float(video.get_attribute('currentTime')) > 0):
            logging.info("Video is playing")
        logging.info("Getting Description")
        desc=driver.find_element(by=By.CLASS_NAME,value="title-info-synopsis").get_attribute("innerText")
        logging.info(f"Description - {str(desc)}")
        logging.info("Getting Cast")
        cast=driver.find_element(by=By.CLASS_NAME,value="title-info-talent").get_attribute("innerText").split(":")[1]
        logging.info(f"Cast - {cast}")

    except NoSuchElementException:
        logging.exception("Element Specified not found.")

    except TimeoutException:
        logging.exception("Timed out waiting for page to load. Please Retry.")