price=float(input("Please type in a price: "))
print("Dinars: ",int(price))
centim = price - int(price)
print("Centimes: ", int(centim * 100))