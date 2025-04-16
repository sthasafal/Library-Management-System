import json

def delete_book(book_id):
    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        return False

    new_books = [book for book in books if book["id"] != book_id]

    if len(new_books) == len(books):
        return False

    with open("books.json", "w") as file:
        json.dump(new_books, file, indent=2)

    return True
