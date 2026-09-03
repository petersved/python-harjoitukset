luku = int(input("Anna kokonaisluku:"))

if luku < 2:
    print("Luku ei ole alkuluku")

else: 
    for x in range(2, luku):
        if luku % x == 0:
            print("luku ei ole alkuluku")
            break 

    else:
        print("Luku on alkuluku")