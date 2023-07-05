from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from math import sin, log


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x = int(browser.find_element(By.ID, "input_value").text)
rez = log(abs(12*sin(x)))
input_rez = browser.find_element(By.ID, "answer")
input_rez.send_keys(rez)
box = browser.find_element(By.ID, "robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", box)
box.click()
robot = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", robot)
robot.click()
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(10)
browser.quit()
