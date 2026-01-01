from model.book import Book
from model.Library import Library
def main():
    my_library = Library()
    new_book = Book("lap trinh ai ","james","123")
    my_library.addBook(new_book)
main()