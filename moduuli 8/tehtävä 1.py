#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma
#tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi
#kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
#Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on
#ensimmäinen talvikuukausi.

vuodenajat = ("talvi","talvi","kevät","kevät","kevät","kesä","kesä","kesä","syksy","syksy","syksy","talvi")


while True:
    kuukausi =int(input("anna kuukauden numero (0 lopettaa):"))

    if kuukausi == 0:
        break

    print(vuodenajat[kuukausi -1])
