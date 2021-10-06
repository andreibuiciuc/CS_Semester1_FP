import datetime
from unittest import TestCase

from Domain.Client import Client
from Domain.ClientValidator import ClientValidator
from Domain.Exceptions import MovieValidatorException, ClientValidatorException, RentalValidatorException, \
    MovieException, ClientException, RentalException, DuplicateIdException, GenreException
from Domain.Movie import Movie
from Domain.MovieValidator import MovieValidator
from Domain.Rental import Rental
from Domain.RentalValidator import RentalValidator


class TestMovieDomain(TestCase):
    def test_movie(self):
        movie = Movie('111111', 'Taxi Driver', 'perfect', 'action')
        self.assertEqual(movie.movie_id, '111111')
        self.assertEqual(movie.title, 'Taxi Driver')
        self.assertEqual(movie.description, 'perfect')
        self.assertEqual(movie.genre, 'action')

        try:
            movie = Movie('asd', 'Title', 'something', 'drama')
            movie_val = MovieValidator()
            movie_val.validate(movie)
        except MovieValidatorException as error:
            self.assertTrue(str(error), 'Invalid movie id, id should be 6 digits long.')
            self.assertTrue('Ok')

        try:
            movie = Movie('', '', '', '')
            movie_val = MovieValidator()
            movie_val.validate(movie)
        except MovieValidatorException:
            self.assertTrue('Ok')

    def test_movie_str(self):
        movie = Movie('111111', 'Taxi Driver', 'perfect', 'action')
        movie_str = '111111 | Taxi Driver | perfect | action'
        self.assertEqual(str(movie), movie_str)

    def test_movie_setter(self):
        movie = Movie('111111', 'title', 'description', 'genre')
        movie.genre = 'comedy'
        movie.title = 'new'
        movie.description = 'new'
        self.assertEqual(movie.title, 'new')
        self.assertEqual(movie.description, 'new')
        self.assertEqual(movie.genre, 'comedy')


class TestClientDomain(TestCase):
    def test_client(self):
        client = Client('111111', 'Andrei')
        self.assertEqual(client.client_id, '111111')
        self.assertEqual(client.name, 'Andrei')

        try:
            client = Client('asd', 'sas')
            client_val = ClientValidator()
            client_val.validate(client)
        except ClientValidatorException as error:
            self.assertTrue(str(error), 'Invalid client id, id should be 6 digits long.')
            self.assertTrue('Ok')

        try:
            client = Client('1111117', '')
            client_val = ClientValidator()
            client_val.validate(client)
        except ClientValidatorException:
            self.assertTrue('Ok')

        try:
            client = Client('', '')
            client_val = ClientValidator()
            client_val.validate(client)
        except ClientValidatorException:
            self.assertTrue('Ok')

    def test_client_str(self):
        client = Client('111111', 'Andrei')
        client_str = '111111 | Andrei'
        self.assertEqual(str(client), client_str)

    def test_client_setter(self):
        client = Client('111111', 'Andrei')
        client.name = 'Andrew'
        self.assertEqual(client.name, 'Andrew')


class TestRentalDomain(TestCase):
    def test_rental(self):
        rental = Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                        datetime.date(2020, 11, 21))
        self.assertEqual(rental.rental_id, '111111')
        self.assertEqual(rental.movie_id, '123123')
        self.assertEqual(rental.client_id, '222111')
        self.assertEqual(rental.rented_date, datetime.date(2020, 11, 15))
        self.assertEqual(rental.due_date, datetime.date(2020, 11, 20))
        self.assertEqual(rental.returned_date, datetime.date(2020, 11, 21))

        try:
            rental = Rental('11a', '111222', '444444', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                            datetime.date(2020, 11, 21))
            r_val = RentalValidator()
            r_val.validate(rental)
        except RentalValidatorException as error:
            self.assertTrue(str(error), 'Invalid rental id, id should be 6 digits long')
            self.assertTrue('Ok')

        try:
            rental = Rental('111111', '', '', datetime.date(2020, 11, 15), datetime.date(2020, 11, 10),
                            datetime.date(2020, 11, 21))
            r_val = RentalValidator()
            r_val.validate(rental)
        except RentalValidatorException:
            self.assertTrue('Ok')

    def test_len_rental(self):
        rental = Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                        datetime.date(2020, 11, 21))

        self.assertEqual(len(rental), 7)

        rental = Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20), None)
        today = datetime.date.today()
        length = (today - rental.rented_date).days + 1
        self.assertEqual(len(rental), length)

    def test_str_rental(self):
        rental = Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                        datetime.date(2020, 11, 21))
        rental_str = '111111 | 123123 | 222111 | 2020-11-15 | 2020-11-20 | 2020-11-21'
        self.assertEqual(str(rental), rental_str)

    def test_rental_activity(self):
        rental = Rental('111111', '123123', '222110', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                        datetime.date(2020, 11, 21))
        self.assertEqual(rental.get_rental_activity, 0)

        rental = Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20), None)
        today = datetime.date.today()
        r_activity = (today - rental.rented_date).days + 1
        self.assertEqual(rental.get_rental_activity, r_activity)

    def test_rental_delay(self):
        rental = Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                        datetime.date(2020, 11, 21))
        self.assertEqual(rental.get_delay, 0)

        rental = Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20), None)
        today = datetime.date.today()
        r_delay = (today - rental.due_date).days + 1
        self.assertEqual(rental.get_delay, r_delay)

    def test_rental_setter(self):
        rental = Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                        datetime.date(2020, 11, 21))
        rental.returned_date = datetime.date(2020, 12, 12)
        self.assertEqual(rental.returned_date, datetime.date(2020, 12, 12))


class TestExceptions(TestCase):
    def test_exceptions(self):
        self.assertRaises(MovieException)
        self.assertRaises(ClientException)
        self.assertRaises(RentalException)
        self.assertRaises(DuplicateIdException)
        self.assertRaises(GenreException)
        self.assertRaises(MovieValidatorException)
        self.assertRaises(ClientValidatorException)
        self.assertRaises(RentalValidatorException)