nimet=[]

while True:
    nimi = input("anna nimi: ")

    if nimi == "stop":
        print(f"nimiä annettiin {len(nimet)}")
        break

    nimet.append(nimi)

    print(nimet)
    print(sorted(nimet))