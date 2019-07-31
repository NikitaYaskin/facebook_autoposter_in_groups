from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

email = 'rebrow7@ukr.net'
password = '7bodnaruk10'

text = 'There will be text'
picture = 'post.jpg'

groups = ['https://m.facebook.com/groups/robotavczechii/','https://m.facebook.com/groups/eurowork.te.ua/','https://m.facebook.com/groups/264448957510473/','https://m.facebook.com/groups/rabotapl/']

groups_to_subsribe = 'm.facebook.com/groups/1402025899898942/;m.facebook.com/groups/810637929293329/?ref=br_rs;m.facebook.com/groups/robotaEuro/;m.facebook.com/groups/2158489101040581/;m.facebook.com/groups/worklifepoland/;m.facebook.com/groups/390164985075703/ ;m.facebook.com/groups/razmorab/?ref=br_rs;m.facebook.com/groups/595245750920571/;m.facebook.com/groups/work.in.poland1/;m.facebook.com/groups/wsi.swoi.praca/;m.facebook.com/groups/213664819423119/;m.facebook.com/groups/309294916389481/;m.facebook.com/groups/1018693051597562/?ref=br_rs;m.facebook.com/groups/437887543413783/ ;m.facebook.com/groups/1605802226166656/about/ ;m.facebook.com/groups/1106914916017791/about/;m.facebook.com/groups/146607602743341/about/;m.facebook.com/groups/327777431004642/about/;m.facebook.com/groups/170842540296622/about/;m.facebook.com/groups/eurogarant/about/;m.facebook.com/groups/2038396809761567/about/;m.facebook.com/groups/fed.work.house/about/;m.facebook.com/groups/1607100779600763/about/;m.facebook.com/groups/487240408309161/about/;m.facebook.com/groups/WorkpolZOO/;m.facebook.com/groups/1311410085588893/about/;m.facebook.com/groups/workstable3/about/;m.facebook.com/groups/SZukamPracu/about/;m.facebook.com/groups/1899603693662388/about/;m.facebook.com/groups/1157993230882157/ ;m.facebook.com/groups/1483841008333030/ ;m.facebook.com/groups/496333417237567/?ref=br_rs ;m.facebook.com/groups/workines/ ;m.facebook.com/groups/284153058599894/?ref=br_rs ;m.facebook.com/groups/ArgosGroup/?ref=br_rs;m.facebook.com/groups/834815706682621/;m.facebook.com/groups/legal.work/about/          ;m.facebook.com/groups/praca.eu/members/           ;m.facebook.com/groups/pracapolska/                      ;m.facebook.com/groups/708387059361301/announcements/      ;m.facebook.com/groups/fed.work.house/?ref=group_browse_new      ;m.facebook.com/groups/BravoJob/?ref=group_browse_new      ;m.facebook.com/groups/work.in.poland.with.us/?ref=group_browse_new   ;m.facebook.com/groups/526694494438821/           ;m.facebook.com/groups/BravoJob/?ref=group_browse_new;m.facebook.com/groups/takpraca/?ref=br_rs      ;m.facebook.com/groups/workpl/        ;m.facebook.com/groups/664580683746536/members/ ;m.facebook.com/groups/310316529391664/ ;m.facebook.com/groups/PolandUA/members/ ;m.facebook.com/groups/pracapolska/?ref=br_rs   ;m.facebook.com/groups/483169858524871/   ;m.facebook.com/groups/521636951523325/       ;m.facebook.com/groups/429628224049403/             ;m.facebook.com/groups/289134834886542/                ;m.facebook.com/groups/BravoJob/members/    ;m.facebook.com/groups/1686409544945206/     ;m.facebook.com/groups/122368818443352/         ;https://www.facebook.com/groups/291482071343106/;m.facebook.com/groups/1774309186117464/;m.facebook.com/groups/2559183197441398/;m.facebook.com/groups/595093963989305/;m.facebook.com/groups/1500211643364486/;m.facebook.com/groups/229137747626872/;m.facebook.com/groups/1089045317855321/;m.facebook.com/groups/310600013067738/;m.facebook.com/groups/2322699201341107/;m.facebook.com/groups/2cosmovisa/;m.facebook.com/groups/2202176336678645/;m.facebook.com/groups/765715327097473/;m.facebook.com/groups/601280736870165/;m.facebook.com/groups/2654214021470321/;m.facebook.com/groups/187262268578017/;m.facebook.com/groups/2188886974727434/;m.facebook.com/groups/robota.ukraine/;m.facebook.com/groups/1389339277861594/;m.facebook.com/groups/105626800208975/;m.facebook.com/groups/1148213881981547/;m.facebook.com/groups/1553080791480607/;m.facebook.com/groups/1720509598044432/?ref=br_rs;m.facebook.com/groups/1170452083065055/;m.facebook.com/groups/2090530117878157/;m.facebook.com/groups/2259976227366441/;m.facebook.com/groups/467391746787695/;m.facebook.com/groups/petrov1989/;m.facebook.com/groups/254210228765574/?ref=br_rs;m.facebook.com/groups/254930011714026/;m.facebook.com/groups/455531398260426/?ref=br_rs;m.facebook.com/groups/1849966451913224/?ref=br_rs;m.facebook.com/groups/1304969076297994/?ref=br_rs;m.facebook.com/groups/316600718894465/?ref=br_rs;m.facebook.com/groups/robota.v.poland/?ref=br_rs;m.facebook.com/groups/work.in.poland1/?ref=br_rs;m.facebook.com/groups/336751676661105/?ref=br_rs;m.facebook.com/groups/213664819423119/?ref=br_rs;m.facebook.com/groups/1018693051597562/?ref=br_rs;m.facebook.com/groups/WorkPL2017/?ref=br_rs;m.facebook.com/groups/UAPLpraca/?ref=br_rs;m.facebook.com/groups/vorona.job/?ref=br_rs;m.facebook.com/groups/628751447299347/?ref=br_rs;m.facebook.com/groups/pracapol/?ref=br_rs;m.facebook.com/groups/1772907502932252/?ref=br_rs;m.facebook.com/groups/1990394824566155/?ref=br_rs;m.facebook.com/groups/1668408073473695/?ref=br_rs;m.facebook.com/groups/1499120036820114/?ref=br_rs;m.facebook.com/groups/1270608863094944/?ref=br_rs;m.facebook.com/groups/463914414089617/?ref=br_rs;m.facebook.com/groups/polandworkpoland/?ref=br_rs;m.facebook.com/groups/449009205619897/?ref=br_rs;m.facebook.com/groups/193038867712150/?ref=br_rs;m.facebook.com/groups/577128642621514/?ref=br_rs'
groups_to_subsribe = groups_to_subsribe.split(';')
list_of_groups = []
for group in groups_to_subsribe:
	list_of_groups.append(group)


