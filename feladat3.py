print("3. feladat")

szam1 = input("Adj meg egy számot: ")
szam2 = input("Adj meg egy másik számot: ")
szam3 = input("Adj meg egy harmadik számot: ")
szam1 = int(szam1)
szam2 = int(szam2)
szam3 = int(szam3)
legnagyobb = max(szam1, szam2, szam3)
print(f"A legnagyobb szám: {legnagyobb}")

lista = []
id = 0
for i in range(3):
    lista.append(int(input(f"Add meg az {i}. számot: ")))
max = lista[0]
for i in range(3):
    if lista[i] > max:
        max = lista[i]
        id = i+1 

print(f"A legnagyobb szám a {max}, ami a(z) {id}. helyen van a listában.")