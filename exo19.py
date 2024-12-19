wordsList = []
counter = 0

while True:
    word = input("Enter a word: ")
    if word in wordsList:
        print(counter)
        break
    else:
        wordsList.append(word)
        counter += 1