# Függvény definíciója
def print_employee_data(name, age):  # paraméter nevek == változók
    """Ez a függvény kiírja az alkalmazott nevét és életkorát"""
    # DRY = don't repeat yourself
    print("Az alkalmazott neve:", name)
    print("Az alkalmazott eletkora:", age)
    # függvény végén a paraméterek törlődnek, nincs többé name és age


def print_dog_name(name):
    print("A kutya neve:", name)


def print_sum(a, b):
    print(a + b)


def sum_list(numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)

print_employee_data("John", 10)  # Függvény hívás, paraméter értékek
# átmásolás sorrendben történik: sorrendi kötés
print_employee_data("Jack", 20)
print_employee_data("Jane", 30)
print_dog_name("Morzsi")
print_sum(6, 8)
print("End")

# Kérjétek be a függvényen kívül a két számot
# és a bekért értékekkel hívjátok meg a print_sum függvényt!

value1 = int(input("Adj meg egy számot"))
value2 = int(input("Adj meg egy másik számot!"))
print_sum(value1, value2)

# Írjatok egy sum_list függvényt, ami paraméterül kap egy listát
# És kiírja a konzolra, a listában szereplő számok összegét
numbers = [1, 2, 5, 8]
sum_list(numbers)