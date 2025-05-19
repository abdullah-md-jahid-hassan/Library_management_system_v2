from save_all_books import save_all_books

def update_book(all_books):
    search_book = input("Enter Book Title to Update: ")
    for book in all_books:
        if book["title"].lower() == search_book.lower():
            print(f"Current Details: {book}")
            book["title"] = input("Enter New Title: ") or book["title"]
            book["author"] = input("Enter New Author: ") or book["author"]
            book["year"] = int(input("Enter New Publishing Year: ") or book["year"])
            book["price"] = float(input("Enter New Price: ") or book["price"])
            book["quantity"] = int(input("Enter New Quantity: ") or book["quantity"])
            save_all_books(all_books)
            print("Book Updated Successfully!")
            return all_books
    print("Book Not Found!")
    return all_books
