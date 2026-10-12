fruits = (("Apple", 150), ("Banana", 80), ("Mango", 200), ("Grapes", 250), ("Orange", 100), ("Papaya", 90))

for fruit in fruits:
    print(fruit[0] + ": " + str(fruit[1]))

fruitNames = [name[0] for name in fruits]
    
print("\n", fruitNames)

totalPrice = sum([price[1] for price in fruits])

print("\nTotal price: ", totalPrice)

fruits = (("Apple", 150), ("Banana", 80), ("Mango", 180), ("Grapes", 250), ("Orange", 100), ("Papaya", 90))

print()
for fruit in fruits:
    print(fruit, end=" ")