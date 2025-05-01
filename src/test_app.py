from add_book import add_book
from delete_book import delete_book

# Test adding a book
response, status = add_book({"id": 1, "title": "Test Book", "author": "Tester"})
print("Add Book:", response, "Status:", status)

# Test deleting the book
response, status = delete_book(1)
print("Delete Book:", response, "Status:", status)
