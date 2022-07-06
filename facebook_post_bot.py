from selenium import webdriver
import time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv

load_dotenv()

text = 'There will be text'
picture = 'post.jpg'
path = os.getenv('SELENIUM_PATH')
email = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


groups = ['367975614070885'] #,'2631785523616117']

driver = webdriver.Chrome(path)
driver.get('https://m.facebook.com')
time.sleep(2)

def login(email, password):
    '''Login function'''
    # Find email input element, and enter email
    emailelement = driver.find_element(By.XPATH,'.//*[@id="m_login_email"]')
    emailelement.send_keys(email)
    # Find password input element, and enter password
    passelement = driver.find_element(By.XPATH,'.//*[@id="m_login_password"]')
    passelement.send_keys(password)
    # Find login button, and click it
    login_button = driver.find_element(By.XPATH,'//*[@id="login_password_step_element"]/button')
    login_button.click()
    # Find button to pass tha waring massage in mobile version of fb
    '''past_button = driver.find_element(By.XPATH,'.//*[@id="root"]/div[1]/div/div/div[3]/div[1]/div/div/a')
    past_button.click()'''
    time.sleep(3)

def get_text():
    with open('post_text.txt', 'r') as file:
        return file.read()

def post(link, picture):
    '''Function for posting posts'''
    driver.get(str('https://m.facebook.com/groups/') + link)
    time.sleep(10)

    input_field = driver.find_element(By.XPATH,'//div[text()="Напишіть що-небудь..."]')
    input_field.click()
    time.sleep(5)

    load_image = driver.find_element(By.XPATH,'//div[text()="Світлина"]')
    time.sleep(1)
    driver.send_keys(os.getcwd()+"/image.png")
    time.sleep(1)
    
    text_area = driver.find_element(By.XPATH,'//*[@id="uniqid_1"]')
    text_area.send_keys(get_text())
    time.sleep(3)

   #load_image.click()

    submit = driver.find_element(By.XPATH,'//*[@id="composer-main-view-id"]/div[3]/div/div/button')
    # submit.click()

login(email, password)

for group in groups:
    post(group, picture)
    time.sleep(5)

driver.quit()
