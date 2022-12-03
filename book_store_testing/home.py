#Task 1: Add comment on home page
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
driver.execute_script('window.scrollBy(0,600);')
# Step 3
Read_more_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.woocommerce-LoopProduct-link > h3')))
Read_more_btn.click()
# Step 4
Reviews_Tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.reviews_tab > a')))
Reviews_Tab.click()
# Step 5
Stars_Score = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.star-5')))
Stars_Score.click()
# Step 6
Review_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'comment')))
Review_Text_Field.send_keys('Nice book!')
# Step 7
Name_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'author')))
Name_Text_Field.send_keys('ZinkevichVA')
# Step 8
Email_Text_Field = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
Email_Text_Field.send_keys('zinkevichva@gmail.com')
# Step 9
Submit_btn = wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
Submit_btn.click()
time.sleep(5)
driver.quit()