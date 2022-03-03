name = input("Mi a neved?")
count = int(input("Hányszor írjam ki?"))
print(type(count))
for i in range(count):
    print(i + 1, name)
