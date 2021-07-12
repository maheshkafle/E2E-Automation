from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

"""
Test Disappearing and Reappearing Elements
"""

URL = "https://the-internet.herokuapp.com/disappearing_elements"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
home_elements = driver.find_elements(By.CSS_SELECTOR,'ul li')
for element in home_elements:
    action_chain = ActionChains(driver)
    print("Mouse Hover on Element ---> ",element.text)
    # Added static wait to slow down mouse hover and validate in UI
    time.sleep(1)
    action_chain.move_to_element(element).perform()
driver.quit()
