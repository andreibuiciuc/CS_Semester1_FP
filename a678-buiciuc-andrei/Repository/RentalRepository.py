import datetime

from Domain.Exceptions import RentalException


class RentalRepository:
    def __init__(self, rental_list):
        self._rental_list = rental_list

    def __len__(self):
        return len(self._rental_list)

    @property
    def get_rentals(self):
        return self._rental_list

    def check_for_movie_availability(self, movie_id):
        """
        Method to check if the movie is available.
        :param movie_id: A given movie id.
        :return: T/F
        """
        for rental in self._rental_list:
            if rental.movie_id == movie_id:
                if rental.returned_date is None:  # means that the movie is not returned
                    return False
        return True

    def check_for_client_compatibility(self, client_id):
        """
        Method to check if the client is compatible.
        :param client_id: A given client id.
        :return:
        """
        for rental in self._rental_list:
            if rental.client_id == client_id:
                if rental.returned_date is None and datetime.date.today() > rental.due_date:
                    return False
        return True

    def rent_movie(self, rental):
        """
        Method for rental.
        :param rental: A rental.
        :return: -
        """
        if self.check_for_movie_availability(rental.movie_id) is False:
            raise RentalException("Movie unavailable :^(")
        if self.check_for_client_compatibility(rental.client_id) is False:
            raise RentalException("Client incompatible!")

        self._rental_list.append(rental)

    def return_movie(self, movie_id):
        """
        Method for return
        :param movie_id: A given movie id.
        :return: -
        """
        if movie_id == '' or movie_id.isnumeric() is False or len(movie_id) != 6:
            raise RentalException("Invalid movie id!")

        for rental in self._rental_list:
            if rental.movie_id == movie_id and rental.returned_date is None:
                rental.returned_date = datetime.date.today()
                return rental

    def add_rental(self, rental):
        self._rental_list.append(rental)

    def remove_rental(self, rental):
        self._rental_list.remove(rental)

    def reverse_return(self, rental):
        for r in self._rental_list:
            if r.rental_id == rental.rental_id:
                r.returned_date = None
