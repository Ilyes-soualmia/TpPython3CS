word = input("Please type in a word: ")

counter = 0
for i in word:
    counter += 1

if counter > 1:
    print(f"The length of the word is: {counter}")
else:
    print("Thank you!")
