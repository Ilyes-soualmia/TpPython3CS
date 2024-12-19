

def anagrams(word1, word2):
    if len(word1) != len(word2): # check if they're of the same length
        return False             # else they can't be anagrams.

    for i in word1:
        if i not in word2:
            return False
        else:
            word2 = word2.replace(i, '', 1) # we're removing the letter from word2 to make sure the same nbr
    return True                             # of repeated letters are present in both words.


print(anagrams('abcdae', 'aabcde'))  # ['aabb', 'bbaa']