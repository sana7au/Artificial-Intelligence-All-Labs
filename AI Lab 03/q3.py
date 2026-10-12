books = [{"title": "Introduction to AI", "author": "Stuart Russell", "copies_available": 3, "rating": 4.8}, 
         {"title": "Python Crash Course", "author": "Eric Matthes", "copies_available": 0},
         {"title": "Deep Learning", "author": "Ian Goodfellow", "copies_available": 5, "rating": 4.6}]

for book in books:
    print(book["title"] + " by " + book["author"])
    
titlesList = [book["title"] for book in books if book["copies_available"] > 0]

print("\nAvailable titles: ", titlesList)

print()
for book in books: 
    print(book.get("title"), "rating: ", book.get("rating", "Not Rated"))
    
print("\nAfter borrowing ", books[0]["title"], ", copies available: ", books[0]["copies_available"] - 1)

print("\nUpdated catalog: ", books)