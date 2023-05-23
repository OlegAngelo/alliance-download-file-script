from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open MS Edge
driver =  webdriver.Edge()

# Open facebook
driver.get('https://facebook.com')

# Wait for facebook to load using implicitly_wait(n) function
driver.implicitly_wait(5) # seconds

# Look for email and password input texts using find_element() function
input_email = driver.find_element(by=By.NAME, value='email')
input_password = driver.find_element(by=By.NAME, value='pass')

Keys.ENTER

# Input login infos
input_email.send_keys('09054948573')
input_password.send_keys('This is my password')

# Press Enter keyboard
Keys.ENTER
driver.implicitly_wait(15)

Keys.ESCAPE
is_fb_homepage_visible = driver.find_element(By.ID, "ssrb_stories_start").is_displayed()


# Sleep then turn off
time.sleep(5)
driver.quit

