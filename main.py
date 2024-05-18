import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)
driver.get("https://mail.google.com")
driver.maximize_window()


def enter_email():
    email = wait.until(EC.visibility_of_element_located((By.ID, "identifierId")))
    email.send_keys("kavindu@ceydigital.com")
    next_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                            'button[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"] span[class="VfPpkd-vQzf8d"]')))
    next_btn.click()


def enter_password():
    time.sleep(60)  # enter_your_password
    password_input_values = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Enter your password"]'))).get_attribute(
        "data-initial-value")
    if password_input_values != "":
        next_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                'button[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"] span[class="VfPpkd-vQzf8d"]')))
        next_btn.click()
        time.sleep(5)
        try:
            error_message = driver.find_element(By.CSS_SELECTOR, 'div[aria-live="polite"] span[jsslot]')
            print(error_message.text)

        except NoSuchElementException:
            pass

    else:
        print("Please enter your password")
        time.sleep(60)
        next_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                'button[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"] span[class="VfPpkd-vQzf8d"]')))
        next_btn.click()
        try:
            error_message = driver.find_element(By.CSS_SELECTOR, 'div[aria-live="polite"] span[jsslot]')
            print(error_message.text)

        except NoSuchElementException:
            pass



# functions_calling
enter_email()
enter_password()
