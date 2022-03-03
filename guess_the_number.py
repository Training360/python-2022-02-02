print("Gondolj egy számra!")
min_guess = 1
max_quess = 10
answer = "x"
guess = 5
while answer != "e":
    guess = (min_guess + max_quess) // 2
    print("A tippem", guess)
    answer = input("k/e/n?")
    if answer == "k":
        max_quess = guess - 1
    elif answer == "n":
        min_guess = guess + 1
print("A gondolt szam", guess)
