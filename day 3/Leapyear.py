#check if the year entered is a leap or no.

year=int(input("Which year you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year. ")
        else:
            print(f"The year {year} is not a leap year. ")
    else:
        print(f"The year {year} is a leap year. ")
else:
    print(f"The year {year} is not a leap year. ")