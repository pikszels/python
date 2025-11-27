print("\n 6. feladat")

szamok_listaja = []
db = 5

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
print(f"A számok átlaga: {atlag:.1f}")