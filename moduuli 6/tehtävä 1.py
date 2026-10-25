
tuntipalkka = float(input("paljonko on tuntipalkkasi:"))

tunnit = float(input("tehdyt tunnit: "))

viikonpäivä = input("viikonpäivä: ")

if viikonpäivä == "sunnuntai":
    palkka = tuntipalkka * 2 * tunnit
else:
    palkka = tuntipalkka * tunnit

print(f"päivän palkkasi on  {palkka:.2f} euroa")
    

