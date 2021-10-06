from Domain.Exceptions import DuplicateIdException, GenreException


class MovieRepository:
    def __init__(self, movie_list):
        self._movie_list = movie_list

    def __len__(self):
        return len(self._movie_list)

    @property
    def get_movies(self):
        return self._movie_list

    def get_movie(self, movie_id):
        index = 0
        for movie in self._movie_list:
            if movie.movie_id == movie_id:
                return movie
            index = index + 1

    def add_movie(self, movie):
        """
        Method to add a movie to the list of movies.
        :param movie: A given movie.
        :return: -
        """
        for m in self._movie_list:
            if m.movie_id == movie.movie_id:
                raise DuplicateIdException('Duplicate id!!')
        self._movie_list.append(movie)

    def remove_movie(self, movie_id):
        """
        Method to remove a movie from the list of movies.
        :param movie_id: A given movie id.
        :return: -
        """
        index = 0
        for m in self._movie_list:
            if m.movie_id == movie_id:
                self._movie_list.pop(index)
                break
            index = index + 1

    def update_movie(self, movie_id, title, description, genre):
        """
        Method to update a movie.
        :param movie_id: A given movie id
        :param title: New title or '' for keeping the old title
        :param description: New description or '' for keeping the old description
        :param genre: New genre or '' for keeping the old genre
        :return: -
        """
        if genre not in ['action', 'adventure', 'biopic', 'comedy', 'drama', 'family', 'horror', 'musical', 'romance',
                         'thriller']:
            raise GenreException("Invalid genre! Genre is predefined.")

        for m in self._movie_list:
            if m.movie_id == movie_id:
                if title != '':
                    m.title = title
                if description != '':
                    m.description = description
                if genre != '':
                    m.genre = genre
                break

