from Variables import MyGlobals as Global
import VButton
import time
import datetime


def loginbis(pseudo):
    id_box = Global.driver.find_element_by_name('username')
    # Send id information
    id_box.send_keys(str(pseudo))
    # Find login button
    login_button = Global.driver.find_element_by_xpath(
        "/html/body/div/div/div/div/div/div/form/button[@class='btn btn-success']")
    # Click login
    login_button.click()


def TabFocus(TabNumber):
    Global.driver.switch_to.window(Global.driver.window_handles[TabNumber])


def timechecker():
    print("[" + time.strftime("%H:%M:%S", time.localtime()) + "] -- Time Checker looped")
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


def Reset():
    Global.driver.refresh()
    loginbis('Clement_FR')


def Voteur(VoteNo):
    if VoteNo == 0:
        print("[" + time.strftime("%H:%M:%S", time.localtime()) + "] -- Vote 1H en cours d'execution")
        Reset()
        time.sleep(2)
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
        time.sleep(2)
        Reset()
    if VoteNo == 1:
        print("[" + time.strftime("%H:%M:%S", time.localtime()) + "] -- Vote 1H30 en cours d'execution")
        Reset()
        time.sleep(2)
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
        time.sleep(2)
        Reset()
    if VoteNo == 2:
        print("[" + time.strftime("%H:%M:%S", time.localtime()) + "] -- Vote 2H en cours d'execution")
        Reset()
        time.sleep(2)
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
        time.sleep(2)
        Reset()
