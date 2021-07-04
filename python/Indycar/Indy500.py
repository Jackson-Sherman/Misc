import urllib.request

def getText():
    with urllib.request.urlopen("http://racecontrol.indycar.com") as url:
        html = url.read().decode()
    return html

def printText(text):

    splitup = text.split('\n')
    maxlen = len(str(len(splitup)))
    numbered = lambda n: (" " * (maxlen - len(n))) + n + " " if isinstance(n, str) else numbered(str(n))
    for i,j in enumerate(splitup):
        print(numbered(i) + j)

printText(getText())
