import json

def update_book(book_id, updated_data):
    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        return None

    for book in books:
        if book["id"] == book_id:
            book.update(updated_data)
            with open("books.json", "w") as file:
                json.dump(books, file, indent=2)
            return book

    return None
