from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

"""
Add or remove web element
"""

URL = "http://the-internet.herokuapp.com/"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
is_add_remove_link_visible = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Add/Remove')))
print(is_add_remove_link_visible)
add_remove_element = driver.find_element(By.PARTIAL_LINK_TEXT,'Add/Remove')
add_remove_element.click()
is_add_button_visible = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div/button')))
print(is_add_button_visible)
add_element = driver.find_element(By.CSS_SELECTOR, 'div.example button')
add_element.send_keys(Keys.ENTER)
is_delete_button_visible = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'added-manually')))
print(is_delete_button_visible)
delete_element = driver.find_element(By.CLASS_NAME, 'added-manually')
delete_element.send_keys(Keys.ENTER)
#Added Static wait just to validate in UI
time.sleep(4)
# driver.quit()
driver.close()