import pip
import time
import pyautogui
import webbrowser
#opening the number
number = input('Enter the number')
webbrowser.open('https://api.WhatsApp.com/send?phone='+number)
#getting the text
f = open('the text.txt','r')
time.sleep(5)
pyautogui.moveTo(802, 213,duration=1)
pyautogui.click()  # click the mouse
#Typing is starting
time.sleep(5)
'''pyautogui.typewrite('hi this is the lyrics of taki taki presented to you by bot bhai')
pyautogui.press('enter')
for w in f:
    pyautogui.typewrite(w)'''
