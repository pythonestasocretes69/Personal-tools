import webbrowser
import time
file = open('topics.txt','r')
lines = file.readlines()
for i in lines:
    if (i.startswith('http')):
        webbrowser.open(i)
    else:
        webbrowser.open('https://www.google.com/search?q='+i)
    time.sleep(5)
file.close()
