luvut = []
luku = input("Anna ensimmäinen luku")

while luku !="":
    luvut.append(float(luku))
    luku = input("Anna seuraava luku")

print("Pienin luku:" ,min(luvut))
print("Suurin luku:" ,max(luvut))

