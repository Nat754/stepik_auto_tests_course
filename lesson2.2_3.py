from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
summa = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(summa))
browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(10)
browser.quit()
