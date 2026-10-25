kokonaisluku = int(input("anna kokonaisluku:"))

if kokonaisluku % 5 == 0 and kokonaisluku % 3 == 0:
    print("jaollinen molemmilla luvuilla")
elif kokonaisluku % 5 == 0:
    print("viidellä jaollinen")
elif kokonaisluku % 3 == 0:
    print("jaollinen kolmella")
