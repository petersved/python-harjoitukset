leiviskät = float(input("Anna leiviskät:"))
naulat = float(input("Anna naulat:"))
luodit = float(input("Anna luodit:"))

luoti_grammoina = 13.3
naula_grammoina = 32 * luoti_grammoina
leiviskä_grammoina = 20 * naula_grammoina

massa = (leiviskät * leiviskä_grammoina) + (naulat * naula_grammoina) + (luodit * luoti_grammoina)
kilogrammat = int(massa // 1000)
grammat = massa % 1000

print("Massa nykymittojen mukaan:" )
print(kilogrammat, "kilogrammaa ja", grammat, "grammaa")
