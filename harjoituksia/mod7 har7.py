def intentaario(tavarat):
    print("sinulla on seuraavat tavarat")
    for t in tavarat:
        print("- " + t)
    return
    

reppu = ["kartta","juomapullo","kompassi"]
intentaario(reppu)
reppu.append("sämpylä")
intentaario(reppu)

