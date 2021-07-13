from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

"""
Test enable and disable aysnchronously changing web elements
"""

URL = "https://the-internet.herokuapp.com/dynamic_controls"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
driver.maximize_window()

enable_button = driver.find_element(By.XPATH, '//*[@id="input-example"]/button')
enable_button.send_keys(Keys.ENTER)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="input-example"]/input')))
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="message"]')))
disable_button = driver.find_element(By.CSS_SELECTOR, 'form#input-example button')
disable_button.send_keys(Keys.ENTER)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="input-example"]/input')))
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, 'message')))

# Added static wait to slow down process and validate in UI
time.sleep(3)
driver.quit()