total_amount = float(input("Total amount: "))
num_items = int(input("Number of items: "))
day_of_week = input("Day of the week: ")


if day_of_week.lower() in ['saturday', 'sunday']:
    discount = 0.20
else:
    discount = 0.10


if num_items > 5:
    discount += 0.05


discounted_price = total_amount * (1 - discount)


print(f"The total price after discount is: {discounted_price:.1f}dinars")
