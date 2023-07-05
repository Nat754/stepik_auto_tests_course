import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value.nowrap')
x = x_element.text
y = calc(x)
rez = browser.find_element(By.CSS_SELECTOR, '#answer')
rez.send_keys(y)
option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
option2.click()
option3 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
option3.click()
time.sleep(10)
browser.quit()
