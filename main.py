from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
driver.get("https://mail.google.com")
driver.maximize_window()

email = wait.until(EC.visibility_of_element_located((By.ID, "identifierId")))
email.send_keys("kavindu@ceydigital.com")
next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d LQeN7 BqKGqe eR0mzb TrZEUc lw1w4b"] span[class="VfPpkd-vQzf8d"]')))
next_btn.click()



