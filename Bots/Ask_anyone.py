import webbrowser as web
import pyautogui as auto
import time
file = open('topics.txt','r')
lines = file.readlines()
for i in lines:
    stop = input('Press Enter')
    if i.startswith("g"):
        web.open("https://google.com")
        web.typewrite("/")
    elif i.startswith("b"):
        web.open("https://bard.com")
    elif i.startswith("c"):
        web.open("https://chat.openai.com")
    else:
     continue
    time.sleep(10)
    auto.typewrite(i[1:])
    time.sleep(20)
file.close()
print(lines)
