def kluvut(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset
        
    

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
tulos = kluvut(lista)
print(f"alkuperäinen lista on : {lista}")
print(f"parilliset on : {tulos}")