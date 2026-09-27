import random
arvotaan = random.randint(1, 10)
arvaus = int(input("arvaa luku (1-10):"))
while arvaus != arvotaan:
    if arvaus > arvotaan:
        print("liian suuri arvaus")
    else:
        print ("liian pieni arvaus")
    arvaus = int(input("arvaa luku (1-10):"))
print ("oikein")