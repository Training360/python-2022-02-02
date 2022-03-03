# Írj egy olyan concat_words függvényt, mely paraméterül kap szavak listáját,
# és összefűzi őket, vesszővel elválasztva, és ezzel tér vissza.
# DE! Az utolsó elem után NE legyen vessző.


# ["a", "b", "c"] -> "a,b,c"

# def concat_words(words):
#     result = ""
#     counter = 1
#     for word in words:
#         result += word
#         if counter != len(words):
#             result += ","
#         counter += 1
#     return result

# def concat_words(words):
#     result = ""
#     counter = 1
#     for word in words:
#         if counter != 1:
#             result += ","
#         result += word
#         counter += 1
#     return result

def concat_words(words):
    result = ""
    is_first = True
    for word in words:        
        if not is_first:
            result += ","
        result += word
        is_first = False
    return result


print(concat_words(["a", "bxxx", "xxc", "dyyyyyy"]))