print("\n 8. feladat")

lista = [10, 6, 8, 68, 7, 11, 76, 84, 51]
szam = int(input ("Adj meg egy számot: "))
if szam in lista:
    print("A szám megtalálható a listában")
else:print("A szám nincs a listában")
print(f"A számok listája: {lista}")