hyttiluokka = input("Haluatko hyttiluokan LUX, A, B vai C? ")
if hyttiluokka == "LUX":
    print("LUX-Luokka on parvekkeellinen hytti yläkannella")
elif hyttiluokka == "A":
    print("A-Luokka on ikkunnallinen hytti autokannen yläpuolella")
elif hyttiluokka == "B":
    print("B-Luokka on ikkunaton hytti autokannen yläpuolella")
elif hyttiluokka == "C":
    print("C-Luokka on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")
