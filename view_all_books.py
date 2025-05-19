import json

def view_all_books(all_books):
    if not all_books:
        print("No books available.")
        return
    
    for book in all_books:
        print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Year: {book['year']}, Price: {book['price']}, Quantity: {book['quantity']}, Added At: {book['bookAddedAt']}")
