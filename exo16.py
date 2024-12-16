numbers = [1, 2, 3, 4, 5]

while True:
    index = int(input("Enter index (-1 to quit): "))
    if index == -1:
        break
    else:
        while True:
            if index < 0 or index >= len(numbers):
                print("Invalid index")
                index = int(input("Enter index (-1 to quit): "))
            else:
                break

    value = int(input("Enter new value: "))
    numbers[index] = value

print(numbers)