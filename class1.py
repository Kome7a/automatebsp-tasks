class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()

    def name(self):
        return self.first_name + ' ' + self.last_name

    def __repr__(self):
        return self.name()


class Author(Person):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.published_books = []


class Book:
    def __init__(self, title, author: Author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f"{self.title} - {self.author}"


class Library:
    def __init__(self, books: list):
        self.books = books
        self.borrowed_books = []
        self.available_books = books.copy()

    def return_book(self, book):
        if book in self.borrowed_books:
            self.available_books.append(book)
            self.borrowed_books.remove(book)
        else:
            print('This book is not from this library!')

    def borrow_book(self, book):
        if book in self.available_books:
            self.borrowed_books.append(book)
            self.available_books.remove(book)
        else:
            print('this book is not available')

    def print_available_books(self):
        for book in self.available_books:
            print(book)

    def print_borrowed_books(self):
        for book in self.borrowed_books:
            print(book)


class Customer(Person):
    def __init__(self, first_name, last_name, library):
        super().__init__(first_name, last_name)
        self.library = library

    def borrow_book(self, book):
        self.library.borrow_book(book)

    def return_book(self, book):
        self.library.return_book(book)


def main():
    hw = Author('Ernest', 'hemingway')
    vazov = Author('Ivan', 'Vazov')
    peyo = Author('Peyo', 'Yavorov')
    authors = [hw, vazov, peyo]

    old_man = Book('Old man and the sea', hw, 'drama')
    pod_igoto = Book('Pod igoto', vazov, 'historical')
    poeziya = Book('Sbornik stihotvoreniya', peyo, 'poetry')
    books = [old_man, pod_igoto, poeziya]

    sofia_library = Library(books)
    customer = Customer('Rumen', 'Ivanov', sofia_library)

    customer.borrow_book(pod_igoto)

    print('available books')
    sofia_library.print_available_books()

    print('borrowed_books')
    sofia_library.print_borrowed_books()


main()

