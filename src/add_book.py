import json

def add_book(new_book):
    # Basic validation
    if not isinstance(new_book, dict):
        return {"error": "Invalid book format. Must be a dictionary."}, 400

    required_fields = {"id", "title", "author"}
    if not required_fields.issubset(new_book.keys()):
        return {"error": f"Missing required fields: {required_fields - set(new_book.keys())}"}, 400

    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        books = []

    # Check for duplicate ID
    if any(book["id"] == new_book["id"] for book in books):
        return {"error": "Book with this ID already exists."}, 409

    books.append(new_book)

    try:
        with open("books.json", "w") as file:
            json.dump(books, file, indent=4)
    except IOError:
        return {"error": "Failed to save book to file."}, 500

    return {"message": "Book added successfully"}, 201
