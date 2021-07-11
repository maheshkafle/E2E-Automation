from selenium import webdriver
from selenium.webdriver.common.by import By
import time


"""
 Enter username and password in the popup-window in selenium Python 
"""

URL = "https://admin:admin@the-internet.herokuapp.com/basic_auth" # Main logic in this solution is to pass username and password in URL username:password@
executable_path = "C:\\Users\\mahesh.kafle\\Downloads\\chromedriver_win32\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors') #Ignores SSL certificate errors
driver = webdriver.Chrome(executable_path=executable_path, chrome_options=options)
driver.get(URL)
login_successful_div = driver.find_element(By.XPATH, '//*[@id="content"]/div/p')
print(login_successful_div.text)
assert login_successful_div.text, "Please check your credentials and try again"
#Added Static wait just to slow down the process and validate in UI
time.sleep(5)
driver.quit()