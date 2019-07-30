from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

email = 'rebrow7@ukr.net'
password = '7bodnaruk10'

driver = webdriver.Chrome('/home/nikita/Загрузки/1/Facebook-Post-Bot/chromedriver')
driver.get('http://m.facebook.com')
time.sleep(2)

def login(email, password):
    emailelement = driver.find_element(By.XPATH,'.//*[@id="m_login_email"]')
    emailelement.send_keys(email)
    
    passelement = driver.find_element(By.XPATH,'.//*[@id="m_login_password"]')
    passelement.send_keys(password)
    
    login_button = driver.find_element(By.XPATH,'.//*[@id="u_0_5"]')
    login_button.click()
    
    past_button = driver.find_element(By.XPATH,'.//*[@id="root"]/div[1]/div/div/div[3]/div[1]/div/div/a')
    past_button.click()

'''post_input = driver.find_element(By.XPATH,'//*[@id="u_0_w"]')
time.sleep(3)
post_input.send_keys('Hi, there!!')
time.sleep(5)

send_button = driver.find_element(By.XPATH,'.//*[@id="js_5l"]/div[2]/div[3]/div[2]/div/div/button')'''

login(email, password)
driver.quit()
