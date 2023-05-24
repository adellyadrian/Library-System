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


books = [
    Book("The great Gatsby", "F. Scott Fitzgerald", 1925, 9780743273565, "Fiction", []),
    Book("The Alchemist", "Paulo Coelho", 1988, 9780061122415, "Fiction", []),
    Book("The Hobbit", "J.R.R. Tolkien", 1937, 9780345339683, "Fantasy", []),
    Book("The Lord of the Rings", "J.R.R. Tolkien", 1954, 9780618640157, "Fantasy", []),
    Book("Don Quixote", "Miguel de Cervantes", 1605, 9780936388878, "Novel", []),
    Book("War and Peace", "Leo Tolstoy", 1869, 9788412664812, "Novel", []),
    Book("Hamlet", "William Shakespeare", 1870, 9780140707342, "Shakespearean tragedy", []),
    Book("Lolita", "Vladimir Nabokov", 1955, 9783498046460, "Novel", []),
    Book("The Brothers Karamazov", "Fyodor Dostoevsky", 1879, 9788437606385, "Philosophical novel", []),
    Book("Alice's Adventures in Wonderland", "Lewis Carroll", 1865, 9780739367384, "Fantasy", [])
]

for book in books:
    book.add_copy("Copy 1")
    print(book.name)
    print(book.available_copies)
    book.remove_copy("Copy 1")
    print(book.available_copies)
