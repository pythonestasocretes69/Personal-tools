import webbrowser as web
import pyautogui as auto
import time
file = open('topics.txt','r')
lines = file.readlines()
web.open('https://chat.openai.com/')
for i in lines:
    stop = input('Press Enter')
    time.sleep(10)
    auto.typewrite(i)
    time.sleep(20)
file.close()
print(lines)
