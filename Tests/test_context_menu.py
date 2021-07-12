from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


"""
Test Context Click Menu or Right Click Menu
"""

URL = "https://the-internet.herokuapp.com/context_menu"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
action_chain = ActionChains(driver)
context_click_element = driver.find_element(By.ID, 'hot-spot')
action_chain.context_click(context_click_element).perform()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
