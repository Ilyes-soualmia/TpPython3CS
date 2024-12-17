number = int(input("Enter a number: "))

while number < 1:
    print("wrong input")
    number = int(input("Enter a POSITIVE number: "))


a=1
b=1

while True:
    print(f"{a} * {b} = {a * b}")
    if(a * (b+1)) <= number:
        b+=1
    elif (a+1) <= number:
        a+=1
        b = 1
    else:
        break

