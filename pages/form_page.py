import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open_page(self):
        self.driver.get("https://practice-automation.com/form-fields/")
        return self

    def enter_name(self, name):
        input_name = self.wait.until(EC.element_to_be_clickable((By.ID, "name-input")))
        input_name.clear()
        input_name.send_keys(name)
        return self

    def enter_password(self, password):
        input_password = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
        input_password.clear()
        input_password.send_keys(password)
        return self

    def select_drinks(self):
        drink_ids = ["drink2", "drink3"]
        for drink_id in drink_ids:
            drink = self.wait.until(EC.element_to_be_clickable((By.ID, drink_id)))
            drink.click()
        return self

    def select_color(self):
        color = self.wait.until(EC.element_to_be_clickable((By.ID, "color3")))
        color.click()
        return self

    def select_automation(self):
        automation_select = Select(self.wait.until(EC.element_to_be_clickable((By.ID, "automation"))))
        automation_select.select_by_value("yes")
        return self

    def enter_email(self, email):
        input_email = self.wait.until(EC.element_to_be_clickable((By.ID, "email")))
        input_email.clear()
        input_email.send_keys(email)
        return self

    def enter_message(self, message="Hello, this is a test message"):
        input_message = self.wait.until(EC.element_to_be_clickable((By.ID, "message")))
        input_message.clear()
        input_message.send_keys(message)
        return self

    def submit(self):
        submit_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
        submit_btn.click()
        # time.sleep(1)
        return self

    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text