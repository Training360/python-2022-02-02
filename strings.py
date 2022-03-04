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
def count_letters(word: str) -> int:
    counter = 0
    for c in word:
        if c == "a":
            counter += 1
    return counter


print(count_letters("almafa"))

## Írj egy olyan függvényt, amely paraméterül kap
## egy szót, és megszámolja, hogy hány magánhangzó van benne

c = "a"
print(c in "aeiou")
print(c in "éíóöőüű")

def count_vowels(word: str) -> int:
    count = 0
    for c in word:
        if c in "aeiou":
            count += 1
    return count


print(count_vowels("karakterlap"))

## Írj egy függvényt, mely kap egy szót, és visszaadja
## a benne szereplő betűket *-gal elválasztva egy stringben!
## Az utolsó karakter után ne legyen *


def concat_letters_with_spec_characters(word: str) -> str:
    result = ""
    for c in word:
        if c != " ":
            result += c + "*"
    return result[:-1]

print(concat_letters_with_spec_characters("alma"))
print(concat_letters_with_spec_characters("alma korte"))

## xyz -> x*y*z

## Írj egy függvényt, amely visszaadja, hogy a paraméterként
## átadott szó megfordítva is ugyanaz-e

def is_reverse_equal(word: str) -> bool:
    return word == word[::-1]

print(is_reverse_equal("anna"))
print(is_reverse_equal("indul a gorog aludni"))
print(is_reverse_equal("indulagorogaludni"))

## anna -> True
## indul a gorog aludni -> False
## indulagorogaludni -> True

## Írj egy függvényt, ami a paraméterként átadott szóból
## kiveszi a space-eket, és azt adja vissza.

def kill_spaces(word: str) -> str:
    result = ""
    for c in word:
        if c != " ":
            result += c
    return result


print(kill_spaces("alma korte barack"))


name = "John Doe"
print(name.index("Doe"))

print(name.index("J"))
# print(name.index("x"))

print("x" in name)

print("alma korte barack".split())

fruits = "alma korte barack"
fruits_list = fruits.split()
print(fruits_list)

for n in fruits_list:
    print(n)

names = "john doe jack doe jane doe"
print(names.upper()[4:15].split())

ip = "192.168.0.1"
print(ip.split("."))
for number in ip.split("."):
    print(int(number))
