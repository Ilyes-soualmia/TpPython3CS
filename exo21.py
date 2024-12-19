def length (list):
    counter = 0
    for i in list:
        counter += 1
    return counter

#Calculates the arithmetic mean

def mean (list):
    total = 0
    for i in list:
        total += int(i)
    return total/length(list)

def range_of_list(list):
    return max(list) - min(list)

#example of application
def main():
    List = [1,2,3,4,5,6,7,8,9,10] #or choose any list

    print(f"Length of the list: {length(List)}")
    print(f"Mean of the list: {mean(List)}")
    print(f"Range of the list: {range_of_list(List)}")

main()    