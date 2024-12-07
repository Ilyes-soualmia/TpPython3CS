TotalAmounts = input("Total amount: ")

ItemsNbr = input("Number of items: ")

cndtn = True
while (cndtn):
  Day = input("Day of the week: ")
  if (Day == "Monday" or Day == "Tuesday" or Day == "Wednesday" or Day == "Thursday" or Day == "Friday" or Day == "Saturday" or Day == "Sunday"):
    cndtn = False

discount = 0

if (Day == "Saturday" or Day == "Sunday"):
  discount = 0.2
else:
  discount = 0.1  

if (int(ItemsNbr) > 5):
  discount = discount + 0.05

TotalAmounts = float(TotalAmounts) - float(TotalAmounts) * discount

print("Total amount after discount: ", TotalAmounts , "Dinars")