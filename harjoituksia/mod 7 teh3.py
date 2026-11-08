#määritellään funktio ennen kun sitä voi kutsua

def tervehdi(tervehdys, kerrat):
    for i in range(kerrat):
        print("tervehdys " + str(i+1) + ". kerran")
        # f tyyli siistimpi
        print(f"hyvää päivää {i+1}. kerran")
    return

#pääohjelma

print("testataan tervehdys funktiota")
tervehdi("moi", 3)
print("testataan varmistukseksi")
tervehdi("hello",5)

