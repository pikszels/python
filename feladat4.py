print("4. feladat")

n = input("Adj meg egy számot: ")
n = int(n)
print(f"A számok 1-től {n}-ig:")
for i in range(1, n + 1):
    print(i, end = " ")