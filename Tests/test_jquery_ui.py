import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://the-internet.herokuapp.com/jqueryui/menu')
driver.maximize_window()
driver.implicitly_wait(5)
current_window = driver.current_window_handle

'''
We click nested jquery_ui links passing two generation of parent jquery ui element in each of the function below 
'''
def jquery_ui_mouseover_to_pdf_element(link_text_of_enabled_element, link_text_of_download_element,
                                       link_text_of_pdf_element):
    enabled_ele = driver.find_element(By.LINK_TEXT, link_text_of_enabled_element)
    action_chain = ActionChains(driver)
    action_chain.move_to_element(enabled_ele).perform()
    driver.implicitly_wait(10)
    downloads_ele = driver.find_element(By.LINK_TEXT, link_text_of_download_element)
    action_chain.move_to_element(downloads_ele).perform()
    pdf_element = driver.find_element(By.LINK_TEXT, link_text_of_pdf_element)
    pdf_element.click()
    driver.refresh()

def jquery_ui_mouseover_to_csv_element(link_text_of_enabled_element, link_text_of_download_element,
                                       link_text_of_csv_element):
    enabled_ele = driver.find_element(By.LINK_TEXT, link_text_of_enabled_element)
    action_chain = ActionChains(driver)
    action_chain.move_to_element(enabled_ele).perform()
    driver.implicitly_wait(10)
    downloads_ele = driver.find_element(By.LINK_TEXT, link_text_of_download_element)
    action_chain.move_to_element(downloads_ele).perform()
    pdf_element = driver.find_element(By.LINK_TEXT, link_text_of_csv_element)
    pdf_element.click()
    driver.refresh()

def jquery_ui_mouseover_to_excel_element(link_text_of_enabled_element, link_text_of_download_element,
                                         link_text_of_excel_element):
    enabled_ele = driver.find_element(By.LINK_TEXT, link_text_of_enabled_element)
    action_chain = ActionChains(driver)
    action_chain.move_to_element(enabled_ele).perform()
    driver.implicitly_wait(10)
    downloads_ele = driver.find_element(By.LINK_TEXT, link_text_of_download_element)
    action_chain.move_to_element(downloads_ele).perform()
    pdf_element = driver.find_element(By.LINK_TEXT, link_text_of_excel_element)
    pdf_element.click()
    driver.refresh()


jquery_ui_mouseover_to_pdf_element(link_text_of_enabled_element='Enabled',
                                   link_text_of_download_element='Downloads', link_text_of_pdf_element='PDF')
jquery_ui_mouseover_to_csv_element(link_text_of_enabled_element='Enabled',
                                   link_text_of_download_element='Downloads', link_text_of_csv_element='CSV')
jquery_ui_mouseover_to_excel_element(link_text_of_enabled_element='Enabled',
                                     link_text_of_download_element='Downloads', link_text_of_excel_element='Excel')

time.sleep(3)
driver.quit()
