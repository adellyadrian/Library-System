class Book:
    def __init__(self, name, author, year, isbn, genre, available_copies):
        self._name = name
        self._author = author
        self._isbn = isbn
        self._year = year
        self._genre = genre
        self._copies = []
        self._available_copies = available_copies

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def year(self):
        return self._year

    @property
    def genre(self):
        return self._genre

    @property
    def copies(self):
        return self._copies

    @property
    def available_copies(self):
        return self._available_copies

    def add_copy(self, copy):
        self._copies.append(copy)
        self._available_copies.append(copy)

    def remove_copy(self, copy):
        if copy in self._copies:
            self.copies.remove(copy)
            self._available_copies.remove(copy)
