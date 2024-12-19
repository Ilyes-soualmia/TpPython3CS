user_list = []

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break
    else:
        user_list.append(number)
        print(user_list)
        print(sorted(user_list))