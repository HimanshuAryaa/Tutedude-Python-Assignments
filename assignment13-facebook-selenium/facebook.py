from selenium import webdriver
import time
from selenium.webdriver.common.by import By

email ="Your Email"
password = "Your Password"
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
email_element = driver.find_element(By.XPATH, '//*[@id="_R_1h6kqsqppb6amH1_"]').send_keys(email)
password_element = driver.find_element(By.XPATH, '//*[@id="_R_1hmkqsqppb6amH1_"]').send_keys(password)
login_btn = driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div/div[1]').click()
time.sleep(5)
post = driver.find_element(By.XPATH, "//*[@name='xhpc_message']")
time.sleep(5)
post.send_keys("Hello!, Automated Post")
time.sleep(5)
buttons = driver.find_elements(By.TAG_NAME, "snd_button")
time.sleep(5)

for button in buttons:
    if button.text == "Post":
        button.click()


