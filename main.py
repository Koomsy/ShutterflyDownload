#include selenium library
from selenium import webdriver

#Open browser and navigate to shutterfly page
driver = webdriver.Chrome()  # Replace with your preferred browser driver
driver.get("https://accounts.shutterfly.com/")

#fill in email and username; Note: this doesn't work
username_field = driver.find_element("email")
username_field.send_keys("kooms@duck.com")

password_field = driver.find_element_by_id("password")
password_field.send_keys("pythonpractice")

login_button = driver.find_element_by_id("login_button")
login_button.click()
