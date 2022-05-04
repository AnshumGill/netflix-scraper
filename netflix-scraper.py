from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import logging
import time

# Netflix Credentials
login_email=""
login_pass=""
# Netflix Homepage URL
netflix_url="https://netflix.com"

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')

with webdriver.Chrome(service=Service(executable_path="chromedriver.exe"),options=chrome_options) as driver:
    driver.get(netflix_url)
    logging.info("Netflix Homepage Openend")
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sign In')))
    driver.find_element(by=By.LINK_TEXT,value="Sign In").click()
    logging.info("On Sign In Page")
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, 'userLoginId')))
    email=driver.find_element(by=By.NAME,value="userLoginId")
    logging.info("Filling in User Email")
    email.send_keys(login_email)
    password=driver.find_element(by=By.NAME,value="password")
    logging.info("Filling in User Password")
    password.send_keys(login_pass)
    driver.find_element(by=By.CLASS_NAME,value="login-button").click()

    try:
        logging.info("Successfully Logged In")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'choose-profile')))
        profiles=driver.find_elements(by=By.CLASS_NAME,value="profile-link")
        logging.info("On Profile page, selecting profile")
        profiles[0].click()
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".color-secondary.hasLabel.hasIcon")))
        driver.find_element(by=By.CSS_SELECTOR,value=".color-secondary.hasLabel.hasIcon").click()
        logging.info("Opening Movie Title Card")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/video")))
        video=driver.find_element(by=By.XPATH,value="/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/video")
        logging.info("Checking if Video is playing")
        if(float(video.get_attribute('currentTime')) > 0):
            logging.info("Video is playing")
        logging.info("Getting Description")
        desc=driver.find_element(by=By.CLASS_NAME,value="preview-modal-synopsis").get_attribute("innerText")
        logging.info("Description - "+str(desc))
        logging.info("Getting Cast")
        cast=driver.find_element(by=By.CLASS_NAME,value="previewModal--detailsMetadata")\
            .find_element(by=By.CLASS_NAME,value="previewModal--detailsMetadata-right")\
            .find_element(by=By.CLASS_NAME,value="previewModal--tags")\
            .find_elements(by=By.CLASS_NAME,value="tag-item")
        cast_str='Cast - '
        for c in cast:
            cast_str+=str(c.get_attribute("innerText")).strip()
        logging.info(cast_str)

    except NoSuchElementException:
        logging.exception("Element Specified not found.")

    except TimeoutException:
        logging.exception("Timed out waiting for page to load. Please Retry.")