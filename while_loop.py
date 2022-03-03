# Logikai = boolean (bool)
# Két értéke lehet: True, False - literál

are_you_a_boy = True
print(are_you_a_boy)
print(type(are_you_a_boy))

is_17_lower_than_15 = False
print(is_17_lower_than_15)

# Összehasonlító operátorok

result = 10 < 20
print(result)

result = 10 > 20
print(result)

result = 10 >= 20
print(result)

result = 10 == 20
print(result)

result = 10 == 10
print(result)

print("alma" == "korte")

print("alma" == "alma")

# while False:
#     print("Hello ciklus")

# Végtelenciklus
# while True:
#     print("Hello vegtelen")

count = 0
while count < 10:
    print("Hello " + str(count))
    count = count + 1
print("End")

# While ciklus
# Addig kérj be a felhasználótól egy számot, amíg 0-át nem ír be
# Írd ki a bekért szám kétszeresét

# 5
# 10
# 2
# 4
# 0
# 0
