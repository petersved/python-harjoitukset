nimi = input("Mikä on nimesi?: ")
ikä = int(input("Minkä ikäinen olet?: "))

if ikä < 12:
    print("Olet liian nuori pelaamaan. ")
else:
    print("Tervetuloa pelaamaan:", nimi)

    komento = ""

    while komento != "Lopeta":
        print("Päävalikko:")
        print("Hahmo")
        print("Kieli")
        print("Reppu")
        print("Lopeta")

        komento = input("Anna komento jatkaaksesi: ")

        if komento == "Hahmo":
            print("Pelin hahmo: Haaland")

        elif komento == "Reppu":
            print("Reppusi on tyhjä")

        elif komento == "Kieli":
            print("Peliä voi pelata vain suomeksi")

    print("Peli lopetetaan")
    


    
