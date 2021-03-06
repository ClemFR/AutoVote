from selenium import webdriver
from Variables import MyGlobals as Global
import time

def vote1H():
    vote1 = Global.driver.find_element_by_xpath(
        "/html/body/div/div/div[@class='col-md-12'][1]/div/div/div/div[@class='row'][2]/div/div/div/a[@class='btn btn-block btn-success website'][5]")
    vote1.click()

def vote1H30():
    vote1H30 = Global.driver.find_element_by_xpath(
        "/html/body/div/div/div[@class='col-md-12'][1]/div/div/div/div[@class='row'][2]/div/div/div/a[@class='btn btn-block btn-success website'][1]")
    vote1H30.click()

def vote2H():
    vote2 = Global.driver.find_element_by_xpath(
        "/html/body/div/div/div[@class='col-md-12'][1]/div/div/div/div[@class='row'][2]/div/div/div/a[@class='btn btn-block btn-success website'][4]")
    vote2.click()

def test():
    return Global.timer1H-round(time.time())
