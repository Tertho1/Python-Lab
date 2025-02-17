from state import books

def add_book(title, author, genre, price):
    books.append({"title": title, "author": author, "genre": genre, "price": price})


def list_books():
    return books
