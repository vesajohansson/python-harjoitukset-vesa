lista = []

while True:
    luku = int(input("anna luku: "))

    if luku == 0:
        break

    lista.append(luku)

    print(lista)
    print(sorted(lista))