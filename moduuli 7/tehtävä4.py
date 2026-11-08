def kluvut(luvut):
    summa = 0
    for luku in luvut:
        summa = summa + luku
    return summa

lista = [10, 20, 30, 40]
tulos = kluvut(lista)
print(f"lukujen summa on : {tulos}")



