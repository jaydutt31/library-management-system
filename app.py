import my_func
import os
from my_func import save_books

my_func.print_options()

option = input()
books = []
while option != "X" and option != "x":
	if option == "1":
		books.append(my_func.create_book())
	elif option == "2":
		save_books(books)
	elif option == "3":
		books = my_func.load_books()
	elif option == "4":
		print(my_func.issue_book(books))
	elif option =="5":
		my_func.return_book(books)
	elif option == "6":
		my_func.update_book(books)
	elif option =="7":
		my_func.show_all(books)
	elif option == "8":
		my_func.show_book(books)
	else:
		print("The given command doesnt exist..")
	input("press Enter to continue...")
	#asking for input
	os.system("cls")
	my_func.print_options()
	option = input()



