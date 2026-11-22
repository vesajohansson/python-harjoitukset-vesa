puhelinluettelo = {"viivi" :"111","ahmed" : "222","pekka" : "333"}

print(puhelinluettelo)
#arvon muuttaminen
puhelinluettelo["pekka"] ="444"

print(puhelinluettelo)
#numeron arvon lisäys
puhelinluettelo["olga"] ="555"

print(puhelinluettelo)

#arvon poistaminen
del puhelinluettelo["viivi"]

print(puhelinluettelo)
#tulostaa avaimet
for numero in puhelinluettelo:
    print(numero)
#tulostaa arvot
for numero in puhelinluettelo.values():
    print(numero)
#tulostetaan molemmat/käytetään koko alkiota
for avain, numero in puhelinluettelo.items():
    print(f"{avain}n puhelinnumero on {numero}")