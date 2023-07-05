import time
from math import log, sin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        es.text_to_be_present_in_element((By.ID, "price"), '100')
    )
button = WebDriverWait(browser, 5).until(
        es.element_to_be_clickable((By.ID, "book"))
    )
button.click()
x = int(browser.find_element(By.ID, "input_value").text)
rez = log(abs(12 * sin(x)))
input_rez = browser.find_element(By.ID, "answer")
input_rez.send_keys(rez)
button = WebDriverWait(browser, 5).until(
        es.element_to_be_clickable((By.ID, "solve"))
    )
button.click()
time.sleep(10)
browser.quit()
