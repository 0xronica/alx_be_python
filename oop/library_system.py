class Book:
    def __init__(self, title, author):
        self.tite = title
        self.authoor = author
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class EBook:
    def __init__(self, title, author, file_size):
        super(). __init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"{self.title} by {self.author} (EBook - {self.file_size}MB)"

class PrintBook:
    def __init__(self, title, author, page_count):
        super(). __init__ (title, author)
        self.page_count = page_count
    def __str__(self):
        return f"{self.title} by {self.author} ({self.page_count} pages)"

class Library:
    """Class representing a library that contains books (composition)."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints details of all books in the library."""
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)