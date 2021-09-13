import json
from book import Book


def load_books():
    # try:
    file = open("books.dat", "r")
    books_dict = json.loads(file.read())
    books = []
    for book in books_dict:
        books_obj = Book(book['id'], book['name'], book['author'], book['desc'],
                         book['isbn'], book['page_count'], book['year'], book['issued'])
        books.append(books_obj)
    return books
    # except Exception as p:
    # print(p)
    # return []


def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    with open("books.dat", "w") as file:
        file.write(json.dumps(json_books, indent=4))


def add_book(book):
    books = load_books()
    new_book = Book(book['id'], book['name'], book['author'], book['description'],
                    book['isbn'], book['page_count'], book['year'], book['issued'])

    save_books([*books, assign_valid_id(books, new_book)])


def assign_valid_id(books, new_book):
    book_ids = []
    for book in books:
        book_ids.append(int(book.id))
    if list(filter(lambda id: id == int(new_book.id), book_ids)) == []:
        return new_book
    else:
        new_book.id = int(max(book_ids) + 1)
        return new_book


def get_issued_books():
    books = load_books()
    return list(filter(lambda book: book.issued == True, books))


def get_unissued_books():
    books = load_books()
    return list(filter(lambda book: book.issued == False, books))


def update_book(book):
    book = Book(book['id'], book['name'], book['author'], book['description'],
                book['isbn'], book['page_count'], book['year'], book['issued'])
    books = load_books()
    if book != None:
        books = list(filter(lambda bk: int(bk.id) != int(book.id), books))
        books.append(book)
        save_books(books)

def delete_book(id):
	books = load_books()
	books = list(filter(lambda bk: int(bk.id)!=int(id), books))
	save_books(books)

def find_book(book_id):
    books = load_books()
    for book in books:
        if int(book.id) == int(book_id):
            return book
    return None
