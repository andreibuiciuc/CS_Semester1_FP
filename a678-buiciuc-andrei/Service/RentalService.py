import datetime

from Domain.Exceptions import DuplicateIdException, MovieException, ClientException
from Domain.Rental import Rental
from Service.UndoService import FunctionCall, Operation


class RentalService:
    def __init__(self, rental_repository, rental_validator, movie_repository, client_repository, undo_service):
        self._rental_repository = rental_repository
        self._rental_validator = rental_validator
        self._movie_repository = movie_repository
        self._client_repository = client_repository
        self._undo_service = undo_service

    @property
    def get_repo(self):
        return self._rental_repository

    def check_for_id(self, rental_id):
        """
        Method to check for duplicate id.
        :param rental_id: A given rental id.
        :return: T/F
        """
        for rental in self._rental_repository.get_rentals:
            if rental.rental_id == rental_id:
                return False
        return True

    def check_for_movie(self, movie_id):
        """
        Method to check if the movie is existent.
        :param movie_id: A given movie id.
        :return: T/F
        """
        for movie in self._movie_repository.get_movies:
            if movie.movie_id == movie_id:
                return True
        return False

    def check_for_client(self, client_id):
        """
        Method to check if the client is existent.
        :param client_id: A given client id.
        :return: T/F
        """
        for client in self._client_repository.get_clients:
            if client.client_id == client_id:
                return True
        return False

    def create_rental(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        """
        Method to create a new rental.
        :param rental_id: Rental id
        :param movie_id: Movie id
        :param client_id: Client id
        :param rented_date: Rented date
        :param due_date: Due date
        :param returned_date: Returned day/None
        :return: A new rental
        """
        if self.check_for_id(rental_id) is False:
            raise DuplicateIdException("Duplicate ID!")
        if self.check_for_movie(movie_id) is False:
            raise MovieException("Nonexistent movie!")
        if self.check_for_client(client_id) is False:
            raise ClientException("Nonexistent client!")
        else:
            rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
            self._rental_validator.validate(rental)
            return rental

    def rent_movie(self, rental):
        self._rental_repository.rent_movie(rental)

    def rent_movie_record(self, rental):
        self.rent_movie(rental)
        fun_undo = FunctionCall(self.remove_rental, rental)
        fun_redo = FunctionCall(self.add_rental, rental)
        self._undo_service.record(Operation(fun_undo, fun_redo))

    def return_movie(self, movie_id):
        self._rental_repository.return_movie(movie_id)

    def return_movie_record(self, movie_id):
        rental = self._rental_repository.return_movie(movie_id)
        fun_undo = FunctionCall(self.reverse_return, rental)
        fun_redo = FunctionCall(self.return_movie, rental.movie_id)
        self._undo_service.record(Operation(fun_undo, fun_redo))

    def filter_rentals_by_client(self, client_id):
        rentals = []
        for rental in self._rental_repository.get_rentals:
            if rental.client_id == client_id:
                rentals.append(rental)
        return rentals

    def filter_rentals_by_movie(self, movie_id):
        rentals = []
        for rental in self._rental_repository.get_rentals:
            if rental.movie_id == movie_id:
                rentals.append(rental)
        return rentals

    def remove_rental_by_client(self, client_id):
        rental_delete = self.filter_rentals_by_client(client_id)
        for rental in rental_delete:
            self._rental_repository.remove_rental(rental)

    def remove_rental_by_movie(self, movie_id):
        rental_delete = self.filter_rentals_by_movie(movie_id)
        for rental in rental_delete:
            self._rental_repository.remove_rental(rental)

    def add_rental(self, rental):
        self._rental_repository.add_rental(rental)

    def remove_rental(self, rental):
        self._rental_repository.remove_rental(rental)

    def reverse_return(self, rental):
        self._rental_repository.reverse_return(rental)

    @property
    def most_rented_movies(self):
        result = []
        rental_days = 0
        for movie in self._movie_repository.get_movies:
            okay = False
            for rental in self._rental_repository.get_rentals:
                if movie.movie_id == rental.movie_id:
                    rental_days = len(rental)
                    okay = True
            if okay is True:
                result.append(MovieRentalDays(movie, rental_days))

        return sorted(result, key=lambda m: m.rental_days, reverse=True)

    @property
    def most_active_clients(self):
        result = []
        for client in self._client_repository.get_clients:
            client_activity = 0
            okay = 0
            for rental in self._rental_repository.get_rentals:
                if client.client_id == rental.client_id and rental.returned_date is None:
                    client_activity += rental.get_rental_activity
                    okay = True
            if okay is True:
                result.append(ClientActivity(client, client_activity))

        return sorted(result, key=lambda c: c.client_activity, reverse=True)

    @property
    def late_rentals(self):
        result = []
        rental_delay = 0
        for movie in self._movie_repository.get_movies:
            okay = False
            for rental in self._rental_repository.get_rentals:
                if movie.movie_id == rental.movie_id and datetime.date.today() > rental.due_date:
                    rental_delay = rental.get_delay
                    okay = True

            if rental_delay != 0 and okay is True:
                result.append(LateRentals(movie, rental_delay))

        return sorted(result, key=lambda m: m.movie_delay, reverse=True)


class MovieRentalDays:
    def __init__(self, movie, rental_days):
        self._movie = movie
        self._rental_days = rental_days

    @property
    def movie(self):
        return self._movie

    @property
    def rental_days(self):
        return self._rental_days

    def __str__(self):
        return str(self._rental_days).rjust(3) + " || " + str(self._movie)


class ClientActivity:
    def __init__(self, client, client_activity):
        self._client = client
        self._client_activity = client_activity

    @property
    def client_activity(self):
        return self._client_activity

    def __str__(self):
        return str(self._client_activity).rjust(3) + " || " + str(self._client)


class LateRentals:
    def __init__(self, movie, movie_delay):
        self._movie = movie
        self._movie_delay = movie_delay

    @property
    def movie_delay(self):
        return self._movie_delay

    def __str__(self):
        return str(self._movie_delay).rjust(3) + " || " + str(self._movie)