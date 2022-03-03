print("Gondolj egy számra!")
min = 1
max = 10
answer = "x"
while answer != "e":
    guess = (min + max) // 2
    print("A tippem", guess)
    answer = input("k/e/n?")
    if answer == "k":
        max = guess - 1
    elif answer == "n":
        min = guess + 1
print("A gondolt szam", guess)