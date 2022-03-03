# Hozz letre egy last_functions.py állományt, ebben egy
# table függvényt, ami kiírja a szorzótáblát!

def table():
    for i in range(1, 11):
        for j in range(1, 11):
            result = i * j
            if result < 10:
                print(" ", end="")
            print(result, end=" ")
        print("")


table()

# Hozz létre egy digits függvényt, ami kiírja a
# paraméterül adott szám számjegyeit!

# 8673432
def szamjegyek(szam):
    while szam > 10:
        maradek = szam % 10
        print(maradek)
        szam = szam // 10
    print(szam)

szamjegyek(8673432)