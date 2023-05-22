from Book import Book
from Student import Student


class Library:
    def __init__(self):
        self._books = []
        self._students = []

    def add_book(self, name, author, year, isbn, genre, available_copies):
        book = Book(name, author, year, isbn, genre, available_copies)
        self._books.append(book)

    def remove_book(self, book):
        if book in self._books:
            self._books.remove(book)

    def add_student(self, name, limit):
        student = Student(name, limit)
        self._students.append(student)

    def remove_student(self, student):
        if student in self._students:
            self._students.remove(student)

    def get_all_books(self):
        return self._books

    def get_available_books(self):
        return [book for book in self._books]

    def search_books_by_name(self, name):
        return [book for book in self._books if name.lower() in book.name.lower()]

    def search_books_by_author(self, author):
        return [book for book in self._books if author.lower() in book.author.lower()]

    def search_books_by_genre(self, genre):
        return [book for book in self._books if genre.lower() in book.genre.lower()]
