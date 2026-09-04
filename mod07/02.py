import random

def heitä_noppaa(tahkot):
    heitto = random.randint(1, tahkot)
    return heitto

maksimiluku = int(input("Anna tahkojen määrä: "))

while True:
    silmäluku = heitä_noppaa(maksimiluku)
    print(silmäluku) 

    if silmäluku == maksimiluku:
        break