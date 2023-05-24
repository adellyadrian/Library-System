from Book import Book


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


student = Student("John Doe", limit=3)
book1 = Book("Book1", "Author 1", 2021, "ISBN 1", "Genre 1", [])
student.borrow_book(book1)
print(student)
student.return_book(book1)
student.change_borrow_limit(5)
book2 = Book("Book 2", "Author 2", 2022, "ISBN 2", "Genre 2", [])
book3 = Book("Book 3", "Author 3", 2023, "ISBN 3", "Genre 3", [])
student.borrow_book(book2)
student.borrow_book(book3)
print(student.can_borrow())
print(student.borrowed_books)
