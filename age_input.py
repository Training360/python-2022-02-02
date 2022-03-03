year = int(input("Mikor szulettel?"))
minimum_year = 1900
actual_year = 2022
if year < minimum_year or year > actual_year:
    print("Helytelen szuletesi ev")
else:
    print("Az eletkorod: " + str(actual_year - year))
