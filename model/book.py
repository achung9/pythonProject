class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    # lay ra ten tac gia
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

