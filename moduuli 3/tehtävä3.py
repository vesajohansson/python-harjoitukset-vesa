sukupuolesi = input("mikä on sukupuolesi? =")
hemo = int(input("mikä on hemogobiinisi (g/l) ? ="))

if sukupuolesi == "nainen":
    if hemo <117:
        print("hemoglobiini alhainen")

    elif 117 <= hemo <=175:
        print("hemoglobiini normaali")

    else:
        print("hemoglobiini korkea")
if sukupuolesi == "mies":
    if hemo <134:
        print("hemoglobiini alhainen")
    elif 134 <= hemo <=195:
        print("hemoglobiini normaali")
    else:
        print("hemoglobiini korkea")




