#Task 4: View page of the good
'''
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
Login_Email_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'username')))
Login_Email_Text_Field.send_keys('zinkevichva@gmail.com')
Login_Password_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'password')))
Login_Password_Text_Field.send_keys('1qaz"WSX3edc$RFV')
Login_Btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'p:nth-child(3) > .button')))
Login_Btn.click()
# Step 3
Menu_Shop = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Shop')))
Menu_Shop.click()
# Step 4
Third_Book = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li:nth-child(3) a.woocommerce-LoopProduct-link')))
Third_Book.click()
# Step 5
Header_Required = 'HTML5 Forms'
Header = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.summary h1')))
Header_Current = Header.text
assert Header_Current == Header_Required

time.sleep(1)
driver.quit()
'''
#Task 5: Check number of products in the category
'''
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
Login_Email_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'username')))
Login_Email_Text_Field.send_keys('zinkevichva@gmail.com')
Login_Password_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'password')))
Login_Password_Text_Field.send_keys('1qaz"WSX3edc$RFV')
Login_Btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'p:nth-child(3) > .button')))
Login_Btn.click()
# Step 3
Menu_Shop = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Shop')))
Menu_Shop.click()
# Step 4
HTML_Category = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'HTML')))
HTML_Category.click()
# Step 5
Products_In_Category = driver.find_elements(By.CSS_SELECTOR, '.products .product')

if len(Products_In_Category) == 3:
    print("Test passed: three products in category ")
else:
    print("Error: in category is " + str(len(Products_In_Category)))

time.sleep(1)
driver.quit()
'''
#Task 6: Sort of goods
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
# Step 1
driver.get('http://practice.automationtesting.in/')
# Step 2
My_Account_Menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'My Account')))
My_Account_Menu.click()
Login_Email_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'username')))
Login_Email_Text_Field.send_keys('zinkevichva@gmail.com')
Login_Password_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'password')))
Login_Password_Text_Field.send_keys('1qaz"WSX3edc$RFV')
Login_Btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'p:nth-child(3) > .button')))
Login_Btn.click()
# Step 3
Menu_Shop = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Shop')))
Menu_Shop.click()
# Step 4
Sort_Selector = driver.find_element(By.CSS_SELECTOR, 'form select')
Sort_Selector_Value = Sort_Selector.get_attribute('value')
assert Sort_Selector_Value == 'menu_order'
# Step 5
Select_Action = Select(Sort_Selector)
Select_Action.select_by_index('5')
# Step 6
Sort_Selector = driver.find_element(By.CSS_SELECTOR, 'form select')
# Step 7
Sort_Selector_Value = Sort_Selector.get_attribute('value')
assert Sort_Selector_Value == 'price-desc'

time.sleep(1)
driver.quit()
'''
#Task 7: View and goods discount
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
# Step 1
driver.get('http://practice.automationtesting.in/')
# Step 2
My_Account_Menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'My Account')))
My_Account_Menu.click()
Login_Email_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'username')))
Login_Email_Text_Field.send_keys('zinkevichva@gmail.com')
Login_Password_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'password')))
Login_Password_Text_Field.send_keys('1qaz"WSX3edc$RFV')
Login_Btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'p:nth-child(3) > .button')))
Login_Btn.click()
# Step 3
Menu_Shop = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Shop')))
Menu_Shop.click()
# Step 4
Post_169 = driver.find_element(By.CSS_SELECTOR, '.post-169 h3')
Post_169.click()
# Step 5
Post_169_Old_Price = driver.find_element(By.CSS_SELECTOR, '.price > del > span')
Post_169_Old_Price_Value = Post_169_Old_Price.text
assert Post_169_Old_Price_Value == '₹600.00'
# Step 6
Post_169_New_Price = driver.find_element(By.CSS_SELECTOR, '.price > ins > span')
Post_169_New_Price_Value = Post_169_New_Price.text
assert Post_169_New_Price_Value == '₹450.00'
# Step 7
Post_169_Cover = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.images')))
Post_169_Cover.click()
# Step 8
Post_169_Close_Ico = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.pp_close')))
Post_169_Close_Ico.click()

time.sleep(1)
driver.quit()
'''
#Tast 8: Price check in basket

# Step 1
# Step 2
# Step 3
# Step 4
# Step 5
# Step 6
# Step 7


#Tast 9: Work in basket

# Step 1
# Step 2
# Step 3
# Step 4
# Step 5
# Step 6
# Step 7
# Step 8
# Step 9
# Step 10
# Step 11

#Tast 10: Purchase of goods

# Step 1
# Step 2
# Step 3
# Step 4
# Step 5
# Step 6
# Step 7
# Step 8
# Step 9
# Step 10