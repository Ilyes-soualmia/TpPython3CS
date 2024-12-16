numbers = [1, 2, 3, 4, 5]

while True:
    while True:
        index = input("Enter index (-1 to quit): ")
        if (index.isdigit()) or (index == "-1"):
            index = int(index)
            break
        else:
            print("Invalid index")

    if index == -1:
        break
    if index +1 > len(numbers) or index < 0:
        print("Invalid input...")
    else:
        value = int(input("Entre a value: "))
        numbers[index] = value

print(numbers)