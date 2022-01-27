#!/usr/bin/env python3

# Calling the decimal module.
from decimal import Decimal 

# Asking for the price and money.
price = Decimal(input("Enter the price of the item: $"))
print()
cash = Decimal(input("Enter the amount of money received: $"))
print()

# Determining the change to give back.
change = Decimal(cash - price)
print("The amount of change is: $", format(change, ",.2f"), sep="")
print()
print("=====================================")
print()

# Figuring the amount of 20s
twenties = int(change / 20)
print("Number of 20 dollar bills is: ", twenties)
change = change - (twenties * 20)
# print(change)
print()

# Figuring the amount of 10s
tens = int(change / 10)
print("Number of 10 dollar bills is: ", tens)
change = change - (tens * 10)
# print(change)
print()

# Figuring the amount of 5s
fives = int(change / 5)
print("Number of 5 dollar bills is: ", fives)
change = change - (fives * 5)
# print(change)
print()

# Figuring the amount of 1s
ones = int(change / 1)
print("Number of 1 dollar bills is: ", ones)
change = change - (ones * 1)
# print(change)
print()

# Figuring the amount of quarters
quarters = int(change / Decimal(".25"))
print("Number of quarters is: ", quarters)
change = change - (quarters * Decimal(".25"))
# print(change)
print()

# Figuring the amount of dimes
dimes = int(change / Decimal(".10"))
print("Number of dimes is: ", dimes)
change = change - (dimes * Decimal(".10"))
# print(change)
print()

# Figuring the amount of nickels
nickels = int(change / Decimal(".05"))
print("Number of nickels is: ", nickels)
change = change - (nickels * Decimal(".05"))
# print(change)
print()

# Figuring the amount of pennies
pennies = int(change / Decimal(".01"))
print("Number of pennies is: ", pennies)
change = change - (pennies * Decimal(".01"))
# print(change)
print()







