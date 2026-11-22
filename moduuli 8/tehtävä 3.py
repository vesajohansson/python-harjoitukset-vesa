lentoasemat={}

while True:
   valinta= input("1 = uusi, 2 = haku, 3 = lopeta:")
   if valinta == "3":
      print("ohjelma lopetettu")
      break
   elif valinta == "1":
      koodi = input("anna icao koodi:")
      nimi = input("anna aseman nimi:")
      lentoasemat[koodi] = nimi

   elif valinta == "2":
      koodi = input("anna icao koodi:")
      print(lentoasemat[koodi])
