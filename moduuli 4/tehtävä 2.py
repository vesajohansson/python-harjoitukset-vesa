tuumat = float(input("anna tuumumäärä (negatiivinen lopettaa): "))
while tuumat >= 0:
    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {senttimetrit} senttimetriä")
    tuumat = float(input("anna tuumamäärä (negatiivinen lopettaa): "))
print ("ohjelma lopetettu")