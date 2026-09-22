class Julkaisu:
	def __init__(self, nimi):
		self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
	    print(f"Nimi: {self.nimi} kirjoittaja: {self.kirjoittaja} sivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi} Päätoimittaja: {self.päätoimittaja}")

lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
kirja1 = Kirja("Hytti no. 6", "Rosa Liksom", 200)
lehti1.tulosta_tiedot()
kirja1.tulosta_tiedot()
