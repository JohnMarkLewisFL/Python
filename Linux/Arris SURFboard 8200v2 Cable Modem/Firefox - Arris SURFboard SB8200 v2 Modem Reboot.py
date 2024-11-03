#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert

# Sets up the WebDriver for Firefox
driver = webdriver.Firefox()

try:
    # Opens Firefox and navigate to the modem's URL
    driver.get("https://192.168.100.1/Login.html") # The default URL for the SB8200 is "https://192.168.100.1/Login.html", but it can be changed here
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Enters the username automatically
    username_field = driver.find_element(By.ID, "loginUsername")
    username_field.send_keys("admin")  # The default username is "admin", but if yours is different, then change it here
    
    # Enters the password automatically
    password_field = driver.find_element(By.ID, "loginWAP")
    password_field.send_keys("password")  # Set your password here
    
    # Clicks the "Apply" button automatically
    apply_button = driver.find_element(By.ID, "login")
    apply_button.click()
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Navigates to the "CONFIGURATION" page automatically
    driver.get("https://192.168.100.1/Cmconfiguration.html")
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Clicks the "Reboot" button automatically
    reboot_button = driver.find_element(By.ID, "Reboot")
    reboot_button.click()
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Clicks the "OK" button automatically when the alert box shows
    alert = Alert(driver)
    alert.accept()
    
    # Wait for 5 seconds
    time.sleep(5)
    
finally:
    # Closes the Firefox window
    driver.quit()