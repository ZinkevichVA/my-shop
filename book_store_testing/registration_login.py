'''
#Task 2: Account registration

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
# Step 1
driver.get('http://practice.automationtesting.in/')
# Step 2
My_Account_Menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'My Account')))
My_Account_Menu.click()
# Step 3
Reg_Email_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'reg_email')))
Reg_Email_Text_Field.send_keys('zinkevichva@gmail.com')
# Step 4
time.sleep(1)
Reg_Password_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'reg_password')))
Reg_Password_Text_Field.send_keys('1qaz"WSX3edc$RFV')
# Step 5
Register_Btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.woocomerce-FormRow input:nth-child(3)')))
Register_Btn.click()

time.sleep(1)
driver.quit()
'''


#Task 3: Login in system

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
# Step 1
driver.get('http://practice.automationtesting.in/')
# Step 2
My_Account_Menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'My Account')))
My_Account_Menu.click()
# Step 3
Login_Email_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'username')))
Login_Email_Text_Field.send_keys('zinkevichva@gmail.com')
# Step 4
Login_Password_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'password')))
Login_Password_Text_Field.send_keys('1qaz"WSX3edc$RFV')
# Step 5
Login_Btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'p:nth-child(3) > .button')))
Login_Btn.click()
# Step 6
Login_Btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Logout')))

time.sleep(1)
driver.quit()
