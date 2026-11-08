import random

def heitto():
    return random.randint(1,6)

#pääohjelma

while True:
    tulos = heitto()
    print(f"luku on: {tulos}")

    if tulos == 6:
        break