"""
    Entity class should be coded here
"""


class BookException(Exception):
    def __init__(self, msg):
        self._msg = msg


class Book:
    def __init__(self, isbn, author, title):
        if len(isbn) != 17:
            raise BookException("Invalid ISBN!! 13 digits format needed: ***-*-**-******-*")
        elif len(isbn) == 17 and validate_isbn(isbn) is False:
            raise BookException("Invalid ISBN!! 13 digits format needed: ***-*-**-******-*")

        if validate_author(author) is False or author.isspace() is True or author == '':
            raise BookException("Invalid author input!!")

        if title.isspace() is True or title == '':
            raise BookException("Invalid title input!!")
        self._isbn = isbn
        self._author = author
        self._title = title

    @property
    def isbn(self):
        return self._isbn

    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title

    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @author.setter
    def author(self, value):
        if value.isalha() is False:
            raise BookException("Invalid author input!!")
        self._author = value

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def parse(self):
        tokens = self._title.strip().split(' ', 1)
        return tokens[0].lower()

    def __str__(self):
        return self._isbn.rjust(13) + ' | ' + self._author.rjust(22) + ' | ' + self._title


def validate_isbn(id_book):
    isbn_numerical = ''
    for char in id_book:
        if char != '-':
            isbn_numerical += char

    if isbn_numerical.isnumeric() is True and id_book[3] == id_book[5] == id_book[8] == id_book[15] == '-':
        return True
    else:
        return False

def validate_author(author_name):
    tokens = author_name.strip().split()
    if len(tokens) > 2 or len(tokens) == 1:
        return False
    elif len(tokens) == 2 and (tokens[0].isalpha() is False or tokens[1].isalpha() is False):
        return False
    else:
        return True

def test_book():
    b = Book('068-4-80-122121-0', 'Ernest Hemingway', 'The Old Man and the Sea')
    assert b.isbn == '068-4-80-122121-0'
    assert b.author == 'Ernest Hemingway'
    assert b.title == 'The Old Man and the Sea'

    try:
        b = Book('2aaa23', 'Ernest Hemingway', 'The Old Man and the Sea')
    except BookException:
        assert True

    try:
        b = Book('1234', 'Ernest Hemingway', 'The Man')
    except BookException:
        assert True

    try:
        b = Book('111-1-11_111111-1', 'Ernest', 'The Man')
    except BookException:
        assert True

    try:
        b = Book('111-1-11-111111-1', 'Ernest.No.1', 'The Man')
    except BookException:
        assert True

    try:
        b = Book('111-1-11-111111-1', 'Ernest.No.1', '')
    except BookException:
        assert True

    try:
        b = Book('111-1-11-111111-1', '   ', 'The Man')
    except BookException:
        assert True





