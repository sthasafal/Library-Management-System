import json

def delete_book(book_id):
    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"error": "Book data not found."}, 404

    # Check if book exists
    book_exists = any(book["id"] == book_id for book in books)
    if not book_exists:
        return {"error": "Book with specified ID not found."}, 404

    updated_books = [book for book in books if book["id"] != book_id]

    try:
        with open("books.json", "w") as file:
            json.dump(updated_books, file, indent=4)
    except IOError:
        return {"error": "Failed to save updated book list."}, 500

    return {"message": "Book deleted successfully"}, 200
