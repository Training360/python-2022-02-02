name = "John Doe"

print(name.upper())
print(name)
print(name.lower())
print(name)

print(name[0])

# Immutable - módosíthatatlan
name.upper()
print(name)

name = name.lower()
print(name)

for c in name:
    print(c)

print(len(name))

# Szeletelés = slicing
print(name[2:6]) # substring
print(name[2:])
print(name[:6])
print(name[0:7:2])
print(name[::-1])

print(name[0:3] + name[4:6])

word = "arvizturotukorfurogep"
print(word[:-1])

filename = "doomdoom.exe"
print(filename[-3:])
ip = "192.168.0.1"
print(ip[-1:])

print("alma" == "alma")
print("alma" == "korte")

print("alma" > "korte")

print("a" in "alma")
print("al" in "alma")
print("la" in "alma")
print("alma" in "alma")
print("b" in "alma")

## Írj egy olyan függvényt, ami megszámolja, hogy
## hány darab a betű van egy szóban!

## Írj egy olyan függvényt, amely paraméterül kap
## egy szót, és megszámolja, hogy hány magánhangzó van benne

c = "a"
print(c in "aeiou")
print(c in "éíóöőüű")

## Írj egy függvényt, mely kap egy szót, és visszaadja
## a benne szereplő betűket *-gal elválasztva egy stringben!
## Az utolsó karakter után ne legyen *

## xyz -> x*y*z

## Írj egy függvényt, amely visszaadja, hogy a paraméterként
## átadott szó megfordítva is ugyanaz-e

## anna -> True
## indul a gorog aludni -> False
## indulagorogaludni -> True

## Írj egy függvényt, ami a paraméterként átadott szóból
## kiveszi a space-eket, és azt adja vissza.
