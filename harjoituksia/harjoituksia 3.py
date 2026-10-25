ostos = ""

while True:
    tuote = input("mitä ostit:")

    if tuote == "en mitään":
        print(ostos)
        break
    else:
        ostos = ostos + tuote + ","



        kappale = ""

