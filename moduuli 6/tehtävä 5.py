tarina = ""

while True:
    sana = input("anna sana lisättäväksi tarinaan:")

    if sana == "loppu":
        print(tarina)
        break
    else:
        tarina = tarina + sana + " "
