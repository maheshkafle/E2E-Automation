from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

"""
Test add and remove aysnchronously changing web elements
"""

URL = "https://the-internet.herokuapp.com/dynamic_controls"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
driver.maximize_window()

remove_checkbox_button = driver.find_element(By.XPATH,'//*[@id="checkbox-example"]/button')
remove_checkbox_button.send_keys(Keys.ENTER)
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox-example"]/button')))
add_checkbox_back_button = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button')
add_checkbox_back_button.send_keys(Keys.ENTER)

# Added static wait to slow down process and validate in UI
time.sleep(3)
driver.quit()
