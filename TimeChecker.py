from Variables import MyGlobals as Global
from selenium.webdriver.common.keys import Keys
import VButton
import time


def timechecker():
    current = int(round(time.time))
    if Global.timer1H-current < -5:
        print("WIP")
        # TODO Voteur auto 1H
    if Global.timer1H - current < -5:
        print("WIP")
        # TODO Voteur auto 1H
    if Global.timer1H - current < -5:
        print("WIP")
        # TODO Voteur auto 1H

def Voteur(VoteNo):
    if VoteNo == 0:
        VButton.vote1H()
    if VoteNo == 1:
        VButton.vote1H30()
    if VoteNo == 2:
        VButton.vote2H()

