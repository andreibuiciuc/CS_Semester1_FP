"""
    Service class includes functionalities for implementing program features
"""
import copy

from domain.entity import BookException, Book, test_book


class UndoException(Exception):
    def __init__(self, msg):
        self._msg = msg


class Library:
    def __init__(self):
        self._books = []
        self._history = copy.deepcopy(self._books)

    def __len__(self):
        return len(self._books)

    @property
    def books(self):
        return self._books

    @property
    def history(self):
        return self._history

    @books.setter
    def books(self, value):
        self._books = value

    @history.setter
    def history(self, value):
        self._history = value

    def add_book(self, book):
        """
        Add a book to the list of books.
        :param book: A book
        :return: -
        :raises BookException for duplicate ISBN.
        """

        for b in self._books:
            if b.isbn == book.isbn:
                raise BookException("Duplicate ISBN!! Cannot add this book.")
        self._books.append(book)

        auxiliary_list = copy.deepcopy(self._books)
        self._history.append(auxiliary_list)

    def filter_list(self, value):
        """
        Filter the list by deleting the book titles starting with the value
        :param value: A filter value
        :return: -
        """

        result = list(filter(lambda book: book.parse != value.lower(), self._books))
        self._books.clear()
        for b in result:
            self._books.append(b)
        # self._books = copy.deepcopy(result)

        auxiliary_list = copy.deepcopy(self._books)
        self._history.append(auxiliary_list)

    def undo_list(self):
        """
        Undoes the operations which modify data until the initial book list is reached
        :return: -
        """
        if len(self._history) == 1:
            raise UndoException("No more undoes left!")
        self._history.pop()
        self._books = copy.deepcopy(self._history[-1])


def test_init():
    books = []
    books.append(Book('0684801221', 'Ernest Hemingway', 'The Old Man and the Sea'))
    books.append(Book('0684801222', 'Victor Hugo', 'Les Miserables'))
    books.append(Book('0684801223', 'Ray Bradbury', 'Fahrenheit 451'))
    books.append(Book('0684801224', 'Thomas Mann', 'The Magic Mountain'))
    books.append(Book('0684801225', 'William Shakespeare', 'Hamlet'))
    books.append(Book('0684801226', 'Mark Twain', 'Life on the Mississippi'))
    books.append(Book('0684801227', 'Paulo Coelho', 'The Alchemist'))
    books.append(Book('0684801228', 'Oscar Wilde', 'The Happy Prince'))
    books.append(Book('0684801229', 'Fyodor Dostoevsky', 'Crime and Punishment'))
    books.append(Book('0684801230', 'J.D.Salinger', 'The Catcher in the Rye'))
    return books


def test_add_book():
    books = Library()
    books.add_book(Book('068-4-80-122121-0', 'Ernest Hemingway', 'The Old Man and the Sea'))
    assert len(books) == 1

    try:
        books.add_book(Book('068-4-80-122121-0', 'Ernest Hemingway', 'The Old Man and the Sea'))
    except BookException:
        assert True
    assert len(books) == 1

    try:
        books.add_book(Book('068-4-80-122121-0', 'An author', 'A title'))
    except BookException:
        assert True
    assert len(books) == 1

    try:
        books.add_book(Book('1234567890123', 'An author', 'A title'))
    except BookException:
        assert True
    assert len(books) == 1

    try:
        books.add_book((Book('1234-210a', 'An author', 'A title')))
    except BookException:
        assert True
    assert len(books) == 1

    try:
        books.add_book(Book('111-1-11-111111-1', 'An author123', 'A title'))
    except BookException:
        assert True
    assert len(books) == 1

    try:
        books.add_book(Book('111-1-11-111111-1', 'firstname', 'A title'))
    except BookException:
        assert True
    assert len(books) == 1


def test_filter_list():
    books = Library()
    books.add_book(Book('068-4-80-122121-0', 'Ernest Hemingway', 'The Old Man and the Sea'))
    books.add_book(Book('068-4-80-444333-1', 'Victor Hugo', 'Les Miserables'))
    books.add_book(Book('068-4-80-566276-0', 'J Salinger', 'The Catcher in the Rye'))

    books.filter_list('No')
    assert len(books) == 3

    books.filter_list('The')
    assert len(books) == 1

    books.filter_list('Les')
    assert len(books) == 0


def test_undo_list():
    books = Library()
    books.add_book(Book('068-4-80-122121-0', 'Ernest Hemingway', 'The Old Man and the Sea'))
    books.add_book(Book('068-4-80-444333-3', 'Victor Hugo', 'Les Miserables'))
    books.add_book(Book('068-4-80-566555-5', 'J Salinger', 'The Catcher in the Rye'))

    books.add_book(Book('068-4-88-888888-8', 'A Bui', 'Life'))
    assert len(books) == 4

    books.undo_list()
    assert len(books) == 3

    books.filter_list('The')
    assert len(books) == 1

    books.undo_list()
    assert len(books) == 3

    books.add_book(Book('068-4-88-888888-8', 'A Bui', 'Life'))
    books.filter_list('The')
    assert len(books) == 2

    books.undo_list()
    assert len(books) == 4

    books.undo_list()
    assert len(books) == 3


def test_functions():
    test_add_book()
    test_filter_list()
    test_undo_list()
    test_book()
