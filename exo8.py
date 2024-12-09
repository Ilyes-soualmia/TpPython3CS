number = int(input("Enter a number: "))

if number % 3 == 0:
    if number % 5 == 0:
        print("FizzBuzz") #divisible by both 3 and 5
    else:
        print("Fizz") #divisible by 3 but not by 5
elif number % 5 == 0:
    print("Buzz") #divisible by 5 only (not by 3)
