laji = input("Oletko ihminen, tonttu vai robotti?")
ikä = int(input("minkä ikäinen olet?"))

print("voit tilata:")

print("- kahvin")

if laji == "ihminen" and ikä >= 18:
    print("- viinin")

if laji == "tonttu" and ikä >= 100:
    print("- oluen")

if laji == "robotti":
    print ("- öljyä")


