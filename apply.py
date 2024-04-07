from selenium.webdriver.common.by import By
from base import BaseClass


class ApplyClass:
    def __init__(self, driver, delay):
        self.driver = driver
        self.delay = delay
        self.obj = BaseClass(self.driver, self.delay)

    def leave(self):
        # leave
        leave_btn = self.obj.wait_till_clickable((By.XPATH, "//span[text()='Leave']"))
        leave_btn.click()
        apply_btn = self.obj.wait_till_clickable((By.XPATH, "//a[text()='Apply']"))
        apply_btn.click()

    def leave_type(self):
        # dropdown
        leave_type_btn = self.obj.wait_till_clickable(
            (By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']"))
        leave_type_btn.click()
        option_btn = self.obj.wait_till_clickable((By.XPATH, "//div[@role='option']/span[text()='CAN - FMLA']"))
        option_btn.click()

    def date_from(self, from_d):
        # from n to
        from_field = self.obj.wait_till_clickable((By.XPATH, "(//input)[2]"))
        from_field.click()
        from_date = self.obj.wait_till_clickable(
            (By.XPATH, f"//div[@class='oxd-calendar-date-wrapper']/div[text()='{from_d}']"))
        from_date.click()

    def date_to(self, to_d):
        to_field = self.obj.wait_till_clickable((By.XPATH, "(//input)[3]"))
        to_field.click()
        to_date = self.obj.wait_till_clickable(
            (By.XPATH, f"//div[@class='oxd-calendar-date-wrapper']/div[text()='{to_d}']"))
        to_date.click()

    def duration(self):
        # duration
        dur_btn = self.obj.wait_till_present( (By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[3]"))
        dur_btn.click()
        btn2 = self.obj.wait_till_present((By.XPATH, "//*[text()='Half Day - Afternoon']"))
        btn2.click()
    def partial(self):
        # partial days
        partial_btn = self.obj.wait_till_present(
            (By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[2]"))
        partial_btn.click()
        btn1 = self.obj.wait_till_present((By.XPATH, "//*[text()='All Days']"))
        btn1.click()


    def comment(self, cmt):
        # comment
        comment_btn = self.obj.wait_till_present((By.XPATH, "//textarea"))
        self.obj.send_k(comment_btn, f"{cmt} will take leave")
        comment_btn.click()

    def apply(self):
        # apply
        submit_btn = self.obj.wait_till_clickable((By.XPATH, "//button[contains(normalize-space(), 'Apply')]"))
        submit_btn.click()
