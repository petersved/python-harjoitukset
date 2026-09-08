def hahmo():
    print("Pelin hahmo: Haaland")

def kieli():
    print("Peliä voi pelata vain suomeksi")

def lisää_reppuun(reppu):
    esine = input("Mitä haluat lisätä reppuun?: ")
    reppu.append(esine)

def repun_sisältö(reppu):
    print("Reppusi sisältö: ")
    for esine in reppu:
        print(esine)

nimi = input("Mikä on nimesi?: ")
ikä = int(input("Minkä ikäinen olet?: "))

if ikä < 12:
    print("Olet liian nuori pelaamaan. ")
else:
    print("Tervetuloa pelaamaan:", nimi)

    reppu = []
    komento = ""

    while komento != "Lopeta":
        print("Päävalikko:")
        print("Hahmo")
        print("Kieli")
        print("Reppu")
        print("Lisää esineitä")
        print("Lopeta")

        komento = input("Anna komento jatkaaksesi: ")

        if komento == "Hahmo":
            hahmo()

        elif komento == "Reppu":
            repun_sisältö(reppu)
            

        elif komento == "Kieli":
            kieli()

        elif komento == "Lisää esineitä":
            lisää_reppuun(reppu)

    print("Peli lopetetaan")
