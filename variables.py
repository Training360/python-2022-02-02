# Literál - érték
print(5)  # Egész szám
print(100_000)

print(3.14)  # Lebegőpontos literál

print("Hello World")
print('Hello World')

employee_name = "John Doe"  # Snake case
print(employee_name)

age = 30
print(age)
age = 31
print(age)

print("31")

color_of_eye = "blue"
print(color_of_eye)

color_of_eye_of_john = color_of_eye
print(color_of_eye)
print(color_of_eye_of_john)

print(111)
print(employee_name)
print(type(5))  # int = integer

print(type(3.14))  # float - lebegőpontos szám
print(type("Hello"))  # str - string - karakterlánc

age = 32
print(type(age))  # int

age = "harminckettő"
print(age)
print(type(age))  # str

# literálok, változóknak - van típusa - Python típusos nyelv
# változóknál a típus változhat - dinamikusan típusos nyelv

# type hint

salary: int = 200
print(salary)
# salary = "kétszáz"
# print(salary)
