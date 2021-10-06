"""
    UI class.
    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""
import copy
import random
import string

from domain.entity import Book, BookException
from services.service import Library, UndoException, test_init, test_functions


class UserInterface:
    def __init__(self):
        self._library = Library()

    def add_book_ui(self):
        isbn = input("Introduce ISBN: ")
        author = input("Introduce author: ")
        title = input("Introduce title: ")
        book = Book(isbn, author, title)
        self._library.add_book(book)

    def display_list(self):
        for book in self._library.books:
            print(book)

    def filter_list_ui(self):
        value = input("Introduce the filter value: ")
        self._library.filter_list(value)

    @staticmethod
    def print_menu():
        print("Hello and welcome to Books! Choose a command below: ")
        print("\t1. Add a book.")
        print("\t2. Display the book list.")
        print("\t3. Filter the list by a filter-value.")
        print("\t4. Undo")
        print("\t0. Exit")

    def start_ui(self):
        self._library.books = generate_books()
        self._library.history.append(copy.deepcopy(self._library.books))
        done = False
        self.print_menu()
        while not done:
            command = input("\nEnter your command: ")
            try:
                if command == '1':
                    self.add_book_ui()
                elif command == '2':
                    self.display_list()
                elif command == '3':
                    self.filter_list_ui()
                elif command == '4':
                    self._library.undo_list()
                elif command == '0':
                    done = True
                else:
                    print("Bad command!!")
            except (UndoException, BookException) as err:
                print(str(err))


def get_string(length):
    digits = "1234567890"
    result = ''.join(random.choice(digits) for i in range(length))
    return result


def get_word(length):
    letters = string.ascii_letters.lower()
    result = ''.join(random.choice(letters) for i in range(length))
    return result


def generate_books():
    books = []
    index = 10

    while index != 0:
        book_id = get_string(3) + '-' + get_string(1) + '-' + get_string(2) + '-' + get_string(6) + '-' + get_string(1)

        len_first_name = random.randint(3, 10)
        len_last_name = random.randint(3, 10)

        first_name = get_word(len_first_name)
        first_name = first_name[0].upper() + first_name[1:]
        last_name = get_word(len_last_name)
        last_name = last_name[0].upper() + last_name[1:]
        book_author = first_name + ' ' + last_name

        len_title_words = random.randint(1, 5)
        book_title = ''
        for i in range(len_title_words):
            length = random.randint(3, 6)
            book_title += get_word(length)
            book_title += ' '

        book_title = book_title[0].upper() + book_title[1:]

        books.append(Book(book_id, book_author, book_title))
        index = index - 1
    return books


def generate_books_v2():
    books = []
    first_name = ['Andrew', 'William', 'John', 'Kevin', 'Sandra', 'Claudia', 'Matthew', 'Mark', 'Joseph', 'Nick',
                  'David', 'Oliver', 'Hannah', 'Christine', 'Thomas', 'Joe', 'Arthur', 'Molly']
    last_name = ['Buick', 'Hoffman', 'Simpsons', 'Park', 'Cole', 'Kennedy', 'Dermot', 'Mann', 'Tennessee', 'Pope',
                 'Shelby', 'Ratatouille', 'Ken', 'Letterman', 'Clayton', 'Steve']
    title_name = ['Life On Mars', 'Introduction to Python', 'Uni is damn difficult', 'One last assignment',
                  'I want to break free', 'Life', 'Gibberish', 'Science', 'Psychology', 'Hate Chemistry', 'Work']

    index = 0
    while index <= 10:
        book_id = get_string(3) + '-' + get_string(1) + '-' + get_string(2) + '-' + get_string(6) + '-' + get_string(1)
        book_author_first = random.choice(first_name)
        book_author_last = random.choice(last_name)
        book_author = book_author_first + ' ' + book_author_last
        book_title = random.choice(title_name)
        new_book = Book(book_id, book_author, book_title)
        if new_book not in books:
            books.append(new_book)
            index += 1

    return books


test_functions()
library_ui = UserInterface()
library_ui.start_ui()
