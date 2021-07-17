import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

"""
Test Drop Down
"""

URL = "https://the-internet.herokuapp.com/tinymce"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
driver.maximize_window()

#First switch to frame and locate element and execute JS script to write content in wysiwyg editor
content_area_frame_id = driver.find_element(By.ID, 'mce_0_ifr')
driver.switch_to.frame(content_area_frame_id)
content_area_id = driver.find_element(By.ID, 'tinymce')
driver.execute_script("document.body.innerHTML = '" + "Hello world" + "'")
driver.switch_to.default_content()

#Static Wait
time.sleep(3)
driver.quit()

