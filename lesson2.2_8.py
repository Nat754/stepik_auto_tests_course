import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys("Ivan")
    browser.find_element(By.NAME, 'lastname').send_keys("Petrov")
    browser.find_element(By.NAME, 'email').send_keys("text@text.text")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.ID, 'file').send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(30)
browser.quit()

