#! python3
# commandLineEmailer.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import sys, time

service = Service(executable_path="/snap/bin/geckodriver")


if len(sys.argv) > 2:
    print(sys.argv)
    browser = webdriver.Firefox(service=service)
    browser.get('https://gmail.com')

    gmail_id = #Use an environment variable
    password = #Use an environment variable
    login_box = browser.find_element(By.NAME,'identifier')
    login_box.send_keys(gmail_id)
    login_box.send_keys(Keys.ENTER)

    time.sleep(20)

    password_box = browser.find_element(By.NAME, 'Passwd')
    password_box.send_keys(password)
    password_box.send_keys(Keys.ENTER)
    time.sleep(20)

    compose_button = browser.find_element(By.XPATH, "//div[@class='aic']/div/div")
    compose_button.click()

    time.sleep(20)


    email_sender = browser.find_element(By.XPATH, '//input[@role="combobox"]')
    email_sender.send_keys(sys.argv[1])

    body_text = browser.find_element(By.XPATH, '//div[@role="textbox"]')
    body_text.send_keys(' '.join(sys.argv[2:]))

    send_button = browser.find_element(By.XPATH, '//div[text()="Send"]')
    send_button.click()
