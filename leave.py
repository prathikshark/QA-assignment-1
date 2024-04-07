from selenium.webdriver.common.by import By
from base import BaseClass


class LeaveClass:
    def __init__(self, driver, delay):
        self.driver = driver
        self.delay = delay
        self.obj = BaseClass(self.driver, self.delay)

    def leave(self):
        # leave btn
        l_btn = self.obj.wait_till_present( (By.XPATH, "//a[text()='My Leave']"))
        l_btn.click()

    def option(self):
        # cancel
        btn3 = self.obj.wait_till_present( (By.XPATH,  "//div[text()='leave']/parent::div/following-sibling::div[1]/child::div/button[text()=' Cancel ']/following-sibling::li/button"))
        btn3.click()

        btn4 = self.obj.wait_till_present( (By.XPATH, "//p[text()='View Leave Details']"))
        btn4.click()

    def cancel(self):
        btn5 = self.obj.wait_till_present( (By.XPATH, "//button[contains(normalize-space(), 'Cancel')]"))
        btn5.click()
        # logout
        user_btn = self.obj.wait_till_present( (By.XPATH, "//span[@class='oxd-userdropdown-tab']"))
        user_btn.click()

    def logout(self):
        logout_btn = self.obj.wait_till_clickable( (By.XPATH, "//a[text()='Logout']"))
        logout_btn.click()




