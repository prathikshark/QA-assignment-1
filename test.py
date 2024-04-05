from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

import time

driver = webdriver.Chrome()
# google
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.ID, 'APjFqb').send_keys('orangehrm')
driver.find_element(By.ID, 'APjFqb').send_keys(Keys.ENTER)
driver.find_element(By.PARTIAL_LINK_TEXT, "opensource-demo").click()

# orange login
driver.implicitly_wait(7)
driver.find_element(By.NAME, 'username').send_keys('Admin')
driver.find_element(By.NAME, 'password').send_keys('admin123')
driver.find_element(By.XPATH, "//button").click()

# leave
leave_btn = driver.find_element(By.XPATH, "//span[text()='Leave']")
leave_btn.click()
apply_btn = driver.find_element(By.XPATH, "//a[text()='Apply']")
apply_btn.click()

# dropdown
leave_type_btn = driver.find_element(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
leave_type_btn.click()
option_btn = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='CAN - FMLA']")
option_btn.click()

# from n to
driver.find_elements(By.XPATH, "//input")[1].click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='oxd-calendar-date-wrapper']/div[text()='4']").click()

driver.find_elements(By.XPATH, "//input")[2].click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='oxd-calendar-date-wrapper']/div[text()='5']").click()

# partial days
partial_btn = driver.find_element(By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[2]")
partial_btn.click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='All Days']").click()

# duration
dur_btn = driver.find_element(By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[3]")
dur_btn.click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Half Day - Afternoon']").click()

# comment
comment_btn = driver.find_element(By.XPATH, "//textarea")
comment_btn.send_keys("leave")
comment_btn.click()
time.sleep(1.5)

# apply
submit_btn = driver.find_element(By.XPATH, "//button[contains(normalize-space(), 'Apply')]")
submit_btn.click()
time.sleep(1.5)

# leave btn
l_btn = driver.find_element(By.XPATH, "//a[text()='My Leave']")
l_btn.click()

# cancel
driver.find_element(By.XPATH,
                    "//div[text()='Availing Leave']/parent::div/following-sibling::div[1]/child::div/button[text()=' Cancel ']/following-sibling::li/button").click()

driver.find_element(By.XPATH, "//p[text()='View Leave Details']").click()

driver.find_element(By.XPATH, "//button[contains(normalize-space(), 'Cancel')]").click()

# #logout
time.sleep(1.5)
user_btn = driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']")
time.sleep(1.5)
user_btn.click()

time.sleep(1.5)
logout_btn = driver.find_element(By.XPATH, "//a[text()='Logout']")
time.sleep(1.5)
logout_btn.click()

input()

