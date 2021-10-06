from Domain.Exceptions import MovieValidatorException


class MovieValidator:
    @staticmethod
    def validate(movie):
        """
        Method to validate a movie
        :param movie: A given movie
        :return: -
        """
        genre_list = ['action', 'adventure', 'biopic', 'comedy', 'drama', 'family', 'horror', 'musical', 'romance',
                      'thriller']

        errors = []
        if movie.movie_id.isnumeric() is False:
            errors.append('Invalid movie id, id should be 6 digits long.')
        if len(movie.movie_id) == 0:
            errors.append('Invalid movie id, empty value provided.')
        if len(movie.movie_id) > 0 and len(movie.movie_id) != 6:
            errors.append('Invalid movie id, id should be 6 digits long.')
        if len(movie.title) == 0:
            errors.append('Invalid title, empty value provided.')
        if len(movie.description) == 0:
            errors.append('Invalid description, empty value provided.')
        if len(movie.genre) == 0:
            errors.append('Invalid genre, empty value provided.')
        if movie.genre not in genre_list:
            errors.append('Invalid genre, genre is predefined.')
        if len(errors) > 0:
            raise MovieValidatorException(errors)

