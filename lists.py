names = []
print(names)

names.append("John Doe")
print(names)

names.append("Jack Doe")
print(names)

names.append("Jane Doe")
print(names)

print(names[0])

print(names[0:2])
print(names[::-1])

names[1] = "Jack Smith"
print(names)

names.remove("Jack Smith")
print(names)

numbers = [1, 2, 3]
print(numbers)

employee = ["John Doe", 20]
print(employee)
print(employee[0])
print(employee[1])

print(len(employee))

print(names)
print("John Doe" in names)
print("Jane Smith" in names)

for name in names:
    print(name)

# Írj egy olyan függvényt, mely paraméterül kap egy listát amibe nevek vannak,
# és visszaad egy másik listát. De a másik listában csak
# azok a nevek legyenek benne, akik John-nal kezdődnek.
# Szűrés - filter

# ["John Smith", "Jane Smith", "Jack Doe", "John Doe"]
# ["John Smith", "John Doe"]

def filter_johns(names: list) -> list:
    result = []
    for name in names:
        if "John" in name and name.index("John") == 0:
            result.append(name)
    return result


print(filter_johns(["John Smith", "Jane Smith", "Jack Doe", "John Doe", "Jack John Doe"]))
