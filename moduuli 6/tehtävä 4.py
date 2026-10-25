import math

while True:
    kokonaisluku = int(input("anna kokonaisluku:"))
    if kokonaisluku < 0:
        print("virheellinen numero")

    elif kokonaisluku > 0:
        print(f"luvun neliöjuuri on {math.sqrt(kokonaisluku)} ")

    else:
        print("ohjelma lopetettu")
        break


 

