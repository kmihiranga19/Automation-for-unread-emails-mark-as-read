from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
driver.get("https://mail.google.com")

email = wait.until(EC.visibility_of_element_located((By.ID, "identifierId")))
email.send_keys("Test")



