print(5 * 6)
print(5 + 6)
print(3 / 2)
print(3 - 2)
print(5 * 6 + 12)
print(1 + 2 * 3)
print((1 + 2) * 3)

print("alma" + "korte")  # konkatenálás

# Mi van ha össze akarsz adni egy str-et és egy int-et
# print("alma" + 5) # TypeError: can only concatenate str (not "int") to str
# Mi van fordítva
# nem működik
# Mi van ha egy stringből ki akarsz vonni egy másikat?
# print("alma" - "korte") # Nem támogatott
# Mi van ha egy stringet megszorzol egy másik stringgel?
# print("a" * "b")
# Mi van, ha egy stringet megszorzol egy int-tel?
print("a" * 5)
print("abc" * 5)

result = 6 * 5 + 2
print(result)

number_of_apples_per_basket = 5
number_of_baskets = 3
number_of_all_apples = number_of_apples_per_basket * number_of_baskets
print(number_of_all_apples)

name = "John Doe"
message = "A name valtozo tipusa: " + str(type(name))
print(message)

print("Az almak szama: " + str(5))

six = 6
print(six)

# kifejezések végrehajtása: kiértékelés

print(len("hello"))
length_of_hello = len("hello")
print(length_of_hello)

# hozzatok létre egy változót, hogy órák száma, hours, értéke legyen először 3
# hozzatok létre egy másik változót, neve: minutes, tartalmazza, hogy - előző változó szorzása 60-nal
# 3 óra az 180 perc - számok helyén használjátok a hours, és minutes változókat

hours = 3
minutes = hours * 60
# print(((str(hours) + " óra az ") + str(minutes)) + " perc")
message = str(hours)
message = message + " óra az "
message = message + str(minutes)
message = message + " perc"
print(message)

number = 5
print(number)
number = number + 3
print(number)

# hozzatok létre egy word nevű változót, és adjátok neki értékül egy nagyon hosszú szót
# számoljátok ki ennek a hosszát
# A xxxcxghedtwireothwe pontosan 13 karakter

word = "eltöredezettségmentesítőtleníttethetetlenségtelenítőtlenkedhetnétek"
# print("A "" + word + "" pontosan " + str(len(word)) + " karakter hosszú.")

print('A "' + word + '" pontosan ' + str(len(word)) + ' karakter hosszú.')

print("A \"" + word + "\" pontosan " + str(len(word)) + " karakter hosszú.")

fruit = "alma"
print('gyumolcs: "' + fruit + '"')
print("gyumolcs: \"" + fruit + "\"")

# print(FRUIT) Python case-sensitive

print(5 // 2)  # ötben a kettő megvan 2-szer
print(5 % 2)  # maradék 1
