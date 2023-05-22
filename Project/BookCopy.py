class BookCopy:
    def __init__(self, book, copy_id):
        self._book = book
        self._copy_id = copy_id
        self._borrowed = False
        self._condition_rating = 0

    @property
    def book(self):
        return self.book

    @property
    def borrowed(self):
        return self._borrowed

    def borrowed_(self, value):
        self._borrowed = value
        if value:
            self.book.available_copies.remove(self)

    @property
    def condition_rating(self):
        return self.condition_rating


def change_borrow_limit(student, limit):
    student.limit = limit
