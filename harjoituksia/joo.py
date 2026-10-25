kappale = ""

while True:
    nimi = input("lisää kappaleen nimi:")

    if nimi == "stop":
        print(kappale)
        break
    else:
        kappale = kappale + nimi + "->"