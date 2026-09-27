vastaus = input ("anna luku (tyhjä lopettaa): ")
luku = int(vastaus)
pienin = luku
suurin = luku
while vastaus != "":
    luku = int(vastaus)
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku
    vastaus = input ("anna luku (tyhjä lopettaa): ")
print ("pienin luku:", pienin)
print ("suurin luku:", suurin)