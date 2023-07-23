import pyautogui as auto
import time
import subprocess
auto.FAILSAFE = True

#tracking the position of the cursor
def track(gap = 5):
    failsafe = False
    path = []
    while True:
        try:
            position = auto.position()
            time.sleep(gap)
            path.append(position)
            print(position)
        except auto.FailSafeException:
            break
    return(path)

#automated shutdown
def shutdown():
    auto.moveTo(9,745,duration=1)
    auto.click()  # click the mouse
    time.sleep(3)
    auto.moveTo(20,701,duration=1)
    auto.click()  # click the mouse
    auto.moveTo(20,625,duration=1)
    auto.click(clicks=2)  # double-click the left mouse button  # click the mouse
    
#delayed click
def click(time=30):
    time.sleep(time)
    auto.click()
