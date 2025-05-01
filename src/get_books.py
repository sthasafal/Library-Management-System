import json

def get_books():
    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        return {"error": "No books found. The data file does not exist."}, 404
    except json.JSONDecodeError:
        return {"error": "Book data is corrupted."}, 500

    if not books:
        return {"message": "No books available."}, 200

    return {"books": books}, 200
