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


def select_page_all_emails():
    select_all_checkbox = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[style="user-select: none;"]')))
    select_all_checkbox.click()


def check_emails_read():
    time.sleep(5)
    try:
        mark_as_unread = driver.find_element(By.CSS_SELECTOR, 'div[data-tooltip="Mark as unread"]')
        if mark_as_unread:
            return False
    except NoSuchElementException:
        return True


def emails_mark_as_read():
    mark_as_read = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-tooltip="Mark as read"]')))
    mark_as_read.click()


def click_older_page():
    older = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-tooltip="Older"]')))
    older.click()


def older_page_available():
    older = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-tooltip="Older"]')))
    older_disable = older.get_attribute("aria-disabled")
    print(older_disable)
    if older_disable != "true":
        return True
    else:
        return False


def all_emails_as_read(older):
    while older:
        select_page_all_emails()
        verify = check_emails_read()
        if verify == "True":
            emails_mark_as_read()
            click_older_page()
        else:
            click_older_page()


# functions_calling
enter_email()
enter_password()
available = older_page_available()
all_emails_as_read(available)
