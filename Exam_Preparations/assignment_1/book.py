
def add_book(title,author,genre,price,books=[] ):
    books.append([title,author,genre,price])
    return books
def list_books(books):
    for book in books:
        print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}, Price: {book[3]}")