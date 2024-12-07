TicketPrice = 15.5

name = input("Enter your name: ")

if (name != "VIP"):
    TicketsNbr = int(input("How many tickets do you want to buy? "))
    TotalPrice = TicketPrice * TicketsNbr
    print("Total price is: ", TotalPrice)
    print("Enjoy the show!")
else:
    print("Enjoy the show for free!")
