class Student:
    def __init__(self, name, limit=0):
        self.name = name
        self.borrowed_books = []
        self.limit = limit

    def __str__(self):
        return self.name

    def can_borrow(self):
        return len(self.borrowed_books) < self.limit

    def borrow_book(self, book):
        if self.can_borrow() and book:
            book.borrowed_by = self
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.borrowed_by = None
            self.borrowed_books.remove(book)

    def change_borrow_limit(self, limit):
        self.limit = limit
