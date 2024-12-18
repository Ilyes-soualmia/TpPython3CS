numbers = [1,2,3,4,5]

while True :
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = int(input("Enter the element to append: "))
        numbers.append(element)
    elif choice == 2:
        element = int(input("Enter the element to insert: "))
        position = int(input("Enter the position to insert: "))
        numbers.insert(position, element)
    elif choice == 3:
        element = numbers.pop()
        print(f"Element popped: {element}")
    elif choice == 4:
        element = int(input("Enter the element to remove: "))
        numbers.remove(element)
    elif choice == 5:
        break
    else:
        print("Invalid choice")

    print(f"Numbers list: {numbers}")

print("Bye!")
