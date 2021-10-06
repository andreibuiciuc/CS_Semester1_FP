import datetime
import re

from Domain.Exceptions import MovieValidatorException, RentalValidatorException, ClientValidatorException, \
    DuplicateIdException, GenreException, RentalException, ClientException, MovieException


class UI:
    def __init__(self, movie_service, client_service, rental_service, undo_service):
        self._movie_service = movie_service
        self._client_service = client_service
        self._rental_service = rental_service
        self._undo_service = undo_service

    @staticmethod
    def print_menu():
        print("\nHello and welcome to Book Rental. Choose a command below:")
        print("\t1. Manage movies")
        print("\t2. Manage clients")
        print("\t3. Manage rentals")
        print("\t4. Show statistics")
        print("\t5. Undo")
        print("\t6. Redo")
        print("\t0. Exit")

    @staticmethod
    def print_movie_submenu():
        print("\ta. Add a movie")
        print("\tb. Remove a movie")
        print("\tc. Update a movie")
        print("\td. Display movies")
        print("\te. Search movies")
        print("\t0. Exit")

    @staticmethod
    def print_client_submenu():
        print("\ta. Add a client")
        print("\tb. Remove a client")
        print("\tc. Update a client")
        print("\td. Display clients")
        print("\te. Search clients")
        print("\t0. Exit")

    @staticmethod
    def print_rent_return_submenu():
        print("\ta. Rent a movie")
        print("\tb. Return a movie")
        print("\tc. Display rentals")
        print("\t0. Exit")

    @staticmethod
    def print_statistics_submenu():
        print("\ta. Most rented movies")
        print("\tb. Most active clients")
        print("\tc. Late rentals")

    def add_movie_ui(self):
        movie_id = input("Introduce the movie id: ")
        title = input("Introduce the movie title: ")
        description = input("Introduce description: ")
        genre = input("Introduce genre: ")

        movie = self._movie_service.create_movie(movie_id, title, description, genre)
        self._movie_service.add_movie_record(movie)

    def remove_movie_ui(self):
        movie_id = input("Introduce the movie id for removal: ")
        self._movie_service.remove_movie_record(movie_id)

    def update_movie_ui(self):
        movie_id = input("Introduce the movie id for update: ")
        title = input("Introduce new title: ")
        description = input("Introduce new description: ")
        genre = input("Introduce new genre: ")
        self._movie_service.update_movie(movie_id, title, description, genre)

    def display_movies(self):
        for movie in self._movie_service.get_repo.get_movies:
            print(str(movie))

    def add_client_ui(self):
        client_id = input("Introduce client id: ")
        name = input("Introduce client name: ")
        client = self._client_service.create_client(client_id, name)
        self._client_service.add_client_record(client)

    def remove_client_ui(self):
        client_id = input("Introduce the client id for removal: ")
        self._client_service.remove_client_record(client_id)

    def update_client_ui(self):
        client_id = input("Introduce the client id for update: ")
        name = input("Introduce new name: ")
        self._client_service.update_client(client_id, name)

    def display_clients(self):
        for client in self._client_service.get_repo.get_clients:
            print(str(client))

    def search_clients(self):
        search = input("Search for a client: ")
        valid_search = False
        for client in self._client_service.get_repo.get_clients:
            match_id = re.search(search, client.client_id)
            match_name = re.search(search.lower(), client.name.lower())
            if match_id or match_name:
                valid_search = True
                print(str(client))
        if valid_search is False:
            print("No search results.")

    def search_movies(self):
        search = input("Search for a movie: ")
        valid_search = False
        for movie in self._movie_service.get_repo.get_movies:
            match_id = re.search(search, movie.movie_id)
            match_title = re.search(search.lower(), movie.title.lower())
            match_description = re.search(search.lower(), movie.description.lower())
            match_genre = re.search(search.lower(), movie.genre.lower())
            if match_id or match_title or match_description or match_genre:
                valid_search = True
                print(str(movie))
        if valid_search is False:
            print("No search results.")

    def rent_movie_ui(self):
        rent_id = input("Introduce rent id: ")
        movie_id = input("Introduce movie id to be rented: ")
        client_id = input("Introduce client id for rental: ")

        rented_date = datetime.date.today()

        year = int(input("Introduce the year for due date: "))
        month = int(input("Introduce the month for due date: "))
        day = int(input("Introduce the day for due date: "))
        due_date = datetime.date(year, month, day)

        rental = self._rental_service.create_rental(rent_id, movie_id, client_id, rented_date, due_date, None)
        self._rental_service.rent_movie_record(rental)

    def return_movie_ui(self):
        movie_id = input("Introduce the movie id for return: ")
        self._rental_service.return_movie_record(movie_id)

    def display_rentals(self):
        for rental in self._rental_service.get_repo.get_rentals:
            print(str(rental))

    def most_rented_movies(self):
        for movie in self._rental_service.most_rented_movies:
            print(str(movie))

    def most_active_clients(self):
        for client in self._rental_service.most_active_clients:
            print(str(client))

    def late_rentals(self):
        for movie in self._rental_service.late_rentals:
            print(str(movie))

    def undo(self):
        self._undo_service.undo()

    def redo(self):
        self._undo_service.redo()

    def start(self):
        done = False
        while not done:
            self.print_menu()
            command_menu = input("\nEnter your command: ")
            try:
                if command_menu == '1':
                    self.print_movie_submenu()
                    done_sub = False
                    while not done_sub:
                        command = input("\nEnter your command: ")

                        if command == 'a':
                            self.add_movie_ui()
                        elif command == 'b':
                            self.remove_movie_ui()
                        elif command == 'c':
                            self.update_movie_ui()
                        elif command == 'd':
                            self.display_movies()
                        elif command == 'e':
                            self.search_movies()
                        elif command == '0':
                            done_sub = True
                        else:
                            print("Bad command!!")

                elif command_menu == '2':
                    self.print_client_submenu()
                    done_sub = False
                    while not done_sub:
                        command = input("\nEnter your command: ")

                        if command == 'a':
                            self.add_client_ui()
                        elif command == 'b':
                            self.remove_client_ui()
                        elif command == 'c':
                            self.update_client_ui()
                        elif command == 'd':
                            self.display_clients()
                        elif command == 'e':
                            self.search_clients()
                        elif command == '0':
                            done_sub = True
                        else:
                            print("Bad command!!")

                elif command_menu == '3':
                    self.print_rent_return_submenu()
                    done_sub = False
                    while not done_sub:
                        command = input("\nEnter your command: ")

                        if command == 'a':
                            self.rent_movie_ui()
                        elif command == 'b':
                            self.return_movie_ui()
                        elif command == 'c':
                            self.display_rentals()
                        elif command == '0':
                            done_sub = True
                        else:
                            print("Bad command!!")

                elif command_menu == '4':
                    self.print_statistics_submenu()
                    done_sub = False
                    while not done_sub:
                        command = input("\nEnter your command: ")

                        if command == 'a':
                            self.most_rented_movies()
                        elif command == 'b':
                            self.most_active_clients()
                        elif command == 'c':
                            self.late_rentals()
                        elif command == '0':
                            done_sub = True
                        else:
                            print("Bad command!!")

                elif command_menu == '5':
                    self.undo()

                elif command_menu == '6':
                    self.redo()

                elif command_menu == '0':
                    done = True
                else:
                    print("Bad command!!")
            except (MovieValidatorException, ClientValidatorException, RentalValidatorException, DuplicateIdException,
                    GenreException, ValueError, RentalException, ClientException, MovieException) as error:
                print(str(error))
