lista = []

while True:

    luku = float(input("anna luku: "))

    if luku == -1:
        print(f"lukuja annettiin {len(lista)}")
        print(max(lista))
        print(min(lista))
        break

    lista.append(luku)

    print(lista)
    print(sorted(lista,reverse=True))

        