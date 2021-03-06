from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from getpass4 import getpass

user=input('Enter Email Id:') 
pwd=getpass('Enter Password:') 

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(user)
print("Email Id entered")
sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("entered password")

login_box = driver.find_element_by_name('login')
login_box.click()

print("Done")
input("Press anything to quit")
driver.quit()
print("Finished")