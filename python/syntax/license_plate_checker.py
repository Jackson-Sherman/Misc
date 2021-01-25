import re
from requests import get
from io import BytesIO
from PIL import Image

def getImage(url):
    response = get(url)
    image_bytes = BytesIO(response.content)
    return Image.open(image_bytes)

stri = 'kana'


def test(string):
    if '  ' in string: # May not have 2 or more consecutive spaces
        return test(string.replace('  ',' '))
    
    string = string.upper()
    string = string.strip()

    if len(string) > 8:
        return test(string[:8])

    i = set(string) # i for input
    s = set(' ') # s for space
    n = set('0123456789') # n for numeral
    a = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ') # a for alphabetical
    if not (i <= s | n | a): # May not include punctuation or special characters (e.g. &, #, $, @)
        return None
    elif i <= s | n: # May not contain numbers only
        return None
    elif len(string) < 2: # Must contain at least two characters
        return None
    elif len(string) > 8: # May not be longer than 8 charachters
        return None
    elif len(string) == 8 and ' ' not in string: # If it is 8 characters long, then there must be at least one space
        return None
    elif set(string[:4]) <= n and len(string) <= 6 and set(string[4:]) <= a: # May not follow the format three numbers followed by one to three letters
        return None
    elif set(string[:3]) <= a and len(string) <= 6 and set(string[3:]) <= n: # May not follow the format two letters followed by one to four numbers
        return None
    else:
        return string

def present(inp):
    string = test(inp)
    if not string:
        string = 'IN-VALID'
    if string:
        while ' ' in string:
            string = string.replace(' ', '%20')
        return getImage('https://mybmv.bmv.in.gov/BMV/mybmv/PLP/PlateImage.aspx?prod=108&len=8&text=' + string + '&mc=0')

if __name__ == '__main__':
    plates = (
        ('SHII ANN','PARVITI ',' CIRIE  ','RBD GDSS'),
        ('YUL KWON','  PARV  ','VLACHOS ','VECEPIA '),
        ('PRPL KEL','QSTAYSQ ',' SANDRA ',' NAONKA '),
        ('J PROBST','GO2ROCK ','321 VOTE','SRVR S28'),
        ('FINAL 3 ','FINAL 2 ','   F3   ',' ROTU 4 '),
        ('CAGAYAN ',' GABON  ',' NOBAG  ','  SRVR  ')
    )
    output = Image.new('RGB',(288*max([len(row) for row in plates]),144*len(plates)))
    for y,row in enumerate(plates):
        for x,string in enumerate(row):
            output.paste(present(string),(x*288,y*144))
            print(str((x,y)) + ' ' + string)
    
    output.show()
    
    

'''
0 123456
01 23456
012 3456
0123 456
01234 56
012345 6
0 1 2345
0 12 345
0 123 45
0 1234 5
01 2 345
01 23 45
01 234 5
012 3 45
012 34 5
0123 4 5
0 1 2 34
0 1 23 4
0 12 3 4
01 2 3 4
0123456
0 12345
01 2345
012 345
0123 45
01234 5
0 1 234
0 12 34
0 123 4
01 2 34
01 23 4
012 3 4
0 1 2 3
012345
0 1234
01 234
012 34
0123 4
0 1 23
0 12 3
01 2 3
01234
0 123
01 23
012 3
0 1 2
0123
0 12
01 2
012
0 1
01
'''