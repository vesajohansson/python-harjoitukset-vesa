import random

def heitto(tahkot):
    return random.randint(1,tahkot)

#pääohjelma

tahkot = int(input("anna tahkojen määrä:"))
while True:
    tulos =heitto(tahkot)
    print(f"luku on: {tulos}")

    if tulos == tahkot:
        break