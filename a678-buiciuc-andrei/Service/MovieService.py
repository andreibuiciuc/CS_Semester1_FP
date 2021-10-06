from Domain.Exceptions import DuplicateIdException
from Domain.Movie import Movie
from Service.UndoService import FunctionCall, Operation


class MovieService:
    def __init__(self, movie_repository, movie_validator, rental_service, undo_service):
        self._movie_repository = movie_repository
        self._movie_validator = movie_validator
        self._rental_service = rental_service
        self._undo_service = undo_service

    @property
    def get_repo(self):
        return self._movie_repository

    def check_for_id(self, movie_id):
        """
        Method to check for duplicate id in the list of movies.
        :param movie_id: A given id.
        :return: True/False
        """
        for movie in self._movie_repository.get_movies:
            if movie.movie_id == movie_id:
                return False
        return True

    def create_movie(self, movie_id, title, description, genre):
        """
        Method to create a movie object
        :param movie_id: Movie id
        :param title: Movie title
        :param description: Movie description
        :param genre: Movie genre
        :return: A new movie
        """
        if self.check_for_id(movie_id) is False:
            raise DuplicateIdException("Duplicate id!!")
        else:
            movie = Movie(movie_id, title, description, genre)
            self._movie_validator.validate(movie)
            return movie

    def add_movie(self, movie):
        self._movie_repository.add_movie(movie)

    def add_movie_with_rentals(self, movie, rentals):
        self.add_movie(movie)
        for rental in rentals:
            self._rental_service.add_rental(rental)

    def add_movie_record(self, movie):
        self.add_movie(movie)

        fun_undo = FunctionCall(self.remove_movie, movie.movie_id)
        fun_redo = FunctionCall(self.add_movie, movie)
        self._undo_service.record(Operation(fun_undo, fun_redo))

    def remove_movie(self, movie_id):
        self._movie_repository.remove_movie(movie_id)

    def remove_movie_with_rentals(self, movie_id):
        self.remove_movie(movie_id)
        self._rental_service.remove_rental_by_movie(movie_id)

    def remove_movie_record(self, movie_id):
        # Remove a movie from the list of movies.
        movie = self._movie_repository.get_movie(movie_id)
        self.remove_movie(movie_id)

        rentals = self._rental_service.filter_rentals_by_movie(movie_id)

        if len(rentals) == 0:
            fun_undo = FunctionCall(self.add_movie, movie)
            fun_redo = FunctionCall(self.remove_movie, movie_id)
            self._undo_service.record(Operation(fun_undo, fun_redo))
        else:
            self._rental_service.remove_rental_by_movie(movie_id)
            fun_undo = FunctionCall(self.add_movie_with_rentals, movie, rentals)
            fun_redo = FunctionCall(self.remove_movie_with_rentals, movie_id)
            self._undo_service.record(Operation(fun_undo, fun_redo))

    def update_movie(self, movie_id, title, description, genre):
        old_title = self._movie_repository.get_movie(movie_id).title
        old_description = self._movie_repository.get_movie(movie_id).description
        old_genre = self._movie_repository.get_movie(movie_id).genre

        self._movie_repository.update_movie(movie_id, title, description, genre)
        fun_undo = FunctionCall(self.reverse_update, movie_id, old_title, old_description, old_genre)
        fun_redo = FunctionCall(self.update_movie, movie_id, title, description, genre)
        self._undo_service.record(Operation(fun_undo, fun_redo))

    def reverse_update(self, movie_id, old_title, old_description, old_genre):
        self._movie_repository.update_movie(movie_id, old_title, old_description, old_genre)
