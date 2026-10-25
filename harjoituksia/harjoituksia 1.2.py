tunnit = int(input("montako tuntia:"))

tuntihinta = int(input("mikä on tuntihinta:"))

päivä = input("mikä viikonpäivä:")

if päivä == "lauantai":
    pysäköintimaksu = tuntihinta * tunnit * 1.5
elif päivä == "sunnuntai":
    pysäköintimaksu = tuntihinta * tunnit * 2

else:
    pysäköintimaksu = tuntihinta * tunnit

print(f"pysäköintimaksusi on: {pysäköintimaksu:.2f}")
