import sqlite3
import csv
import re

connection = sqlite3.connect('/Users/jacksonsherman/Documents/Misc/Rosters/r.db')

c = connection.cursor()
iu = "IU"

def doit(years, school="IU"):
    for year in years:
        if year < 10:
            year = "0{}".format(year)
        c.execute("DROP TABLE IF EXISTS {0}{1}".format(school, year))
        c.execute("""
        CREATE TABLE {0}{1} (
            Number integer,
            Name text,
            Position text,
            Height integer,
            Weight integer,
            BMI real,
            Class text,
            Hometown text,
            High text,
            Previous text
        )
        """.format(school, year))

        cs = csv.reader(open('/Users/jacksonsherman/Documents/Misc/Rosters/{0}/{0}{1}.csv'.format(school, year)), delimiter='\t', quotechar='"')
        d = [i for i in cs]
        for i,row in enumerate(d):
            for j,each in enumerate(row):
                if j in (0,3,4):
                    d[i][j] = int(each)
                if j == 5:
                    d[i][5] = float(each)
            c.execute("INSERT INTO {0}{1} VALUES (?".format(school, year)+",?"*9+")",d[i])
    connection.commit()

def twoyear(y0, y1, school="IU"):
    if y0 > y1:
        y0, y1 = y1, y0
    if y0 < 10:
        y0 = "0{}".format(y0)
    if y1 < 10:
        y1 = "0{}".format(y1)
    
    s = ""
    if len(school) % 2:
        s = school
    else:
        for char in school:
            s += char + " "
        s = s[:-1]

    print()
    print()
    print("* "*51 + "*")
    print("*" + " "*101 + "*")
    print("*{0:^101}*".format(s))
    print("*{0:^101}*".format("{1} - {2}".format(school, y0, y1)))
    print("*" + " "*101 + "*")
    for row in c.execute("SELECT n.Name, o.Class, n.Class, (n.Height - n.Height%12)/12, n.Height%12, (n.Height - o.Height), o.Weight, (n.Weight - o.Weight), abs(1000*(n.Weight - o.Weight)/o.Weight), n.Weight, o.BMI, round(n.BMI - o.BMI,2), n.BMI FROM {0}{2} AS n INNER JOIN {0}{1} AS o ON n.Name = o.Name ORDER BY (1000*(n.Weight - o.Weight)/o.Weight)".format(school, y0, y1)):
        print("*   {:<35}:{:>6}{:>6} | {} {:<2} {:<2}|{} {:=+3} {:3.0f}‰ {} | {:<5.2f} {:<+5.2f} {:<5.2f}   *".format(*row))

    print("*" + " "*101 + "*")
    f = (("gain", "n.Weight > o.Weight"), ("all ","TRUE"), ("loss", "n.Weight < o.Weight"))
    for where in f:
        for row in c.execute("SELECT count(*), round(avg(n.Height)/12-0.5), round(avg(n.Height)%12,1), round(sum(n.Height - o.Height),1), round(avg(o.Weight),1), round(avg(n.Weight - o.Weight),1), round(avg(n.Weight),1), round(avg(o.BMI),2), round(avg(n.BMI - o.BMI),2), round(avg(n.BMI),2) FROM {0}{2} AS n INNER JOIN {0}{1} AS o ON n.Name = o.Name WHERE ".format(school, y0, y1) + where[1]):
            if None not in row:
                print("*   {0:<98}*".format("average {} x{:<2}: {:.0f} {:<4.0f} {:.0f}|{:.1f} {:=+5.1f} {:.1f}|{:<5.2f} {:<+5.2f} {:<5.2f}".format(where[0],*row)))
            else:
                print("*   {0:<98}*".format("average {} x0".format(where[0])))
    print("*" + " "*101 + "*")
    print("* "*51 + "*")

def threeyear(y0,y1,y2):
    print("\n\n" + "*"*30 + "\n\n")
    for row in c.execute("SELECT IU20.Name, IU18.Class, IU19.Class, IU20.Class, (IU20.Height - IU20.Height%12)/12, IU20.Height%12, (IU19.Height - IU18.Height), (IU20.Height - IU19.Height), (IU20.Height - IU18.Height), IU18.Weight, (IU19.Weight - IU18.Weight), IU19.Weight, (IU20.Weight - IU19.Weight), IU20.Weight, (IU20.Weight - IU18.Weight), IU18.BMI, round(IU19.BMI - IU18.BMI,2), IU19.BMI, round(IU20.BMI - IU19.BMI,2), IU20.BMI, round(IU20.BMI - IU18.BMI,2) FROM IU20 INNER JOIN IU19 ON IU20.Name = IU19.Name INNER JOIN IU18 ON IU19.Name = IU18.Name ORDER BY (IU20.BMI-IU18.BMI)"):
        print("{:<40}:{:>6}{:>6}{:>6} | {} {:<2} {},{}:{:<2}| {} {:=+3} {} {:=+3} {} {:=+3} | {:<5} {:<+5} {:<5} {:<+5} {:<5} {:<+5}".format(*row))

doit(range(16,21))
[[twoyear(o, d+o) for o in range(16, 21 - d)] for d in range(1,22-16)]

for n in range(16,21):
    for row in c.execute("SELECT {0}, Name, max(length(Name)) FROM IU{0}".format(n)):
        print(row)


c.close()
connection.close()
