from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from login import LoginClass
from apply import ApplyClass
from leave import LeaveClass

import time

driver = webdriver.Chrome()
delay = 10
# google
driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element(By.ID, 'APjFqb').send_keys('orangehrm')
driver.find_element(By.ID, 'APjFqb').send_keys(Keys.ENTER)
driver.find_element(By.PARTIAL_LINK_TEXT, "opensource-demo").click()

# orange login
login = LoginClass(driver, delay)
login.login()

# apply
apply = ApplyClass(driver, delay)
apply.leave()
apply.leave_type()
apply.date_from(10)
apply.date_to(11)
apply.partial()
apply.duration()
apply.comment("EMP:1 taking leave")
apply.apply()

# leave
leave = LeaveClass(driver, delay)
leave.leave()
leave.option()
leave.cancel()
leave.logout()

input()
