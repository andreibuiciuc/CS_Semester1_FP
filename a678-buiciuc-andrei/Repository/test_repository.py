import datetime
from unittest import TestCase
from Domain.Client import Client
from Domain.Exceptions import DuplicateIdException, GenreException, RentalException
from Domain.Movie import Movie
from Domain.Rental import Rental
from Repository.ClientRepository import ClientRepository
from Repository.MovieRepository import MovieRepository
from Repository.RentalRepository import RentalRepository

class TestMovieRepository(TestCase):
    def test_repo(self):
        movies = [Movie('111111', 'Joker', 'masterpiece', 'drama'), Movie('222222', 'Inception', 'incredible',
                                                                          'adventure')]
        m_repo = MovieRepository(movies)
        self.assertEqual(len(m_repo), 2)

    def test_add_movie(self):
        movies = [Movie('111111', 'Joker', 'masterpiece', 'drama'), Movie('222222', 'Inception', 'incredible',
                                                                          'adventure')]
        m_repo = MovieRepository(movies)

        m_repo.add_movie(Movie('333333', 'Forrest Gump', 'beautiful', 'family'))
        self.assertEqual(len(m_repo), 3)

        try:
            m_repo.add_movie(Movie('222222', 'Star Wars', 'blockbuster', 'action'))
        except DuplicateIdException:
            self.assertTrue('Ok')

    def test_remove_movie(self):
        movies = [Movie('111111', 'Joker', 'masterpiece', 'drama'), Movie('222222', 'Inception', 'incredible',
                                                                          'adventure')]
        m_repo = MovieRepository(movies)

        m_repo.remove_movie('222222')
        self.assertEqual(len(m_repo), 1)

        m_repo.remove_movie('000000')
        self.assertEqual(len(m_repo), 1)

    def test_update_movie(self):
        movies = [Movie('111111', 'Joker', 'masterpiece', 'drama'), Movie('222222', 'Inception', 'incredible',
                                                                          'adventure')]
        m_repo = MovieRepository(movies)

        m_repo.update_movie('111111', '', 'perfect', 'comedy')
        self.assertEqual(movies[0].movie_id, '111111')
        self.assertEqual(movies[0].title, 'Joker')
        self.assertEqual(movies[0].description, 'perfect')
        self.assertEqual(movies[0].genre, 'comedy')

        try:
            m_repo.update_movie('222222', '', '', 'invalid_genre')
        except GenreException:
            self.assertTrue('Ok')


class TestClientRepo(TestCase):
    def test_repo(self):
        clients = [Client('111111', 'Andrei'), Client('222222', 'John')]
        c_repo = ClientRepository(clients)
        self.assertEqual(len(c_repo), 2)

    def test_add_client(self):
        clients = [Client('111111', 'Andrei'), Client('222222', 'John')]
        c_repo = ClientRepository(clients)

        c_repo.add_client(Client('333333', 'Kevin'))
        self.assertEqual(len(c_repo), 3)

        try:
            c_repo.add_client(Client('222222', 'Client'))
        except DuplicateIdException:
            self.assertTrue('Ok')

    def test_remove_client(self):
        clients = [Client('111111', 'Andrei'), Client('222222', 'John')]
        c_repo = ClientRepository(clients)

        c_repo.remove_client('111111')
        self.assertEqual(len(c_repo), 1)

        c_repo.remove_client('000000')
        self.assertEqual(len(c_repo), 1)

    def test_update_client(self):
        clients = [Client('111111', 'Andrei'), Client('222222', 'John')]
        c_repo = ClientRepository(clients)

        c_repo.update_client('111111', '')
        self.assertEqual(clients[0].client_id, '111111')
        self.assertEqual(clients[0].name, 'Andrei')


class TestRentalRepo(TestCase):
    def test_repo(self):
        rentals = [Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                          datetime.date(2020, 11, 21)),
                   Rental('111111', '123123', '222111', datetime.date(2020, 11, 15),
                          datetime.date(2020, 11, 20), None)]
        r_repo = RentalRepository(rentals)
        self.assertEqual(len(r_repo), 2)

    def test_check_for_movie(self):
        rentals = [Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                          datetime.date(2020, 11, 21)),
                   Rental('222222', '333333', '222000', datetime.date(2020, 11, 15),
                          datetime.date(2020, 11, 20), None)]
        r_repo = RentalRepository(rentals)

        self.assertEqual(r_repo.check_for_movie_availability('123123'), True)
        self.assertEqual(r_repo.check_for_movie_availability('000000'), True)
        self.assertEqual(r_repo.check_for_movie_availability('333333'), False)

    def test_check_for_client(self):
        rentals = [Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                          datetime.date(2020, 11, 21)),
                   Rental('222222', '333333', '222000', datetime.date(2020, 11, 15),
                          datetime.date(2020, 11, 20), None)]
        r_repo = RentalRepository(rentals)

        self.assertEqual(r_repo.check_for_client_compatibility('222111'), True)
        self.assertEqual(r_repo.check_for_client_compatibility('222000'), False)

    def test_rent_movie(self):
        rentals = [Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                          datetime.date(2020, 11, 21)),
                   Rental('222222', '333333', '222000', datetime.date(2020, 11, 15),
                          datetime.date(2020, 11, 20), None)]
        r_repo = RentalRepository(rentals)
        r_repo.rent_movie(Rental('333333', '444123', '500500', datetime.date(2020, 6, 6), datetime.date(2020, 6, 16),
                                 None))
        self.assertEqual(len(r_repo), 3)

        try:
            r_repo.rent_movie(Rental('333333', '333333', '500500', datetime.date(2020, 6, 6), datetime.date(2020, 6, 16),
                                 None))
        except RentalException:
            self.assertTrue('Ok')

        try:
            r_repo.rent_movie(
                Rental('333333', '123123', '222000', datetime.date(2020, 6, 6), datetime.date(2020, 6, 16),
                       None))
        except RentalException:
            self.assertTrue('Ok')

    def test_return_movie(self):
        rentals = [Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                          datetime.date(2020, 11, 21)),
                   Rental('222222', '333333', '222000', datetime.date(2020, 11, 15),
                          datetime.date(2020, 11, 20), None)]
        r_repo = RentalRepository(rentals)

        try:
            r_repo.return_movie('asds')
        except RentalException:
            self.assertTrue('Ok')

        r_repo.return_movie('333333')
        self.assertEqual(r_repo.get_rentals[1].returned_date, datetime.date.today())