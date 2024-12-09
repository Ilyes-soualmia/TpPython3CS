
# Easy way to check if a word is a palindrome
def PalindromeAdvanced (word):
    if word == word[::-1]:
        print("Yes, it's a palindrome.")
    else:
        print("No, it's not a palindrome.")

#normal way
def Palindrome (word):
    i = len(word) - 1
    j = 0
    while j<i/2:
        if word[j] == word[i - j]:
            j += 1
        else:
            print("No, it's not a palindrome.")
            return
    print("Yes, it's a palindrome.")
    
word = input("Please type in a word: ")

Palindrome(word)

"""
PalindromeAdvanced(word)
"""