class Book:
    """A class representing a book with title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track if the book is checked out

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
        return False

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a library containing multiple books."""

    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it exists and is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Return a book by title if it exists and is checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print the list of available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
            else:
                print("Sorry, the book you mentioned is now available.")
