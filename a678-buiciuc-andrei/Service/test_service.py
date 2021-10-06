import datetime
from unittest import TestCase
from Domain.Client import Client
from Domain.ClientValidator import ClientValidator
from Domain.Exceptions import DuplicateIdException, MovieValidatorException, MovieException, ClientException
from Domain.Movie import Movie
from Domain.MovieValidator import MovieValidator
from Domain.Rental import Rental
from Domain.RentalValidator import RentalValidator
from Repository.ClientRepository import ClientRepository
from Repository.MovieRepository import MovieRepository
from Repository.RentalRepository import RentalRepository
from Service.ClientService import ClientService
from Service.MovieService import MovieService
from Service.RentalService import RentalService
from Service.UndoService import UndoService


class TestMovieService(TestCase):
    def test_get_repo(self):
        movies = [Movie('111111', 'Joker', 'masterpiece', 'drama'), Movie('222222', 'Interstellar', 'spectacular',
                                                                          'adventure')]
        u_service = UndoService()
        m_repo = MovieRepository(movies)
        m_val = MovieValidator()
        c_repo = ClientRepository([])
        c_val = ClientValidator()
        r_repo = RentalRepository([])
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        m_service = MovieService(m_repo, m_val, r_service, u_service)

        self.assertEqual(m_service.get_repo, m_repo)

    def test_check_for_id(self):
        movies = [Movie('111111', 'Joker', 'masterpiece1', 'drama'), Movie('222222', 'Interstellar', 'spectacular',
                                                                           'adventure')]
        u_service = UndoService()
        m_repo = MovieRepository(movies)
        m_val = MovieValidator()
        c_repo = ClientRepository([])
        c_val = ClientValidator()
        r_repo = RentalRepository([])
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        m_service = MovieService(m_repo, m_val, r_service, u_service)

        self.assertEqual(m_service.check_for_id('111111'), False)
        self.assertEqual(m_service.check_for_id('000000'), True)

    def test_create_movie(self):
        u_service = UndoService()
        m_repo = MovieRepository([])
        m_val = MovieValidator()
        c_repo = ClientRepository([])
        c_val = ClientValidator()
        r_repo = RentalRepository([])
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        m_service = MovieService(m_repo, m_val, r_service, u_service)

        movie = m_service.create_movie('111111', 'Joker', 'masterpiece', 'drama')
        self.assertEqual(movie.movie_id, '111111')
        self.assertEqual(movie.title, 'Joker')
        self.assertEqual(movie.description, 'masterpiece')
        self.assertEqual(movie.genre, 'drama')

        m_repo.add_movie(movie)

        try:
            movie = m_service.create_movie('111111', 'Movie', 'something', 'drama')
        except DuplicateIdException:
            self.assertTrue('Ok')

        try:
            movie = m_service.create_movie('asd', 'Movie', '', 'invalid_genre')
        except MovieValidatorException:
            self.assertTrue('Ok')

    def test_add_movie(self):
        u_service = UndoService()
        movies = [Movie('111111', 'Joker', 'masterpiece', 'drama'), Movie('222222', 'Interstellar', 'spectacular',
                                                                          'adventure')]
        m_repo = MovieRepository(movies)
        m_val = MovieValidator()
        c_repo = ClientRepository([])
        c_val = ClientValidator()
        r_repo = RentalRepository([])
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        m_service = MovieService(m_repo, m_val, r_service, u_service)

        m_service.add_movie(Movie('333333', 'Taxi Driver', 'perfect', 'action'))
        self.assertEqual(len(m_repo), 3)

    def test_remove_movie(self):
        u_service = UndoService()
        movies = [Movie('111111', 'Joker', 'masterpiece', 'drama'), Movie('222222', 'Interstellar', 'spectacular',
                                                                          'adventure')]
        m_repo = MovieRepository(movies)
        m_val = MovieValidator()
        c_repo = ClientRepository([])
        c_val = ClientValidator()
        r_repo = RentalRepository([])
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        m_service = MovieService(m_repo, m_val, r_service, u_service)

        m_service.remove_movie('111111')
        self.assertEqual(len(m_repo), 1)

    def test_update_movie(self):
        u_service = UndoService()
        movies = [Movie('111111', 'Joker', 'masterpiece', 'drama'), Movie('222222', 'Interstellar', 'spectacular',
                                                                          'adventure')]
        m_repo = MovieRepository(movies)
        m_val = MovieValidator()
        c_repo = ClientRepository([])
        c_val = ClientValidator()
        r_repo = RentalRepository([])
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        m_service = MovieService(m_repo, m_val, r_service, u_service)

        m_service.update_movie('111111', 'Taxi Driver', '', 'action')
        self.assertEqual(m_repo.get_movies[0].movie_id, '111111')
        self.assertEqual(m_repo.get_movies[0].title, 'Taxi Driver')
        self.assertEqual(m_repo.get_movies[0].description, 'masterpiece')
        self.assertEqual(m_repo.get_movies[0].genre, 'action')


