import json

def get_books():
    try:
        with open("books.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
