name = input("Add meg a neved!")
# if len(name) == 0:
#     print("Nem jo, ne adj meg ures nevet!")

if name == "":
    print("Nem jo, ne adj meg ures nevet!")

age_input = input("Add meg az eletkorod!")
age = int(age_input)
if age < 20:
    print("Tul fiatal vagy")
    print(2020 - age)

# if True:
#     print("Hello World")
#     print("Hello Python")
# print("End")