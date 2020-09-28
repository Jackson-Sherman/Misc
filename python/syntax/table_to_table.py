import io
import re
import math

strings = ["""   S → NP VP
  AP → (AdvP) A
  VP → V NP
  NP → (D) (AP*) N (PP*) (S)
AdvP → (AdvP) Adv
  VP → V NP NP
   S → (Comp) S
  VP → V 
  VP → V NP PP
  PP →  P NP

   X → X Conj X



""", """   D → a
 Adv → very
   N → coats
   D → that
 Adv → extremely
   N → dieting
   D → the
   V → have
   N → effects
   D → three
   V → prefer
   N → grass
   P → in
   V → investigate
   N → Gus
   P → from
   V → cost
   N → headphones
   P → with
   V → found
   N → I
   P → about
   V → coats
   N → intellect
   P → of
   V → warns
   N → K-mart
   P → on
   V → found
   N → Louisiana
   P → for
   V → told
   N → manager
   A → fuzzy
Conj → and
   N → someone
   A → dry
Comp → that
   N → sugar
   A → cunning
   N → alpacas
   N → treble
   A → piercing
   N → Argentina
   N → research
   A → much
   N → bag
   N → passcode
   A → dieting
   N → bucks
   N → Shawn
 Adv → too
   N → chips
   N → vault"""]
fi = open("output.txt","x")
final_string = ""
for string in strings:
  listo = re.split("\n", string)
  for i in range(len(listo) - 1):
    listo[i] += "\n"
  print(listo)
  for mod in (0,1,2):
    i = mod
    while i < len(listo):
      line = listo[i]
      final_string += line
      i += 3

fi.write(final_string)


            
        