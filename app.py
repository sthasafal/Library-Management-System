from flask import Flask, jsonify, request
from src.books import get_all_books, create_book


app = Flask(__name__)

@app.route('/books')
def list_books():
    return jsonify(get_all_books())

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = create_book(data)
    return jsonify(new_book), 201