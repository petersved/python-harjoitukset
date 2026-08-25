vuosiluku = int(input("Anna vuosiluku:"))

if vuosiluku % 400 == 0:
    print(f"{vuosiluku} On karkausvuosi")
elif vuosiluku % 100 == 0:
    print(f"{vuosiluku} Ei ole karkausvuosi")
elif vuosiluku % 4 == 0:
    print(f"{vuosiluku} On karkausvuosi")
else:
    print(f"{vuosiluku} Ei ole karkausvuosi")