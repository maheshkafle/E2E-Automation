from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import requests

"""
Test broken images
"""

URL = "https://the-internet.herokuapp.com/broken_images"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/h3')))
image_elements = driver.find_elements(By.TAG_NAME,'img')

'''Loop through all images and check if the image is broken or not using requests library'''
for image in image_elements:
    print("Image Link------->", image.get_attribute('src'))
    response = requests.get(image.get_attribute('src'))
    print("Status Code------>",response.status_code)
    if response.status_code == 404:
        print("Image is Broken"  + "\n")
    else:
        print("\n")