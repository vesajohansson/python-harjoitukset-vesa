import math

def tiedot(halkaisija, hinta):
    halkaisija = halkaisija / 100
    säde = halkaisija / 2
    pinta_ala = math.pi * säde **2
    yksikköhinta = hinta / pinta_ala
    return yksikköhinta

hinta1 = float(input("1 pitsan hinta: "))
halkaisija1 = float(input("1 pitsan halkaisija: "))
hinta2 = float(input("2 pitsan hinta: "))
halkaisija2 = float(input("2 pitsan halkaisija: "))

yh1 = tiedot(halkaisija1, hinta1)
yh2 = tiedot(halkaisija2, hinta2)

if yh1 < yh2 :
    print(" 1 pitsa on parempi vastine")

else:
    print(" 2 pitsa on parempi vastine")