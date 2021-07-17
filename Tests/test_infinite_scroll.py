import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

"""
Test file downloader
"""

SCROLL_PAUSE_TIME = 0.5
URL = "https://the-internet.herokuapp.com/infinite_scroll"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
driver.maximize_window()

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height