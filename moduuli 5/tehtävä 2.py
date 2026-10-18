luvut = []

vastaus = input("anna luku (tyhjä lopettaa):")

while vastaus != "":
    luvut.append(int(vastaus))
    vastaus = input("anna luku (tyhjä lopettaa):")

luvut.sort(reverse=True)

for luku in luvut [:5]:
    print(luku)