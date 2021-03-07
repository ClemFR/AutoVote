import time
import TimeChecker
import VButton
from Variables import MyGlobals as Global
import datetime
import AlcasarLogin

# Open the website
Global.driver.get('https://ulycraft.fr/vote')


def login(pseudo):
    id_box = Global.driver.find_element_by_name('username')
    # Send id information
    id_box.send_keys(str(pseudo))
    # Find login button
    login_button = Global.driver.find_element_by_xpath(
        "/html/body/div/div/div/div/div/div/form/button[@class='btn btn-success']")
    # Click login
    login_button.click()


def VoteTimeInit(Vote):
    if Vote == 0:
        VButton.vote1H()
        time.sleep(2)
        Global.timer1H = round(time.time()) + GetTextTimeLeft()
    if Vote == 1:
        VButton.vote1H30()
        time.sleep(2)
        Global.timer1H30 = round(time.time()) + GetTextTimeLeft()
    if Vote == 2:
        VButton.vote2H()
        time.sleep(2)
        Global.timer2H = round(time.time()) + GetTextTimeLeft()


def GetTextTimeLeft():
    text = Global.driver.find_element_by_xpath(
        "/html/body/div/div/div[@class='col-md-12'][1]/div/div/div/div/div[@class='alert alert-danger']").text
    base = text.find("attendre") + 9
    if text.find("heures") != -1:
        heure = text[base:text.find("heures") - 1]
        min = text[text.find("heures") + 7:text.find("minutes") - 1]
        sec = text[text.find("minutes") + 8:text.find("secondes") - 1]
    else:
        heure = "0"
        min = text[base:text.find("minutes") - 1]
        sec = text[text.find("minutes") + 8:text.find("secondes") - 1]
    return int(heure) * 60 * 60 + int(min) * 60 + int(sec)


def Loop():
    print("[" + datetime.datetime.fromtimestamp(int(round(time.time()))).strftime("%H:%M:%S") + "] - Loop initialisé")
    while True:
        TimeChecker.timechecker()


# Global.driver.execute_script("window.open('');")
# Global.driver.switch_to.window(Global.driver.window_handles[1])
# Global.driver.close()

#
login('Clement_FR')
time.sleep(2)
for i in range(3):
    VoteTimeInit(i)
    time.sleep(1)
print("Vote 1H estimé à -- " + datetime.datetime.fromtimestamp(int(round(Global.timer1H))).strftime("%H:%M:%S") + "\nVote 1H30 estimé à -- " + datetime.datetime.fromtimestamp(int(round(Global.timer1H30))).strftime("%H:%M:%S") + "\nVote 2H estimé à -- " + datetime.datetime.fromtimestamp(int(round(Global.timer2H))).strftime("%H:%M:%S") + "\n")

Loop()