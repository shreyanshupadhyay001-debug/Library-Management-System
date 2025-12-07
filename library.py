import json

DATA_FILE = "data/books.json"

def load_books():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=4)

def add_book(title, author):
    books = load_books()
    new_book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "status": "available"
    }
    books.append(new_book)
    save_books(books)

def issue_book(book_id):
    books = load_books()
    for book in books:
        if book["id"] == book_id and book["status"] == "available":
            book["status"] = "issued"
            save_books(books)
            return "Book issued successfully!"
    return "Book not available."

def return_book(book_id):
    books = load_books()
    for book in books:
        if book["id"] == book_id and book["status"] == "issued":
            book["status"] = "available"
            save_books(books)
            return "Book returned."
    return "Invalid return."

def view_books():
    books = load_books()
    return books


