people = int(input('How many people need a ride? '))

PinTaxi = int(input('How many people fit in one taxi? '))

# Calculate the number of taxis needed
# and the number of people left over
taxis = people // PinTaxi +1

print('Taxis needed:', taxis)