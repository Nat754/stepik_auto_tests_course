import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
treasure = browser.find_element(By.ID, "treasure")
x = treasure.get_attribute("valuex")
y = calc(x)
rez = browser.find_element(By.CSS_SELECTOR, '#answer')
rez.send_keys(y)
option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
option2.click()
option3 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
option3.click()
time.sleep(10)
browser.quit()
