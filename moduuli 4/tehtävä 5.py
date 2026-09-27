oikea_tunnus = "väsyttää"
oikea_salasana = "helvetisti"
yritykset = 1
tunnus = input ("käyttäjätunnus: ")
salasana = input ("salasana: ")
while (tunnus != oikea_tunnus or salasana != oikea_salasana) and yritykset < 5:
    yritykset = yritykset +1
    tunnus = input("käyttäjätunnus: ")
    salasana = input ("salasana: ")
if tunnus == oikea_tunnus and salasana == oikea_salasana:
    print ("tervetuloa")
else:
    print ("pääsy evätty")