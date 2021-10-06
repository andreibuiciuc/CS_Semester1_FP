import datetime


class Rental:
    def __init__(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date=None):
        self._rental_id = rental_id
        self._movie_id = movie_id
        self._client_id = client_id
        self._rented_date = rented_date
        self._due_date = due_date
        self._returned_date = returned_date

    @property
    def rental_id(self):
        return self._rental_id

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def client_id(self):
        return self._client_id

    @property
    def rented_date(self):
        return self._rented_date

    @property
    def due_date(self):
        return self._due_date

    @property
    def returned_date(self):
        return self._returned_date

    @returned_date.setter
    def returned_date(self, value):
        self._returned_date = value

    def __str__(self):
        return self._rental_id + ' | ' + self._movie_id + ' | ' + self._client_id + ' | ' + str(self._rented_date) + \
               ' | ' + str(self._due_date) + ' | ' + str(self._returned_date)

    def __len__(self):
        if self._returned_date is not None:
            return (self._returned_date - self._rented_date).days + 1
        today = datetime.date.today()
        return (today - self._rented_date).days + 1

    @property
    def get_rental_activity(self):
        today = datetime.date.today()
        if self._returned_date is None:
            return (today - self._rented_date).days + 1
        return 0

    @property
    def get_delay(self):
        today = datetime.date.today()
        if self._returned_date is None:
            if today > self._due_date:
                return (today-self._due_date).days + 1
        return 0
