number = int(input("Enter a number: "))

for i in range(-number, number + 1):
    if i == 0:
        continue
    print(i)