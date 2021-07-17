from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


"""
Test Horizontal Slider
"""

URL = "https://the-internet.herokuapp.com/horizontal_slider"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
action_chain = ActionChains(driver)

#main logic
horizontal_slider_element = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/input')
action_chain.click_and_hold(horizontal_slider_element).move_by_offset(30,0).release().perform()

# Added static wait to slow down process and validate in UI
time.sleep(3)
driver.quit()