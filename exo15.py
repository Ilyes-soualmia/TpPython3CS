
word = input("Enter a word in lower case: ")

a , e , o = 0 , 0 , 0
for i in word:
    if i == "a":
        a += 1
    elif i == "e":
        e += 1
    elif i == "o":
        o += 1
if a>0:
    print("a found")
else:
    print("a not found") 
if e>0:
    print("e found")
else:
    print("e not found")
if o>0:
    print("o found")
else:
    print("o not found")
