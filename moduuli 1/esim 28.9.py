nimet = ["Viivi","Ahmed","Pekka","Olga","Mary"]

nimet2 = ["Matti","Teppo"]

nimet.extend(nimet2)

print(nimet)



if "Matti" in nimet:
    print("matin indeksi on",nimet.index("Matti"))
else:
    print("Mattia ei löytynyt")


värit = ["keltainen","punainen","sininen","musta","violetti"]

lempi = input("anna lempivärisi: ")
if lempi in värit:
    print("löytyy listasta")
else:
    print("lempiväri ei listalla")
    