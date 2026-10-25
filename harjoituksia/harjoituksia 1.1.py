hinta = int(input("mikä on lipun hinta: "))

määrä = int(input("mikä on lippujen määrä: "))

viikonpäivä = input("mikä on viikonpäivä: ")

if viikonpäivä == "tiistai":
    kokonaishinta = hinta * määrä / 2
else:
    kokonaishinta = määrä * hinta

print(f"kokonaishinta on: {kokonaishinta:.2f}")