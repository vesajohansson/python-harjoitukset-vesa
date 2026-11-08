def vaihda():
    kaupunki = "vantaa"
    print("funktiossa lopuksi:"+ kaupunki)
    return

#pääohjelma
kaupunki = "helsinki"
print("kaupungin nimi alunperin:" + kaupunki)
vaihda()
print("globaalin kaupungin nimi:" + kaupunki)

#globaalia muuttujaa voi käyttää funktiossa mutta paikallista (funktion sisällä olevaa)
#muuttujaa ei voi käyttää pääohjelmasta