print("Runner1:")
name1 = input("name: ")
Time = float(input("Time (in seconds): "))
print("Runner2")
name2 = input("name: ")
Time2 = float(input("Time (in seconds): "))

if (Time < Time2):
    print("The faster runner is ", name1)
elif (Time > Time2):
    print("The faster runner is ", name2)
else:
    print(name1, " and ", name2, " have the same time.")