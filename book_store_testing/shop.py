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
driver.execute_script('window.scrollBy(0, 100);')
Add_To_Cart_Btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul li:nth-child(4) a.button')))
Add_To_Cart_Btn.click()
time.sleep(1)
Goods_In_Cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a > span.cartcontents')))
Goods_In_Cart_Value = Goods_In_Cart.text
assert Goods_In_Cart_Value == '1 Item'
print('In the cart is', Goods_In_Cart_Value + '.', end = '')
print('Test passed.')
Goods_Price_In_Cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a > span.amount')))
Goods_Price_In_Cart_Value = Goods_Price_In_Cart.text
assert Goods_Price_In_Cart_Value == '₹180.00'
print('Goods in the cart is for', Goods_Price_In_Cart_Value + '.', end = '')
print('Test passed.')
# Step 5
Shopping_Cart_Ico = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#wpmenucartli > a > i')))
Shopping_Cart_Ico.click()
# Step 6
Subtotal_Value = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr.cart-subtotal > td > span'), '₹'))
# Step 7
Total_Value = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr.order-total > td > strong > span'), '₹'))
# Cleaning shopping cart
Remove_Item_From_Cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'td.product-remove > a')))
Remove_Item_From_Cart.click()

driver.quit()
'''

#Tast 9: Work in basket
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
Menu_Shop = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Shop')))
Menu_Shop.click()
# Step 3
driver.execute_script('window.scrollBy(0, 300);')
Add_To_Cart_Btn_HTML = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul li:nth-child(4) a.button')))
Add_To_Cart_Btn_HTML.click()
time.sleep(1)
Add_To_Cart_Btn_JS = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul li:nth-child(5) a.button')))
Add_To_Cart_Btn_JS.click()
Goods_In_Cart = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a > span.cartcontents'), '2 Items'))
# # Step 4
Shopping_Cart_Ico = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#wpmenucartli > a > i')))
Shopping_Cart_Ico.click()
# # Step 5
time.sleep(1)
Remove_Item_From_Cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(1) > td.product-remove > a')))
Remove_Item_From_Cart.click()
# Step 6
Undo_Link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Undo?')))
Undo_Link.click()
# Step 7
Quantity_Text_Field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(2) > td.product-quantity > div > input')))
Quantity_Text_Field.clear()
Quantity_Text_Field.send_keys('3')
# Step 8
Update_Basket = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(3) > td > input.button')))
Update_Basket.click()
# Step 9
Quantity_Text_Field_Value = Quantity_Text_Field.get_attribute('value')
assert Quantity_Text_Field_Value == '3'
print('Test passed. In quantity text field equal is', Quantity_Text_Field_Value + '.')
# Step 10
time.sleep(1)
Apply_Coupon_Btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(3) > td > div > input.button')))
Apply_Coupon_Btn.click()
# Step 11
Alert_Messege_Field= wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.woocommerce > ul > li'), 'Please enter a coupon code.'))

time.sleep(1)
driver.quit()
'''
#Tast 10: Purchase of goods

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
Menu_Shop = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Shop')))
Menu_Shop.click()
# Step 3
driver.execute_script('window.scrollBy(0, 300);')
Add_To_Cart_Btn_HTML = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul li:nth-child(4) a.button')))
Add_To_Cart_Btn_HTML.click()
time.sleep(1)
# Step 4
Shopping_Cart_Ico = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#wpmenucartli > a > i')))
Shopping_Cart_Ico.click()
# Step 5
Proceed_to_Checkout_Btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.woocommerce > div > div > div > a')))
Proceed_to_Checkout_Btn.click()
# Step 6
First_Name_Field = wait.until(EC.element_to_be_clickable((By.ID, 'billing_first_name')))
First_Name_Field.send_keys('Vadim')
Last_Name_Field = wait.until(EC.element_to_be_clickable((By.ID, 'billing_last_name')))
Last_Name_Field.send_keys('Zinkevich')
Email_Address_Field = wait.until(EC.element_to_be_clickable((By.ID, 'billing_email')))
Email_Address_Field.send_keys('zinkevichva@gmail.com')
Phone_Field = wait.until(EC.element_to_be_clickable((By.ID, 'billing_phone')))
Phone_Field.send_keys('1234567890')
driver.execute_script('window.scrollBy(0, 500);')
Country_Selector = wait.until(EC.element_to_be_clickable((By.ID, 'select2-chosen-1')))
Country_Selector.click()
Country_Selector_Search = wait.until(EC.element_to_be_clickable((By.ID, 's2id_autogen1_search')))
Country_Selector_Search.send_keys('Russia')
Country_Selector_Search_Result = wait.until(EC.element_to_be_clickable((By.ID, 'select2-results-1')))
Country_Selector_Search_Result.click()
Address_Field = wait.until(EC.element_to_be_clickable((By.ID, 'billing_address_1')))
Address_Field.send_keys('Birzhevoy bridge')
Town_City_Field = wait.until(EC.element_to_be_clickable((By.ID, 'billing_city')))
Town_City_Field.send_keys('Saint-Peterburg')
State_City_Field = wait.until(EC.element_to_be_clickable((By.ID, 'billing_state')))
State_City_Field.send_keys('Leningrad region')
Postcode_Field = wait.until(EC.element_to_be_clickable((By.ID, 'billing_postcode')))
Postcode_Field.send_keys('1234567')
# Step 7
driver.execute_script('window.scrollBy(0, 600);')
Check_Payments_Radiobutton = wait.until(EC.element_to_be_clickable((By.ID, 'payment_method_cheque')))
Check_Payments_Radiobutton.click()
# Step 8
Place_Order_Btn = wait.until(EC.element_to_be_clickable((By.ID, 'place_order')))
Place_Order_Btn.click()
# Step 9
Thanks_Messege_Field = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'p.woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))
# Step 10
Payment_Method_Messege_Field = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'li.method > strong'), 'Check Payments'))

time.sleep(1)
driver.quit()