# Shopping List
shopping_list = [ 
{"item": "Notebook", "price": 150, "purchased": True}, 
{"item": "Pen", "price": 30, "purchased": True}, 
{"item": "USB Drive", "price": 900, "purchased": False}, 
]

# List comprehension to get names of items not yet purchased
unpurchased_items = [item["item"] for item in shopping_list if item["purchased"] == False]

# List comprehension to calculate total price of unpurchased items
total_price = sum(item["price"] for item in shopping_list if item["purchased"] == False)

# Printing data
print(f"Still need to buy: {unpurchased_items}")
print(f"Remaining cost: {total_price}")