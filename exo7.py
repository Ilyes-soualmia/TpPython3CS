#LEAP YEAR

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 != 0:
            leap = True
        else:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
    else:
        leap = False
    
    return leap

year = int(input("Please type in a year: "))

if is_leap(year):
    print(year, " is a leap year.")
else:
    print(year, " is not a leap year.")
