from model.book import Book
from model.Library import Library

def main():
    my_library = Library()
    # Thêm sách
    new_book1 = Book("lap trinh ai ", "james", "123")
    my_library.addBook(new_book1)
    new_book2 = Book("cooking with souma ", "souma", "333")
    my_library.addBook(new_book2)
    # In danh sách
    print("--- Danh sách sách trong thư viện ---")
    my_library.printBooks()
    # Kiểm tra tồn tại
    print("\nKiểm tra 'cooking with souma' có tồn tại không:")
    # LỖI CŨ CỦA BẠN: my_library.books("...")
    # SỬA THÀNH: Gọi đúng tên hàm searchBook
    exists = my_library.searchBook("cooking with souma")
    print(f"Kết quả: {exists}")
    my_library.searchBooksbyAuthor("james")

main()