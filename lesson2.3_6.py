from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
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
