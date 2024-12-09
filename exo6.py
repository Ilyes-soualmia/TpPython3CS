price = float(input("please type in a price: "))

print("Dinars: ", int(price // 1))

print("Centimes:", int(price % 1 * 100))