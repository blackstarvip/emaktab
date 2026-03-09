import time
import random
from selenium.webdriver.common.by import By
from browser import create_driver

driver = create_driver()

def human_type(element, text):

    for c in text:

        element.send_keys(c)

        time.sleep(random.uniform(0.05,0.2))


def login_student(login,password):

    try:

        driver.get("https://login.emaktab.uz")

        time.sleep(3)

        login_input = driver.find_element(By.NAME,"login")
        password_input = driver.find_element(By.NAME,"password")

        human_type(login_input,login)
        human_type(password_input,password)

        if driver.find_elements(By.NAME,"Captcha.Input"):

            return "captcha"

        driver.find_element(
            By.CSS_SELECTOR,"input[type='submit']"
        ).click()

        time.sleep(4)

        return "success"

    except:

        return "error"