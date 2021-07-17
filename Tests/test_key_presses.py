from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""
Test Key Presses
"""

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "https://the-internet.herokuapp.com/key_presses"
driver.get(URL)

#Send ADD key into input element
ADD = '\ue025'
input_key_element = driver.find_element(By.ID, 'target')
input_key_element.send_keys(ADD)

#Assert success message after Key is passed into input element
result_div = driver.find_element(By.XPATH, '//*[@id="result"]')
result_div_text = result_div.text
print(result_div.text)
assert result_div_text, 'Pass Valid Input Key'

#Clear Input element
time.sleep(2)
input_key_element.clear()

#Quit driver
time.sleep(1)
driver.quit()
