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
def shutdown():
    file = 'D:\home\projects\Shut down shortcut.py'
    subprocess.run(["python", file])
