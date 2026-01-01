class Library:
    def __init__(self):
        self.books = []
    def addBook(self, book):
        self.books.append(book)
    def searchBook(self, title):
        for book in self.books:
            if book.title == title:
                return True
        return False
    def printBooks(self):
        for book in self.books:
            print(book)
    def searchBooksbyAuthor(self, author):
        for book in self.books:
            if book.author == author:
                print(book)