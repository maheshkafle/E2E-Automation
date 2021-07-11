from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


"""
Test Checkboxes
"""

URL = "https://the-internet.herokuapp.com/checkboxes"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div.example h3')))
checkbox_elements = driver.find_elements(By.CSS_SELECTOR,'form#checkboxes input')
print(len(checkbox_elements))
for checkbox in checkbox_elements:
    print(checkbox.get_attribute("type"))
    if checkbox.is_selected() == False:
        checkbox.click()
    print(checkbox.is_selected())