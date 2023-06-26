import pyautogui as auto
import time
import subprocess

def track(gap = 5):
    failsafe = False
    path = []
    while not failsafe:
        try:
            position = auto.position()
            time.sleep(gap)
            snap.append(position)
            print(position)
        except pyautogui.FailSafeException:
            failsafe = True
        return(path)
def shutdown():
    file = 'D:\home\projects\Shut down shortcut.py'
    subprocess.run(["python", file])
