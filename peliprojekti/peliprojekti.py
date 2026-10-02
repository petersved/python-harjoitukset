class Huone:
    def __init__(self, nimi, kerros):
        self.nimi = nimi
        self.kerros = kerros
        self.esineet = []

class Esine:
    def __init__(self, nimi, väri):
        self.nimi = nimi
        self.väri = väri

class Pelaaja:
    def __init__(self, nimi, ikä, sijainti):
        self.nimi = nimi
        self.ikä = ikä
        self.sijainti = sijainti
        self.esineet = []

    def liiku(self, uusi_huone):
        self.sijainti = uusi_huone

    def kerää_esine(self):
        if len(self.sijainti.esineet) > 0:
            esine = self.sijainti.esineet[0]

            self.esineet.append(esine)
        pass



#
#--------Huoneet------------
#

luokka_huone = Huone("Luokkahuone", 6)
hissi = Huone("Hissi", 6)
rappuset = Huone("Rappuset", 6)

#
#-----------ESINEET----------
#

keltainen_avain = Esine("avain", "keltainen")
sininen_avain = Esine("avain", "sininen")




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
