def neliosumma(eka, toka):
    ns = eka**2 + toka**2
    return ns

luku1 = float(input("anna ensimmäinen luku:"))
luku2= float(input("anna toinen luku:"))
tulos = neliosumma(luku1,luku2)
print(f"lukujen {luku1:.2} ja {luku2:.2} neliosumma on {tulos:.2f}.")