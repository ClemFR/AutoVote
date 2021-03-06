from Variables import MyGlobals as Global
import VButton
import time

from datetime import datetime

def TabFocus(TabNumber):
    Global.driver.switch_to.window(Global.driver.window_handles[TabNumber])

def timechecker():
    current = int(round(time.time()))
    if Global.timer1H - current < -5:
        Voteur(0)
        Global.timer1H = Global.timer1H + 3620
        print("[" + time.strftime("%H:%M:%S", time.localtime()) + "] -- Voté pour le site d'intervalle 1H \nProchain "
                                                                  "vote estimé à " +
              datetime.datetime.fromtimestamp(int(round(Global.timer1H))).strftime("%H:%M:%S"))

    if Global.timer1H - current < -5:
        Voteur(1)
        Global.timer1H30 = Global.timer1H30 + 5420
        print("[" + time.strftime("%H:%M:%S", time.localtime()) + "] -- Voté pour le site d'intervalle 1H \nProchain "
                                                                  "vote estimé à " +
              datetime.datetime.fromtimestamp(int(round(Global.timer1H))).strftime("%H:%M:%S"))

    if Global.timer1H - current < -5:
        Voteur(2)
        Global.timer2H = Global.timer2H + 7220
        print("[" + time.strftime("%H:%M:%S", time.localtime()) + "] -- Voté pour le site d'intervalle 1H \nProchain "
                                                                  "vote estimé à " +
              datetime.datetime.fromtimestamp(int(round(Global.timer1H))).strftime("%H:%M:%S"))
    time.sleep(30)


def Voteur(VoteNo):
    if VoteNo == 0:
        VButton.vote1H()
        time.sleep(5)
        TabFocus(1)
        Global.driver.close()
        time.sleep(15)
        TabFocus(0)
        recompense_button = Global.driver.find_element_by_xpath("/html/body/div/div/div[@class='col-md-12']["
                                                                "1]/div/div/div/div/div/button[@class='btn btn-success "
                                                                "btn-block get-reward']")
        recompense_button.click()
    if VoteNo == 1:
        VButton.vote1H30()
        time.sleep(5)
        TabFocus(1)
        Global.driver.close()
        time.sleep(15)
        TabFocus(0)
        recompense_button = Global.driver.find_element_by_xpath("/html/body/div/div/div[@class='col-md-12']["
                                                                "1]/div/div/div/div/div/button[@class='btn btn-success "
                                                                "btn-block get-reward']")
        recompense_button.click()
    if VoteNo == 2:
        VButton.vote2H()
        time.sleep(5)
        TabFocus(1)
        Global.driver.close()
        time.sleep(15)
        TabFocus(0)
        recompense_button = Global.driver.find_element_by_xpath("/html/body/div/div/div[@class='col-md-12']["
                                                                "1]/div/div/div/div/div/button[@class='btn btn-success "
                                                                "btn-block get-reward']")
        recompense_button.click()
