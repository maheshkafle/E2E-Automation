import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
Test file uploader
"""

URL = "https://the-internet.herokuapp.com/upload"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
driver.maximize_window()

browse_button = driver.find_element(By.ID, 'file-upload')
browse_button.send_keys('C:\\Users\\mahesh.kafle\\Desktop\\Initial Changes in procap-test-automation\\changes.txt')
upload_button = driver.find_element(By.ID, 'file-submit')
upload_button.send_keys(Keys.ENTER)
upload_success_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/h3')))
print(upload_success_element.text)

#Test File Uploaded text after file gets uploaded successfully
assert upload_success_element.text == 'File Uploaded!'


time.sleep(3)
driver.quit()
