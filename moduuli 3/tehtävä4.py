vuosiluku = int(input("anna vuosiluku ="))
if vuosiluku % 4 == 0:
    if vuosiluku % 100 == 0:
        if vuosiluku % 400 ==0:
            print("on karkausvuosi")

        else:
            print("ei ole karkausvuosi")

    else:
        print("on karkausvuosi")
else:
    print("ei ole karkausvuosi")






