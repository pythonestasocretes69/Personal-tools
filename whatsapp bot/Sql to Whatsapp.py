import mysql.connector as bkend
import pyautogui
import time
import webbrowser

no = input('enter the no to messaged: ')
mycon = bkend.connect(host='localhost', user='root', passwd='Plank#6.626', database='business')
if mycon.is_connected():
    print('!!Successfully connected!!', end='\n' * 2)
cursor = mycon.cursor()
cursor.execute("select * from Empl")
data = cursor.fetchall()
n = 1
webbrowser.open('https://wa.me/+91'+no)
time.sleep(20)
for line in data:
    for i in line:
        pyautogui.typewrite(str(i) + ',')
    pyautogui.press('enter')
    n += 1
# trial version 1.1
