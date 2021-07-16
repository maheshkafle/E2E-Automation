from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

"""
Test ad entry on page load
"""

URL = "https://the-internet.herokuapp.com/entry_ad"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
driver.maximize_window()

# Main logic here to close modal is to add Explicit Wait and use element_to_be_clickable function
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="modal"]/div[2]/div[3]/p'))).click()

# Added static wait to slow down process and validate in UI
time.sleep(3)
driver.quit()
