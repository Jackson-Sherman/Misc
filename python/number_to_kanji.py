def kanji(n):
    d = {
        0: "○",
        1: "一",
        2: "二",
        3: "三",
        4: "四",
        5: "五",
        6: "六",
        7: "七",
        8: "八",
        9: "九",
        10: "十",
        100: "百",
        1000: "千",

    }
    if n not in d:
        if n < 10000:
            if n < 10 and 0 < n :
                return d[n]
            output = ""
            cur = str(n)
            if n[-] # work here *winks*

        else:
            d[n] = d[0]
    return d[n]

if __name__ == "__main__":
    import random
    
    maxi = 9
    repeat_count = 10
    
    for _ in range(repeat_count):
        num = int(10 ** (random.random() * maxi))
        def add_commas(n, spacing):
            if isinstance(n, str):
                if len(n) <= spacing:
                    return n
                else:
                    return add_commas(n[:-spacing], spacing) + "," + n[-spacing:]
            else:
                return add_commas(str(n), spacing)
        print((("{:>" + str(maxi+(maxi-1)//3) + "} => ")*3).format(num, add_commas(num, 3), add_commas(num, 4), kanji(num))[:-4])