from flask import Flask, request, jsonify
from flask_cors import CORS

from src.get_books import get_books
from src.add_book import add_book
from src.update_book import update_book
from src.delete_book import delete_book

app = Flask(__name__)
CORS(app)

@app.route("/books", methods=["GET"])
def list_books():
    return jsonify(get_books())

@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    new_book = add_book(data)
    return jsonify(new_book), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def edit_book(book_id):
    data = request.get_json()
    updated = update_book(book_id, data)
    if updated:
        return jsonify(updated)
    return jsonify({"error": "Book not found"}), 404

@app.route("/books/<int:book_id>", methods=["DELETE"])
def remove_book(book_id):
    deleted = delete_book(book_id)
    if deleted:
        return jsonify({"message": "Book deleted"})
    return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
