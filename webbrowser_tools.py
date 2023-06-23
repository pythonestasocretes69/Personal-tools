import webbrowser 

def getweb(address , option = None):
    # register all browsers we have

    ##1 brave
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    if 'brave' not in webbrowser._browsers:
        webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
    ##2 Crome
    crome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    if 'crome' not in webbrowser._browsers:
        webbrowser.register('crome', None, webbrowser.BackgroundBrowser(crome_path))
    ##3 Firefox
    fox_path = "‪C:\Program Files\Mozilla Firefox\firefox.exe"
    if 'firefox' not in webbrowser._browsers:
        webbrowser.register('firefox', None, webbrowser.GenericBrowser('firefox'), preferred=True)
    ##4 Explorer
    edge_path ="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if 'explorer' not in webbrowser._browsers:
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

    #Menu
    if option != None:
        print(option, 'is the option chosen')
    else:
        option = int(input('''Enter the browser you want to use
1-> Brave
2-> Crome
3-> Firefox <not fuctional right now>
4-> Explorer\n#'''))
    if option == 1:
        webbrowser.get('brave').open(address)
    elif option == 2:
        webbrowser.get('crome').open(address)
    elif option == 3:
        webbrowser.get('firefox').open(address)
    elif option == 4:
        webbrowser.get('edge').open(address)
    else:
        webbrowser.get('brave').open(address)
