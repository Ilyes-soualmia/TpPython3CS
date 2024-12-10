nbrOfStars = 30
word = input("Enter a word: ")

nbrOfStars = nbrOfStars - len(word)
if nbrOfStars % 2 == 0:
    nbrOfStars = nbrOfStars // 2
    print("*" * nbrOfStars + word + "*" * nbrOfStars)
else:
    nbrOfStars = nbrOfStars // 2
    print("*" * nbrOfStars + word + "*" * (nbrOfStars + 1))