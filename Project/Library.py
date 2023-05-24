from Book import Book
from Student import Student


class Library:
    def __init__(self):
        self._books = []
        self._students = []

    def add_book(self, name, author, year, isbn, genre, available_copies):
        book_ = Book(name, author, year, isbn, genre, available_copies)
        self._books.append(book_)

    def remove_book(self, book_):
        if book_ in self._books:
            self._books.remove(book_)

    def add_student(self, name, limit):
        student = Student(name, limit)
        self._students.append(student)

    def remove_student(self, student):
        if student in self._students:
            self._students.remove(student)

    def get_all_books(self):
        return self._books

    def get_available_books(self):
        return [book_ for book_ in self._books]

    def search_books_by_name(self, name):
        return [book_ for book_ in self._books if name.lower() in book.name.lower()]

    def search_books_by_author(self, author):
        return [book_ for book_ in self._books if author.lower() in book.author.lower()]

    def search_books_by_genre(self, genre):
        return [book_ for book_ in self._books if genre.lower() in book.genre.lower()]

    @property
    def students(self):
        return self._students


library = Library()

library.add_book("Book 1", "Author 1", 2021, "ISBN 1", "Genre 1", 5)
library.add_book("Book 2", "Author 2", 2022, "ISBN 2", "Genre 2", 3)
library.add_book("Book 3", "Author 3", 2023, "ISBN 3", "Genre 1", 2)

# Add students to the library
library.add_student("John Doe", 3)
library.add_student("Jane Smith", 5)

# Get all books in the library
all_books = library.get_all_books()
for book in all_books:
    print(book.name)

# Get available books in the library
available_books = library.get_available_books()
for book in available_books:
    print(book.name)

# Search books by name
searched_books = library.search_books_by_name("book")
for book in searched_books:
    print(book.name)

# Remove a book from the library
book_to_remove = all_books[0]
library.remove_book(book_to_remove)

# Remove a student from the library
student_to_remove = library.students[0]
library.remove_student(student_to_remove)
