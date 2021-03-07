from selenium import webdriver
from selenium.webdriver.chrome.options import Options

WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)


class MyGlobals(object):
    driver = webdriver.Chrome(chrome_options=chrome_options)
    timer1H = 0
    timer1H30 = 0
    timer2H = 0
