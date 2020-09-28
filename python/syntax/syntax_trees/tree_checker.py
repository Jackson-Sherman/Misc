import re
import io

def importing(loc = ""):
    location_of_txt_file = ""

    if not(loc):
        location_of_txt_file = str(input("Drag file into terminal and hit enter:"))

    else:
        location_of_txt_file = loc
    
    new_loc = ""
    for i,j in enumerate(location_of_txt_file):
        if j == " ":
            location_of_txt_file = location_of_txt_file[0:i] + location_of_txt_file[i + 1:]

    if location_of_txt_file[-4:] != ".txt":
        location_of_txt_file += ".txt"
    
    io.open(location_of_txt_file)

#rules = importing()
#tree = importing()
out = True

#test = io.open("newout.txt", "x")
string = "ok\nlets"

#test.write("matame\nhellos")
