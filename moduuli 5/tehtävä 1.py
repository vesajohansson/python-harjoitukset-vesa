import random

noppia = int(input("montako noppaa heitetään"))

summa = 0

for i in range(noppia):
    heitto = random.randint(1,6)
    summa = summa + heitto
print(f"yhteistulos on {summa}")
