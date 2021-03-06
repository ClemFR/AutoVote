from selenium import webdriver
import time


def login_page():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://alcasar-0810012y.smile-education.fr/intercept.php?res=notyet&uamip=10.227.31.254&uamport=3990'
               '&challenge=e3418ca07ed2fbcd18ffcef1b64e4bcd&called=00-0C-29-BF-D6-99&mac=20-16-B9-B9-BF-D6&ip=10.227'
               '.17.214&nasid=alcasar-0810012y.smile-education.fr&sessionid=6041499200000018&ssl=https%3a%2f%2f1.0.0'
               '.1%3a3991%2f&userurl=http%3a%2f%2fcrl.identrust.com%2fDSTROOTCAX3CRL.crl&md'
               '=018807F257D625CC2160C6937CC77B43')


def login():
    login_button = driver.find_element_by_xpath(
        "/html/body/center/div[@id='logon']/form/table[@id='boite-logon']/tbody/tr[3]/td["
        "@id='authenticate-button']/input")
    login_button.click()


def sender(User, Passwd):
    login = driver.find_element_by_xpath(
        "/html/body/center/div[@id='logon']/form/table[@id='boite-logon']/tbody/tr[1]/td[@id='username_input']/input")
    login.send_keys(User)
    passwd = driver.find_element_by_xpath(
        "/html/body/center/div[@id='logon']/form/table[@id='boite-logon']/tbody/tr[2]/td[@id='password_input']/input")
    passwd.send_keys(Passwd)

# for i in range(2):
#    sender('CARAYG', 'JGRJ7B')
#    login()
