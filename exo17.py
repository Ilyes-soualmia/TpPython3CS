#initializing the 2 lists
numbers = []
shoe_sizes = []

#filling the lists using append method
for i in range(1, 6): # 1 to 5
    numbers.append(i)
    shoe_sizes.append(i + 7) # 8 to 12

#displaying the lists
print(f"Numbers list: {numbers}")
print(f"Shoe sizes list: {shoe_sizes}")