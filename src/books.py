# src/books.py

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

def get_all_books():
    return books

def create_book(data):
    new_id = max([book["id"] for book in books], default=0) + 1
    new_book = {
        "id": new_id,
        "title": data.get("title"),
        "author": data.get("author")
    }
    books.append(new_book)
    return new_book

