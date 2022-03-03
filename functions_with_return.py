def calculate_sum(a, b):  # formális paraméter
    return a + b


print(calculate_sum(6, 8))  # aktuális paraméter
# függvényhíváskor az aktuális paraméterek értékeit
# átmásolja a formális paraméterekbe

result = calculate_sum(1, 2)
print(result)

print(6 + calculate_sum(7, 9))

print(calculate_sum(1 + 2, 3 + 4))

print(calculate_sum(len("alma"), calculate_sum(10, 7 + 2)))