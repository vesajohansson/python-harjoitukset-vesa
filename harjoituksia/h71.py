def koordinaatti(_x,_y):
    piste = (_x,_y)
    return piste
#huomaa  alaviiva x  ja normi x erot jotta ei mene sekaisin

x = int(input("anna x koordinaatti:"))
y = int(input("anna y koordinaatti:"))

karttapiste = koordinaatti(x,y)
print("kohde kartalla on koordinaatissa",karttapiste)

#funktio voi palauttaa monikon