class TestClientService(TestCase):
    def test_get_repo(self):
        u_service = UndoService()
        clients = [Client('111111', 'Andrei'), Client('222222', 'John')]
        c_repo = ClientRepository(clients)
        m_repo = MovieRepository([])
        m_val = MovieValidator()
        r_repo = RentalRepository([])
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        c_val = ClientValidator()
        c_service = ClientService(c_repo, c_val, r_service, u_service)

        self.assertEqual(c_service.get_repo, c_repo)

    def test_check_for_id(self):
        clients = [Client('111111', 'Andrei'), Client('222222', 'John')]
        u_service = UndoService()
        c_repo = ClientRepository(clients)
        m_repo = MovieRepository([])
        m_val = MovieValidator()
        r_repo = RentalRepository([])
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        c_val = ClientValidator()
        c_service = ClientService(c_repo, c_val, r_service, u_service)

        self.assertEqual(c_service.check_for_id('111111'), False)
        self.assertEqual(c_service.check_for_id('000000'), True)

    def test_create_client(self):
        clients = [Client('111111', 'Andrei'), Client('222222', 'John')]
        u_service = UndoService()
        c_repo = ClientRepository(clients)
        m_repo = MovieRepository([])
        m_val = MovieValidator()
        r_repo = RentalRepository([])
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        c_val = ClientValidator()
        c_service = ClientService(c_repo, c_val, r_service, u_service)

        client = c_service.create_client('333333', 'John')
        self.assertEqual(client.client_id, '333333')
        self.assertEqual(client.name, 'John')

        try:
            c_service.create_client('111111', 'Kevin')
            self.assertFalse('Not ok')
        except DuplicateIdException:
            self.assertTrue('Ok')

    def test_add_client(self):
        clients = [Client('111111', 'Andrei'), Client('222222', 'John')]
        u_service = UndoService()
        c_repo = ClientRepository(clients)
        m_repo = MovieRepository([])
        m_val = MovieValidator()
        r_repo = RentalRepository([])
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        c_val = ClientValidator()
        c_service = ClientService(c_repo, c_val, r_service, u_service)

        c_service.add_client(Client('333333', 'Serban'))
        self.assertEqual(len(c_repo), 3)

        try:
            c_service.add_client(Client('333333', 'Paul'))
        except DuplicateIdException:
            self.assertTrue('OK')

    def test_remove_client(self):
        clients = [Client('111111', 'Andrei'), Client('222222', 'John')]
        u_service = UndoService()
        c_repo = ClientRepository(clients)
        m_repo = MovieRepository([])
        m_val = MovieValidator()
        r_repo = RentalRepository([])
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        c_val = ClientValidator()
        c_service = ClientService(c_repo, c_val, r_service, u_service)

        c_service.remove_client('222222')
        self.assertEqual(len(c_repo), 1)

        c_service.remove_client('000000')
        self.assertEqual(len(c_repo), 1)

    def test_update_client(self):
        clients = [Client('111111', 'Andrei'), Client('222222', 'John')]
        u_service = UndoService()
        c_repo = ClientRepository(clients)
        m_repo = MovieRepository([])
        m_val = MovieValidator()
        r_repo = RentalRepository([])
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        c_val = ClientValidator()
        c_service = ClientService(c_repo, c_val, r_service, u_service)

        c_service.update_client('111111', 'Andrei')
        self.assertEqual(c_repo.get_clients[0].client_id, '111111')
        self.assertEqual(c_repo.get_clients[0].name, 'Andrei')