driver = webdriver.Chrome('/home/nikita/Загрузки/1/Facebook-Post-Bot/chromedriver')
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
    login_button = driver.find_element(By.XPATH,'.//*[@id="u_0_5"]')
    login_button.click()
    # Find button to pass tha waring massage in mobile version of fb
    '''past_button = driver.find_element(By.XPATH,'.//*[@id="root"]/div[1]/div/div/div[3]/div[1]/div/div/a')
    past_button.click()'''
    time.sleep(3)

def add_group(link):
	'''Function for adding new groups'''
	driver.get(link)
	time.sleep(5)
	add_group = driver.find_element(By.XPATH,'//*[@id="MRoot"]/div/div[2]/div/div[1]/div/div/button')
	add_group.click()

def post(link,text,picture):
    '''Function for posting posts'''
    driver.get(link)
    time.sleep(5)

    input_field = driver.find_element(By.XPATH,'.//*[@id="u_0_3x"]/div')
    input_field.click()

    time.sleep(5)

    text_area = driver.find_element(By.XPATH,'//*[@id="uniqid_1"]')
    text_area.send_keys(text)


    #load_image = driver.find_element(By.XPATH,'.//*[@id="structured_composer_form"]/div[7]/div/button[1]/div/div[2]')
    #load_image.click()

    submit = driver.find_element(By.XPATH,'//*[@id="composer-main-view-id"]/div[3]/div/button')
    submit.click()

login(email, password)

for group in list_of_groups:
	group = str('https://') + group
	print(group)
	add_group(group)
	time.sleep(2)

'''for group in groups:
    post(group,text,picture)
    time.sleep(5)'''

driver.quit()
