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
# Menu_Icon = wait.until(EC.element_to_be_clickable((By.ID, 'menu-icon')))
# Menu_Icon.click()
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

# Step 1
# Step 2
# Step 3
# Step 4
# Step 5
# Step 6
# Step 7
# Step 8
# Step 9