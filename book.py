class Book:
	def __init__(self, id, name, author, desc, isbn, page_count, year, issued):
		self.id= id
		self.name = name
		self.desc = desc
		self.isbn = isbn 
		self.page_count = page_count
		self.issued = issued 
		self.author = author
		self.year = year

	#def set_name(self,name): not used to keep it simple. a function to check name
		#if 
	
	def to_dict(self):
		dictionary = {
			"id":self.id,
			"name":self.name,
			"author":self.author,
			"desc":self.desc,
			"isbn":self.isbn,
			"page_count":self.page_count,
			"year":self.year,
			"issued":self.issued
		}
		return dictionary



#book = Book(12,"autobiography of a yogi","build habits","212","500",True,"yogi","2020")

#print(book.to_dict())