class TestRentalService(TestCase):
    def test_get_repo(self):
        u_service = UndoService()
        movies = [Movie('111111', 'Joker', 'masterpiece', 'drama'), Movie('222222', 'Interstellar', 'spectacular',
                                                                          'adventure')]
        m_repo = MovieRepository(movies)
        clients = [Client('111111', 'Andrei'), Client('222222', 'John')]
        c_repo = ClientRepository(clients)
        rentals = [Rental('111111', '123123', '222111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                          datetime.date(2020, 11, 21)),
                   Rental('222222', '333333', '222000', datetime.date(2020, 11, 15),
                          datetime.date(2020, 11, 20), None)]
        r_repo = RentalRepository(rentals)
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        self.assertEqual(r_service.get_repo, r_repo)

    def test_check_rental(self):
        u_service = UndoService()
        movies = [Movie('111111', 'Joker', 'masterpiece', 'comedy'), Movie('222222', 'Interstellar', 'spectacular',
                                                                           'adventure')]
        m_repo = MovieRepository(movies)
        clients = [Client('111111', 'Andrew'), Client('222222', 'John')]
        c_repo = ClientRepository(clients)
        rentals = [Rental('111111', '123123', '222112', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                          datetime.date(2020, 11, 21)),
                   Rental('222222', '333333', '222000', datetime.date(2020, 11, 15),
                          datetime.date(2020, 11, 20), None)]
        r_repo = RentalRepository(rentals)
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)

        self.assertEqual(r_service.check_for_id('111111'), False)
        self.assertEqual(r_service.check_for_id('000000'), True)

        self.assertEqual(r_service.check_for_movie('111111'), True)
        self.assertEqual(r_service.check_for_movie('000000'), False)

        self.assertEqual(r_service.check_for_client('111111'), True)
        self.assertEqual(r_service.check_for_client('000000'), False)

    def test_create_rental(self):
        u_service = UndoService()
        movies = [Movie('111111', 'Joker', 'master', 'comedy'), Movie('222222', 'Interstellar', 'spectacular',
                                                                      'adventure')]
        m_repo = MovieRepository(movies)
        clients = [Client('111111', 'Nick'), Client('222222', 'John')]
        c_repo = ClientRepository(clients)
        rentals = [Rental('111111', '123123', '122112', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                          datetime.date(2020, 11, 21)),
                   Rental('222222', '333333', '222000', datetime.date(2020, 11, 15),
                          datetime.date(2020, 11, 20), None)]
        r_repo = RentalRepository(rentals)
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)

        try:
            r_service.create_rental('111111', '222222', '333333', datetime.date(2020, 5, 5),
                                    datetime.date(2020, 5, 15), None)
        except DuplicateIdException:
            self.assertTrue('Ok')

        try:
            r_service.create_rental('333333', '000000', '333333', datetime.date(2020, 5, 5),
                                    datetime.date(2020, 5, 15), None)
        except MovieException:
            self.assertTrue('Ok')

        try:
            r_service.create_rental('333333', '222222', '000000', datetime.date(2020, 5, 5),
                                    datetime.date(2020, 5, 15), None)
        except ClientException:
            self.assertTrue('Ok')

        r_service.create_rental('000000', '222222', '111111', datetime.date(2020, 5, 5),
                                datetime.date(2020, 5, 15), None)

    def test_rent_return_movie(self):
        u_service = UndoService()
        movies = [Movie('111111', 'Joker', 'master', 'horror'), Movie('222222', 'Interstellar', 'spectacular',
                                                                      'adventure')]
        m_repo = MovieRepository(movies)
        clients = [Client('111111', 'NickCave'), Client('222222', 'John')]
        c_repo = ClientRepository(clients)
        rentals = [Rental('111111', '123123', '022112', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                          datetime.date(2020, 11, 21)),
                   Rental('222222', '333333', '222000', datetime.date(2020, 11, 15),
                          datetime.date(2020, 11, 20), None)]
        r_repo = RentalRepository(rentals)
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)
        r_service.rent_movie(Rental('333333', '111111', '111111', datetime.date(2020, 4, 4), datetime.date(2020, 4, 14),
                                    None))
        self.assertEqual(len(r_repo), 3)
        r_service.return_movie('111111')
        self.assertEqual(r_service.get_repo.get_rentals[2].returned_date, datetime.date.today())


