from selenium.webdriver.common.by import By
from base import BaseClass


class LoginClass:
    def __init__(self, driver, delay):
        self.driver = driver
        self.delay = delay
        self.obj = BaseClass(self.driver, self.delay)

    def login(self):
        # orange login
        user_field = self.obj.wait_till_present((By.NAME, 'username'))
        self.obj.send_k(user_field,'Admin')
        password_field = self.obj.wait_till_present((By.NAME, 'password'))
        self.obj.send_k(password_field,'admin123')
        login_button = self.obj.wait_till_clickable((By.XPATH, "//button"))
        login_button.click()