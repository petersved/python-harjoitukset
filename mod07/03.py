def gallonat_litroina(gallonat):
	litroina = gallonat * 3.785
	return litroina

while True:
    gallonat = float(input("Anna gallonamäärä: "))

    if gallonat < 0:
        break

    litrat = gallonat_litroina(gallonat)
    print(f"Gallonat litroina: {litrat}")


