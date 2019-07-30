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
    # Find email input element, and enter email
    emailelement = driver.find_element(By.XPATH,'.//*[@id="m_login_email"]')
    emailelement.send_keys(email)
    # Find password input element, and enter password
    passelement = driver.find_element(By.XPATH,'.//*[@id="m_login_password"]')
    passelement.send_keys(password)
    # Find login button, and click it
    login_button = driver.find_element(By.XPATH,'.//*[@id="u_0_5"]')
    login_button.click()
    # Find button to pass tha waring massage in mobile version of fb
    '''past_button = driver.find_element(By.XPATH,'.//*[@id="root"]/div[1]/div/div/div[3]/div[1]/div/div/a')
    past_button.click()'''
    driver.get('http://m.facebook.com/groups/1999858476958957/')
    time.sleep(5)

'''post_input = driver.find_element(By.XPATH,'//*[@id="u_0_w"]')
time.sleep(3)
post_input.send_keys('Hi, there!!')
time.sleep(5)

send_button = driver.find_element(By.XPATH,'.//*[@id="js_5l"]/div[2]/div[3]/div[2]/div/div/button')'''

login(email, password)
driver.quit()