class TestUndoService(TestCase):
    def test_add_remove(self):
        u_service = UndoService()
        movies = [Movie('111111', 'Joker', 'master', 'horror'), Movie('222222', 'Interstellar', 'spectacular',
                                                                      'adventure')]
        m_repo = MovieRepository(movies)
        m_val = MovieValidator()
        clients = [Client('111111', 'NickCave'), Client('222222', 'John')]
        c_repo = ClientRepository(clients)
        c_val = ClientValidator()
        rentals = [Rental('111111', '111111', '111111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                          datetime.date(2020, 11, 21)),
                   Rental('222222', '333333', '222222', datetime.date(2020, 11, 15),
                          datetime.date(2020, 11, 20), None)]
        r_repo = RentalRepository(rentals)
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)

        m_service = MovieService(m_repo, m_val, r_service, u_service)
        c_service = ClientService(c_repo, c_val, r_service, u_service)

        m_service.add_movie_record(Movie('333333', 'movie', 'new', 'drama'))
        u_service.undo()
        self.assertEqual(len(m_repo), 2)
        u_service.redo()
        self.assertEqual(len(m_repo), 3)

        m_service.remove_movie_record('333333')
        u_service.undo()
        self.assertEqual(len(m_repo), 3)
        u_service.redo()
        self.assertEqual(len(m_repo), 2)

        m_service.remove_movie_record('222222')
        u_service.undo()
        self.assertEqual(len(m_repo), 2)

        m_service.remove_movie_record('111111')
        self.assertEqual(len(m_repo), 1)
        self.assertEqual(len(r_repo), 0)
        u_service.undo()
        self.assertEqual(len(m_repo), 2)
        self.assertEqual(len(r_repo), 1)
        u_service.redo()
        self.assertEqual(len(m_repo), 1)
        self.assertEqual(len(r_repo), 0)

        c_service.add_client_record(Client('333333', 'Me'))
        u_service.undo()
        self.assertEqual(len(c_repo), 2)
        u_service.redo()
        self.assertEqual(len(c_repo), 3)

        c_service.remove_client_record('333333')
        u_service.undo()
        self.assertEqual(len(c_repo), 3)
        u_service.redo()
        self.assertEqual(len(c_repo), 2)

        c_service.remove_client_record('222222')
        u_service.undo()
        self.assertEqual(len(c_repo), 2)

        c_service.remove_client_record('111111')
        self.assertEqual(len(c_repo), 1)
        self.assertEqual(len(r_repo), 0)
        u_service.undo()
        self.assertEqual(len(c_repo), 2)
        self.assertEqual(len(r_repo), 0)
        u_service.redo()
        self.assertEqual(len(c_repo), 1)
        self.assertEqual(len(r_repo), 0)

    def test_update(self):
        u_service = UndoService()
        movies = [Movie('111111', 'Joker', 'master', 'horror'), Movie('222222', 'Interstellar', 'spectacular',
                                                                      'adventure')]
        m_repo = MovieRepository(movies)
        m_val = MovieValidator()
        clients = [Client('111111', 'NickCave'), Client('222222', 'John')]
        c_repo = ClientRepository(clients)
        c_val = ClientValidator()
        rentals = [Rental('111111', '111111', '111111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                          datetime.date(2020, 11, 21)),
                   Rental('222222', '333333', '222000', datetime.date(2020, 11, 15),
                          datetime.date(2020, 11, 20), None)]
        r_repo = RentalRepository(rentals)
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)

        m_service = MovieService(m_repo, m_val, r_service, u_service)
        c_service = ClientService(c_repo, c_val, r_service, u_service)

        m_service.update_movie('111111', '', '', 'drama')
        self.assertEqual(m_repo.get_movies[0].genre, 'drama')
        u_service.undo()
        self.assertEqual(m_repo.get_movies[0].genre, 'horror')
        u_service.redo()
        self.assertEqual(m_repo.get_movies[0].genre, 'drama')

        c_service.update_client('111111', 'name')
        self.assertEqual(c_repo.get_clients[0].name, 'name')
        u_service.undo()
        self.assertEqual(c_repo.get_clients[0].name, 'NickCave')
        u_service.redo()
        self.assertEqual(c_repo.get_clients[0].name, 'name')

    def test_rentals(self):
        u_service = UndoService()
        movies = [Movie('111111', 'Joker', 'master', 'horror'), Movie('222222', 'Interstellar', 'spectacular',
                                                                      'adventure')]
        m_repo = MovieRepository(movies)
        m_val = MovieValidator()
        clients = [Client('111111', 'NickCave'), Client('222222', 'John')]
        c_repo = ClientRepository(clients)
        c_val = ClientValidator()
        rentals = [Rental('111111', '111111', '111111', datetime.date(2020, 11, 15), datetime.date(2020, 11, 20),
                          datetime.date(2020, 11, 21)),
                   Rental('222222', '333333', '222000', datetime.date(2020, 11, 15),
                          datetime.date(2020, 11, 20), None)]
        r_repo = RentalRepository(rentals)
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)

        m_service = MovieService(m_repo, m_val, r_service, u_service)
        c_service = ClientService(c_repo, c_val, r_service, u_service)

        r_service.rent_movie_record(Rental('333333', '111111', '111111', datetime.date(2020, 12, 1),
                                           datetime.date(2020, 12, 5), None))
        self.assertEqual(len(r_repo), 3)
        u_service.undo()
        self.assertEqual(len(r_repo), 2)
        u_service.redo()
        self.assertEqual(len(r_repo), 3)

        r_service.return_movie_record('111111')
        self.assertEqual(r_repo.get_rentals[2].returned_date, datetime.date.today())
        u_service.undo()
        self.assertEqual(r_repo.get_rentals[2].returned_date, None)
        u_service.redo()
        self.assertEqual(r_repo.get_rentals[2].returned_date, datetime.date.today())