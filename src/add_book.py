import json

def add_book(new_book):
    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []

    new_book['id'] = len(books) + 1
    books.append(new_book)

    with open("books.json", "w") as file:
        json.dump(books, file, indent=2)

    return new_book
