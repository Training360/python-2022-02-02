# Kérd be a felhasználótól, hogy hány számot szeretne megadni
# 3
# Kérjél be tőle pont annyi számot, mint amit az előbb megadott
# Összegezzük a felhasználó által megadott CSAK pozitív számokat
# 3
# 4
# -2
# Eredmeny: 7

# Szorgalmi: egy másik program addig kérje be a számokat, míg nullát nem kap, és mindig
# írja ki a részösszeget!

count = int(input("Hany szamot szeretnel megadni?"))
sum = 0
for i in range(count):
    number = int(input("Add meg a " + str(i + 1) + ". szamot"))
    print("A megadott szam:", number)
    if number > 0:
        sum += number
        print("Reszosszeg:", sum)
print("Vegso osszeg:", sum)