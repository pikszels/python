import random

print("9. feladat")

#lista = [10,2,33,14,51,68,47,18,99,15,71,26,24,64,87,23,17,44,82,21]
lista = random.sample(range(1, 101), 20)
lista2 = []
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista2.append(lista[i])
print(f"A számok listája: {lista}")
print(f"A páros számok listája:{lista2}")