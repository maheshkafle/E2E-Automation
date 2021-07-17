import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
Test Geolocation
"""
geo_location = webdriver.FirefoxOptions()
geo_location.set_preference('geo.prompt.testing', True)
geo_location.set_preference('geo.prompt.testing.allow', True)
# This will mock a certain location:
geo_location.set_preference('geo.provider.network.url',
                            'data:application/json,{"location": {"lat": 10.0, "lng": 10.0}, "accuracy": 100.0}')

URL = "https://the-internet.herokuapp.com/geolocation"
# Pass options into the profile and open your page
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=geo_location)
driver.get(URL)
driver.maximize_window()

element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button')
element.send_keys(Keys.ENTER)

#Static Wait
time.sleep(3)
driver.quit()
