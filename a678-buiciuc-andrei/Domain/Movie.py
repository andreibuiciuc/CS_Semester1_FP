class Movie:
    def __init__(self, movie_id, title, description, genre):
        self._movie_id = movie_id
        self._title = title
        self._description = description
        self._genre = genre

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def genre(self):
        return self._genre

    @title.setter
    def title(self, value):
        self._title = value

    @description.setter
    def description(self, value):
        self._description = value

    @genre.setter
    def genre(self, value):
        self._genre = value

    def __str__(self):
        return self._movie_id + ' | ' + self._title + ' | ' + self._description + ' | ' + self._genre


