while True:

    try:
        luku1 = float(input("Anna luku: "))
        luku2 = float(input("Anna toinen luku: "))

        tulos = luku1 / luku2
        print("Tulos:", tulos)
        break

    except ValueError:
        print("Anna numero!")

    except ZeroDivisionError:
        print("Nollalla ei voi jakaa!")