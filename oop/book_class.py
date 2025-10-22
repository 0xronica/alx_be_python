class Book:
    def __init__(self, title: str, author: str, year: int)
        self.title = title
        self.author = author
        self.year = year
    def __del__(self):
        print(f"Deleting {self.title}")
    
    def __str__(self):
        return f"(title), by (author), published in (year)"
    
    def __repr__(self):
        retun f"Book('{sel.title}', '{self.author}', {self.year}')"