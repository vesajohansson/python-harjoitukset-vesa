ika = int(input("anna ikäsi"))

if 15 <= ika < 18:
    paino = float(input("anna painosi: "))

if ika >= 18 or ika >=15 and paino >= 55:
    print("lääkkeen käyttö on sallittua.")
else:
    print("lääkkeen käyttö ei ole sallittua.")
    
