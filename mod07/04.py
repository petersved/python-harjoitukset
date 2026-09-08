def lukujen_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

luvut = [2, 5, 20, 50]
summa = lukujen_summa(luvut)

print(summa)
