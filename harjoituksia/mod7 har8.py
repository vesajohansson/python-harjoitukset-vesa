def tervehdi(nimi):
    print("morjens," + nimi)
    return

def tervehdi_monesti(nimi, kerrat):
    while kerrat > 0:
        tervehdi(nimi)
        kerrat -= 1
    return

#pääohjelam
tervehdi_monesti("vesa",3)

