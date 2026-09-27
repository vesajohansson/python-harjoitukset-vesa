print ("valitse mitä toimintoa haluat käyttää")




while True:
    valinta = input("A: yhteenlasku, B vähennyslasku, C: Kertolasku, D: jakolasku, Q = LOPETA OHJELA")
    valinta = input("anna valintasi:").upper

    a = float(input("anna ensimmäinen luku"))
    b = float(input("anna toine luku"))


    if valinta == "A":
        print(f"lukujen {a} ja {b} summa on {a+b}") 
    elif valinta == "B":
        print(f"lukujen {a} ja {b} erotus on {a-b}")
    elif valinta == "C":
        print(f"lukujen {a} ja {b} tulo on {a*b}")
    elif valinta == "D":
        print(f"lukujen {a} ja {b} osamäärä on {a/b}")

