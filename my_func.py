from book import Book
import book 
import json
from tabulate import tabulate

def print_options():
	print("Press the specfic button for the action")
	print("1 create a book")
	print("2 save the book")
	print("3 load book from the list")
	print("4 issued books")
	print("5 return a book")
	print("6 update a book")
	print("7 show all books")
	print("8 show books")

def input_book_info():
	id = input("id:")
	name = input("name:")
	desc = input("desc:")
	isbn = input("ISBN:")
	page_count = int(input("Page Count:"))
	issued = input("Issued: y/Y for True, any else key for False:")
	issued = (issued =="y" or issued == "Y")
	author = input("author:")
	year = int(input("year:"))
	
	return {
		"id":id,
		"name":name,
		"desc":desc,
		"isbn":isbn,
		"page_count":page_count,
		"issued":issued,
		"author":author,
		"year":year
	}


def create_book():
	print("Please enter your book informatio:")
	book_input = input_book_info()
	book = Book(book_input['id'], book_input['name'],book_input['desc'], book_input['isbn'], book_input['page_count'], book_input['issued'], book_input['author'], book_input['year'])
	print(book.to_dict())
	return book

def save_books(books):
	json_books = []
	for book in books:
		json_books.append(book.to_dict())
	try:
		file = open("books.dat","w")
		file.write(json.dumps(json_books, indent=4))
	except:
		print("we had an Error.")
		

def load_books():
	try:
		file = open("books.dat","r")
		loaded_books = json.loads(file.read())
		books = []
		for book in loaded_books:
			new_obj = Book(book['id'], book['name'],book['desc'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year'])
			books.append(new_obj)
		print("succesfully loaded books")
		return books
	except:
		print("The file doesnt exist or an error occured")

def find_book(books, id):
	for index, book in enumerate(books):
		if book.id == id:
			return index
	return None

def issue_book(books):
	id = input("Enter Id of book you want to issue:")
	index = find_book(books, id)
	if index != None:
		books[index].issued = True
		print("Book succesfully Updated")
	else:
		print("could not find the book you are looking for")

def return_book(books):
	id = input("Enter Id of book you want to return:")
	index = find_book(books, id)
	if index != None:
		books[index].issued = False
		print("Book succesfully Updated")
	else:
		print("could not find the book you are looking for")

def update_book(books):
	id = input("Enter Id of book you want to update:")
	index = find_book(books, id)
	if index != None:
		new_book = create_book()
		old_book = books[index]
		books[index] = new_book
		del old_book
		print("Book succefully updated")
	else:
		print("we could not find the book")

def show_all(books):
	for book in books:
		table = book.to_dict()
		print(table)


def show_book(books):
	id = input("Please enter id of the book youre looking for:")
	index = find_book(books, id)
	if index != None:
		print(books[index].to_dict())
	else:
		print("We could not found the book.")


