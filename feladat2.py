print("2. feladat")

szam = int(input("Adj meg egy számot: "))
if(szam != 0):
    if szam % 2 == 0:
        print("Páros szám")  
    else:
        print("Páratlan szám")
else:
    print("A szám nem lehet nulla")