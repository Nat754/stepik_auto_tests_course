from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

link = "https://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = int(browser.find_element(By.ID, "input_value").text)
    rez = log(abs(12 * sin(x)))
    input_rez = browser.find_element(By.ID, "answer")
    input_rez.send_keys(rez)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
browser.quit()
