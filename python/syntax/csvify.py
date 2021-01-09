import re

def roster(year, school="IU"):
    path = "/Users/jacksonsherman/Documents/Misc/Rosters/{0}/{0}{1}".format(school, year)
    text = ''
    with open(path + '.txt', 'r') as file:
        text = file.read()

    # print(text)

    text = text.strip()
    text = re.sub('>(\s*\n?\s*)*<', '><', text)
    assert '開' not in text and '閉' not in text, 'sorry it just won"t work :('
    print(text)
    # 開 = open
    # 閉 = close
    lild = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九', 10: '十'}
    def intag(string):
        output = ''
        while string:
            if string[0] == '<':
                string = string[1:]
                output += '閉' if string[0] == '/' else '開'
                while string[0] != '>':
                    string = string[1:]
            else:
                if string[:3] == ' / ':
                    output += '"\t"'
                    string = string[2:]
                else:
                    output += string[0]
            string = string[1:]

        return output

    def numbered(string):
        output = ''
        m = re.match('開開[^開閉]*閉閉', string)
        while m:
            s = m.span()
            string = string[:s[0]] + string[s[0] + 1:s[1] - 1] + string[s[1]:]
            m = re.match('開開[^開閉]*閉閉', string)

        level = 0
        while string:
            if string[0] == '開':
                level += 1
                if level < 3:
                    output += lild[level]
            elif string[0] == '閉':
                if level < 3:
                    output += lild[level]
                level -= 1
            else:
                output += string[0]
            string = string[1:]
        return output

    def dups(string):
        output = ''
        
        while string:
            while string[0] in lild.values() and 1 < len(string) and string[:2] != string[0]*2:
                string = string[1:]
            if string[0] in lild.values():
                string = string[1:]
            output += string[:1]
            string = string[1:]

        return output

    text = intag(text)
    print(text)
    text = numbered(text)
    print(text)
    text = dups(text)
    print(text)
    text = re.split(lild[1],text)
    for i in range(len(text)):
        text[i] = re.split(lild[2],text[i])
    print(text)
    output = ''
    for i,line in enumerate(text):
        height = 0
        weight = 0
        for j,word in enumerate(line):
            if re.match('[0-9]-1?[0-9]', word):
                height = int(word[:1]) * 12 + int(word[2:])
                output += str(height) + '\t'
            elif re.match('[1-9][0-9][0-9]', word):
                weight = int(word)
                output += word + '\t{:.2f}\t'.format((weight*45359237)/(height*height*64516))
            elif re.match('[0-9]+', word):
                output += word + '\t'
            else:
                output += '"' + word + '"\t'
        if 0 < len(output) and output[-1] == '\t':
            output = output[:-1]
        output += '\n'
    text = output[:-1]
    print(text)
    with open(path + '.csv', 'w') as file:
        file.write(text)