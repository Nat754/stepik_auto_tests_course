import time
import math
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as es
from data import LOGIN, PASSWORD


@pytest.mark.parametrize('step', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_stepik_link(browser, step):
    link = f"https://stepik.org/lesson/{step}/step/1"
    browser.get(link)
    button = Wait(browser, 50).until(es.element_to_be_clickable((By.ID, "ember33")))
    button.click()
    login = browser.find_element(By.ID, "id_login_email")
    login.send_keys(LOGIN)
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys(PASSWORD)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    Wait(browser, 50).until(es.invisibility_of_element((By.CSS_SELECTOR, "body.ember-application.show-modal")))
    try:  # если есть кнопка "Решить снова", жмем её
        browser.find_element(By.CSS_SELECTOR, ".again-btn.white").click()
    except NoSuchElementException:
        pass
    Wait(browser, 50).until(es.visibility_of_element_located((By.CSS_SELECTOR, "[class='ember-text-area ember-view "
                                                                               "textarea string-quiz__textarea']")))
    Wait(browser, 50).until(es.element_to_be_clickable((By.CSS_SELECTOR, "[class='ember-text-area ember-view "
                                                                         "textarea string-quiz__textarea']")))
    browser.find_element(By.CSS_SELECTOR, "[class='ember-text-area ember-view textarea string-quiz__textarea']").\
        send_keys(math.log(int(time.time())))
    Wait(browser, 50).until(es.presence_of_element_located((By.CSS_SELECTOR, "button.submit-submission")))
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    Wait(browser, 50).until(es.visibility_of_element_located((By.CSS_SELECTOR, "p[class='smart-hints__hint']")))
    message = browser.find_element(By.CSS_SELECTOR, "p[class='smart-hints__hint']").text
    print(f'\n{message}')
