
# Easy way to check if a word is a palindrome
def PalindromeAdvanced (word):
    if word == word[::-1]:
        return True
    else:
        return False

#normal way
def Palindrome (word):
    i = len(word) - 1
    j = 0
    while j<i/2:
        if word[j] == word[i - j]:
            j += 1
        else:
            return False
    return True
    
word = input("Please type in a word: ")

if Palindrome(word):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")


"""
if PalindromeAdvanced(word):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
"""