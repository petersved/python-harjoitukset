class Auto:
	def __init__(self, rekisteritunnus, huippunopeus):
		self.rekisteritunnus = rekisteritunnus
		self.huippunopeus = huippunopeus
		self.nopeus = 0
		self.kuljettu_matka = 2000

	def kiihdytä(self, muutos):
		self.nopeus += muutos

		if self.nopeus > self.huippunopeus:
			self.nopeus = self.huippunopeus
		elif self.nopeus < 0:
			self.nopeus = 0

	def kulje(self, tuntimäärä):
		self.kuljettu_matka += tuntimäärä * self.nopeus


auto = Auto("ABC-123", 142)

print("Rekisteritunnus:", auto.rekisteritunnus)
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Tämänhetkinen nopeus: {auto.nopeus} km/h")
print(f"Kuljettu matka: {auto.kuljettu_matka} km")


auto.kiihdytä(60)
auto.kulje(1.5)

print(f"Autolla kuljettu matka ajon jälkeen: {auto.kuljettu_matka} km")
