from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

"""
Test floating menu
"""

URL = "https://the-internet.herokuapp.com/floating_menu"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
driver.maximize_window()

nav_bar_element = driver.find_element(By.ID, 'menu')
nav_bar_elements = driver.find_elements(By.TAG_NAME, 'li')
current_window = driver.current_window_handle

def loop_through_nav_bar_and_click_elements(nav_bar_elements):
    '''
        Loop through li of a div and click each li's and assert it
    '''
    for ele in range(len(nav_bar_elements)):
        ## Added static wait to slow down mouse hover and validate in UI
        time.sleep(3)
        element = nav_bar_element.find_elements_by_tag_name("li")[ele]
        element.click()

#Assert presence of menu bar
loop_through_nav_bar_and_click_elements(nav_bar_elements)
# Added static wait to slow down mouse hover and validate in UI
time.sleep(3)

#Execute Scroll down to bottom of page and click menu bar
driver.execute_script("window.scroll(0,document.body.scrollHeight);")
loop_through_nav_bar_and_click_elements(nav_bar_elements)

# Added static wait to slow down mouse hover and validate in UI
time.sleep(2)
driver.quit()