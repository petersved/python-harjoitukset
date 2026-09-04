import random

def heitä_noppaa():
    heitto = random.randint(1, 6)
    return heitto

while True:
    silmäluku = heitä_noppaa()
    print(silmäluku)

    if silmäluku == 6:
        break
