#1
""" print("1. feladat")
szam1 = input("Adj meg egy számot: ")
szam2 = input("Adj meg egy másik számot: ")
szam1 = int(szam1)
szam2 = int(szam2)
print(f"A két szám összege: {szam1 + szam2}") """

#2
""" print("2. feladat")
szam = int(input("Adj meg egy számot: "))
if(szam != 0):
    if szam % 2 == 0:
        print("Páros szám")  
    else:
        print("Páratlan szám")
else:
    print("A szám nem lehet nulla") """

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

""" lista = []
id = 0
for i in range(3):
    lista.append(int(input(f"Add meg az {i}. számot: ")))
max = lista[0]
for i in range(3):
    if lista[i] > max:
        max = lista[i]
        id = i+1 

print(f"A legnagyobb szám a {max}, ami a(z) {id}. helyen van a listában.")"""

#4
""" print("\n 4. feladat")
n = input("Adj meg egy számot: ")
n = int(n)
print(f"A számok 1-től {n}-ig:")
for i in range(1, n + 1):
    print(i, end = " ") """


#5
""" print("\n 5. feladat")
szam = int(input("Kérem N értékét: "))
ossz = 0
for i in range(1, szam + 1):
    ossz = ossz + i
print(f"A számok összege: {ossz}") """

#6
""" print("\n 6. feladat")

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

#7
""" print("\n 7. feladat")
szlista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
legnagyobb = max(szlista)
legkisebb = min(szlista)
print(f"A legnagyobb elem: {legnagyobb}")
print(f"A legkisebb elem: {legkisebb}") """

#8
""" print("\n 8. feladat")
lista = [10, 6, 8, 68, 7, 11, 76, 84, 51]
szam = int(input ("Adj meg egy számot: "))
if szam in lista:
    print("A szám megtalálható a listában")
else:print("A szám nincs a listában")
print(f"A számok listája: {lista}") """

#9
""" lista = [1,2,3,4,5,6,7,8,9]
lista2 = []
for i in range(len(lista)):
    print("hablabda") """