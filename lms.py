import json
import add_books
import view_all_books
import delete_book
import update_book

try:
    with open("all_books.json", "r") as fp:
        all_books = json.load(fp)
except FileNotFoundError:
    all_books = []

while True:
    print("\nWelcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Delete Book")

    menu = input("Select an option: ")

    if menu == "0":
        print("Thanks for using Library Management System!")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        all_books = update_book.update_book(all_books)
    elif menu == "4":
        all_books = delete_book.delete_books(all_books)
    else:
        print("Invalid option. Please try again!")
