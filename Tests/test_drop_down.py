import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

"""
Test Drop Down
"""

URL = "https://the-internet.herokuapp.com/dropdown"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
driver.maximize_window()
select_elements = driver.find_elements(By.XPATH, '//*[@id="dropdown"]')
for select_element in select_elements:
    select_option = Select(select_element)
    print(select_element.text)
    #Method 1 ---> text value
    # select_option.select_by_visible_text("Option 1")
    #Method 2 ---> put value inside value="" in html option tag inside select tag
    select_option.select_by_value("2")
    break

time.sleep(3)
driver.quit()
