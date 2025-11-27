#1
""" print("1. feladat")
szam1 = input("Adj meg egy számot: ")
szam2 = input("Adj meg egy másik számot: ")
szam1 = int(szam1)
szam2 = int(szam2)
print(f"A két szám összege: {szam1 + szam2}") """

#2
""" print("2. feladat")
szam = input("Adj meg egy számot: ")
if int(szam) % 2 == 0:
    print("Páros szám")
else:
    print("Páratlan szám") """

#3
""" print("3. feladat")
szam1 = input("Adj meg egy számot: ")
szam2 = input("Adj meg egy másik számot: ")
szam3 = input("Adj meg egy harmadik számot: ")
szam1 = int(szam1)
szam2 = int(szam2)
szam3 = int(szam3)
legnagyobb = max(szam1, szam2, szam3)
print(f"A legnagyobb szám: {legnagyobb}") """

#4
""" print("\n 4. feladat")
n = input("Adj meg egy számot: ")
n = int(n)
print(f"A számok 1-től {n}-ig:")
for i in range(1, n + 1):
    print(i, end = " ") """

#5
""" print("\n 5. feladat")

szamok_listaja = []
db = 5

# Kérj be 5 számot egy ciklus segítségével
for i in range(db):
    while True:
        try:
            szam_input = float(input(f"Kérlek, add meg a(z) {i + 1}. számot: "))
            szamok_listaja.append(szam_input)
            break
        except ValueError:
            print("Hibás bevitel. Kérlek, érvényes számot adj meg.")

osszeg = sum(szamok_listaja)
atlag = osszeg / len(szamok_listaja)
print(f"A számok átlaga: {atlag:.1f}") """