import re
def strTime (seconds):
    output = ""
    if seconds >= 24 * 60 * 60:
        output += str(seconds // (24 * 60 * 60)) + ":"
    seconds %= 24 * 60 * 60
    if seconds >= 60 * 60:
        output += str(seconds // (60 * 60)) + ":"
    seconds %= 60 * 60
    return output + "{0:0>2}:{1:0>2}".format(seconds//60, seconds%60)

def minsec2sec (minutes, seconds):
    return minutes * 60 + seconds

def getTime (seconds=0):
    string = input(strTime(seconds) + " + " )

    string = re.sub("[^0-9]","",string)

    seconds += int(string[-2:])
    string = string[:-2]

    if string:
        seconds += 60 * int(string[-2:])
        string = string[:-2]
    
    if string:
        seconds += 24 * int(string)
        string = ""
    return seconds

if __name__=="__main__":
    s = 0
    repeat = True
    while repeat:
        print()
        try: s = getTime(s)
        except: repeat = False
