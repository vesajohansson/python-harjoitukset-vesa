ika = input(input("anna ikäsi: "))

if ika >= 65:
    print("olet eläkkeellä.")
elif ika >= 18:
    print("olet työikäinen.")
elif ika <= 7:
    print("olet kouluikäinen")
else:
    print("olet pienil lapsi. ")
