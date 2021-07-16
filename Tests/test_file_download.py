import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

"""
Test file downloader
"""

URL = "https://the-internet.herokuapp.com/download"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
driver.maximize_window()
file_download_links = driver.find_elements(By.TAG_NAME, 'a')
current_window = driver.current_window_handle
for link in file_download_links:
    link = link.get_attribute('href')
    driver.execute_script("window.open('" + link + "');")
    driver.switch_to.window(current_window)

time.sleep(4)
driver.quit()