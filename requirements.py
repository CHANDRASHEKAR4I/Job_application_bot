# requried modules
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv


# Setup browser
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
# driver.maximize_window()
