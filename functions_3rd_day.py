# Írjatok egy get_max nevű függvényt,
# aminek paraméterül át lehet adni két
# lebegőpontos számot, és adja vissza a
# kettő közül a nagyobbat!

def get_max(a: float, b: float) -> float:
    if a > b:
        return a
    else:
        return b


print(get_max(3.4, 8.5))
# print(get_max("aaaa", "bbbb")) NE!

# Írjatok egy beszédes print_square függvényt,
# ami paraméterül kap két egész számot.
# Rajzoljon ki egy ekkora téglalapot, csillagokból.

def print_square(width: int, height: int) -> None:
    if width < 0 or height < 0:
        return

    full_row = width * "*"
    print(full_row)

    if height == 1:
        return

    if width == 1:
        center_row = "*"
    else:
        center_row = "*" + (width-2) * " " + "*"
    for i in range(0, height - 2):
        print(center_row)
    # print((center_row + "\n") * (height - 3) + center_row)
    print(full_row)


print_square(1, 6)
print_square(10, 6)
print("10x1-es téglalap")
print_square(10, 1)
print("téglalap negatív értékekkel")
print_square(-7, 1)
print_square(7, -8)
print_square(-7, -8)

def repeat_str(s: str, count: int) -> str:
    # return s * count
    result = ""
    for i in range(0, count):
        result += s
    return result

print(repeat_str("XYZ", 3))

# 7, 5
#
# *******
# *     *
# *     *
# *     *
# *******

# Írjatok egy függvényt, ami paraméterül megkapja
# a szavak listáját, és visszaadja ezeket összefűzve,
# de mindegyiket gondolatjel között.

# ["alma", "korte", "meggy"]
# "-alma--korte--meggy-"


def repeat_words_with_hyphens(words: list) -> str:
    result = ""
    for word in words:
        result += "-" + word + "-"
    return result


print(repeat_words_with_hyphens(["alma", "korte", "meggy"]))