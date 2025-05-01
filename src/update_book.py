import json

def update_book(book_id, updated_info):
    if not isinstance(updated_info, dict):
        return {"error": "Update data must be a dictionary."}, 400

    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"error": "Book data not found."}, 404

    book_found = False
    for book in books:
        if book["id"] == book_id:
            book.update(updated_info)
            book_found = True
            break

    if not book_found:
        return {"error": "Book with specified ID not found."}, 404

    try:
        with open("books.json", "w") as file:
            json.dump(books, file, indent=4)
    except IOError:
        return {"error": "Failed to save updated book."}, 500

    return {"message": "Book updated successfully"}, 200
