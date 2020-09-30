import io
import re
import math

strings = ["""  S → NP V NP
Art → the
  S → NP V PP
 CN → answer
  S → NP V NP P
 CN → boat
 NP → Art CN
 CN → present
 NP → N
  N → Homer
  V → V P
  N → Marge
 PP → P NP
  V → decided

  V → considered

  V → looked

  P → up

  P → on"""]

column_count = int(input("Type the original column count: "))

fi = open("output.txt","x")
final_string = ""
for string in strings:
  listo = re.split("\n", string)
  for i in range(len(listo) - 1):
    listo[i] += "\n"
  print(listo)
  for mod in range(column_count):
    i = mod
    while i < len(listo):
      line = listo[i]
      final_string += line
      i += column_count

fi.write(final_string)