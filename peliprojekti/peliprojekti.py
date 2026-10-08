
#
#------LUODAAN LUOKAT---------
#

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
            
            if esine.väri == "keltainen":
                print("Löysit keltaisen avaimen!")
            
            elif esine.väri == "sininen":
                print("Löysit sinisen avaimen!")

        else:
            print("Täällä ei ole esinettä.")

    def näytä_reppu(self):
        if len(self.esineet) == 0:
            print("Reppusi on tyhjä")

        else:
            print("Repussasi on:")
            for esine in self.esineet:
                print("-", esine.nimi, esine.väri)

    def tarkista_avain(self, väri):
        for esine in self.esineet:

            if esine.nimi == "avain" and esine.väri == väri:
                return True

        return False

    def näytä_sijainti(self):
        print()
        print("Olet huoneesse: ", self.sijainti.nimi)
        print("Kerroksessa: ", self.sijainti.kerros)
        print()


#
#--------Huoneet------------
#

luokkahuone = Huone("Luokkahuone", 6)
hissi = Huone("Hissi", 6)
rappuset = Huone("Rappuset", 6)
a_siiven_vessa = Huone("A-siiven vessa", 6)
b_siiven_vessa = Huone("B-siiven vessa", 6)
toinen_kerros = Huone("2. kerros", 2)
opettajienhuone = Huone("Opettajienhuone", 6)

#
#-----------ESINEET----------
#

keltainen_avain = Esine("avain", "keltainen")
sininen_avain = Esine("avain", "sininen")

#---ESINEIDEN SIJOITUS

a_siiven_vessa.esineet.append(keltainen_avain)
b_siiven_vessa.esineet.append(sininen_avain)


#
#---------Pelaajan tiedot--------
#
# Alle 12 vuotiaat ei voi pelata peliä.

nimi = input("Mikä on nimesi?: ")
ikä = int(input("Minkä ikäinen olet?: "))

if ikä < 12:
    print("\nOlet liian nuori pelaamaan. ")
    exit()

else:
    print("\nTervetuloa pelaamaan:", nimi)

    pelaaja = Pelaaja(nimi, ikä, luokkahuone)


#
#--------Päävalikko--------
#
    
    while True:
        
        print("\n          Päävalikko\n")
        print("1 - Kieli")
        print("2 - Aloita peli")
        print("3 - Lopeta peli")

        valinta = input("> ")



        if valinta == "1":

            print()
            print("Peliä voi pelata vain suomeksi.")


        elif valinta == "2":

            print("\nAloitetaan peli!\n")
            print("Olet nukahtanut luokkaan ja jäänyt kouluun jumiin.")
            print("Tehtäväsi on päästä pois huomaamatta\n")

        #
        #----------- 
        #
            
            while True:

                pelaaja.näytä_sijainti()

                
                print("1 - Mene A-siiven vessaan")
                print("2 - Mene B-siiven vessaan")
                print("3 - Mene rappusiin")
                print("4 - Mene hissiin")
                print("5 - Mene opettajien huoneeseen")
                print("6 - Kerää esine")
                print("7 - Näytä reppu")
                print("8 - Avaa luokkahuoneen ikkuna")
                print("9 - Kysy apua")
                print("10 - Sammuta valot")
                print("11 - Lopeta peli")

                toiminto = input("> ")


                if toiminto == "1":

                    pelaaja.liiku(a_siiven_vessa)
                    print("\nMenit A-siiven vessaan. ")


                elif toiminto == "2":

                    pelaaja.liiku(b_siiven_vessa)
                    print("\nMenit B-siiven vessaan. ")

                elif toiminto == "3":

                    if pelaaja.tarkista_avain("keltainen"):

                        print("\nSinulla on keltainen avain, pääset rappusiin! ")

                        pelaaja.liiku(toinen_kerros) 

                        print("\nSaavuit 2. kerrokseen ja pääsit ulos\n")
                        print("Voitit pelin! ")

                        break

                    else: 
                        print("\nSinulla ei ole keltaista avainta.")
                        print("Et pääse rappusiin.")


                elif toiminto == "4":

                    if pelaaja.tarkista_avain("sininen"):

                        print("\nSinulla on sininen avain, pääset hissiin!")

                        pelaaja.liiku(toinen_kerros)

                        print("\nSaavuit 2. kerrokseen ja pääsit ulos\n")
                        print("Voitit pelin! ")

                    else:
                        print("\nSinulla ei ole sinistä avainta. ")
                        print("Et pääse hissiin. ")


                elif toiminto == "5":

                    pelaaja.liiku(opettajienhuone)

                    print("\nMenit opettajienhuoneeseen")
                    print("\nJäit kiinni ja hävisit pelin")

                    exit()

                
                elif toiminto == "6":

                    pelaaja.kerää_esine()

                
                elif toiminto == "7":

                    pelaaja.näytä_reppu()

                
                elif toiminto == "8":

                    if pelaaja.sijainti == luokkahuone:

                        print("\nAvasit luokkahuoneen ikkunan")
                        print("Ikkunan takaa löytyi tikapuut joita pitkin kiivetä alas\n")
                        print("\n Voitit pelin! ")

                        break

                    else:
                        print("\nTässä huoneessa ei ole ikkunaa. ")



                elif toiminto == "9":

                    print("\nPyysit apua ja jäit kiinni")
                    print("\n Hävisit pelin." )

                    exit()

                elif toiminto == "10":

                    print("\nsammutit valot ja siten säästit energiaa!")


                elif toiminto == "11":

                    print("\n Peli lopetetaan \n")

                    break

                else:

                    print("\nValitse 1, 2, 3, 4, 5, 6, 7, 8, 9 tai 10\n")




        elif valinta == "3":

            print("Peli lopetetaan")

            exit()

        else: 

            print("Valitse 1, 2 tai 3. ")
