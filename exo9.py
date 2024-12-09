
Cities = {}
counter = 0
while True:
    city = input("Please type in a city name: ")
    if city == "stop" or city == "STOP" or city == "Stop":
        break
    else:
        for i in city:
            counter += 1
        Cities.update({city: counter*1_000_000})
        counter = 0    
#sort by value
Cities = sorted(Cities.items() , key=lambda x: x[1]) 
print(Cities)