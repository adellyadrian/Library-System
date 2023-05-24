from Book import Book
from Student import Student


class BookCopy:
    def __init__(self, book_, copy_id):
        self._book = book_
        self._copy_id = copy_id
        self._borrowed = False
        self._condition_rating = 0

    @property
    def book(self) -> Book:
        return self._book

    @property
    def borrowed(self) -> bool:
        return self._borrowed

    def borrowed_(self, value: bool) -> None:
        self._borrowed = value
        if value:
            self._book.available_copies.remove(self)

    @property
    def condition_rating(self) -> int:
        return self._condition_rating

    def condition_rating_(self, rating: int) -> None:
        if 0 <= rating <= 5:
            self._condition_rating = rating


def change_borrow_limit(student_, limit):
    student_.limit = limit


book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "9780743273565", "Fiction", [])

# Create a book copy object
book_copy = BookCopy(book, "Copy 1")

# Get the book associated with the copy
copy_book = book_copy.book
print(copy_book.name)  # Output: The Great Gatsby

# Check if the copy is borrowed
print(book_copy.borrowed)  # Output: False

# Set the copy as borrowed
book_copy.borrowed_(False)

# Check if the copy is borrowed after setting it
print(book_copy.borrowed)  # Output: True

# Change the condition rating of the copy
book_copy._condition_rating_ = 4

# Get the condition rating of the copy
print(book_copy.condition_rating_)  # Output: 4

# Change the borrowing limit of a student
student = Student("John Doe", limit=3)
change_borrow_limit(student, 5)
print(student.limit)  # Output: 5
