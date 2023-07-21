from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from data import LOGIN, PASSWORD


link = "https://stepik.org/lesson/236895/step/1"


def test_user_login(browser):
    browser.get(link)
    button = WebDriverWait(browser, 5).until(
        es.element_to_be_clickable((By.ID, "ember33"))
    )
    button.click()
    login = browser.find_element(By.ID, "id_login_email")
    login.send_keys(LOGIN)
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys(PASSWORD)
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()
