from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

"""
Test enable and disable aysnchronously changing web elements
"""

URL = "https://the-internet.herokuapp.com/javascript_error"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
driver.maximize_window()

#Main Logic
logs = driver.get_log('browser')
for log in logs:
    print(log)
    print(log['message'])
    assert log['message']
    break

#Static Wait
time.sleep(3)
driver.quit()
