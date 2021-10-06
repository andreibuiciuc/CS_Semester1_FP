import datetime
from unittest import TestCase

from Domain.Client import Client
from Domain.ClientValidator import ClientValidator
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


class TestStatistics(TestCase):
    def test_statistics(self):
        joker = Movie('100000', 'Joker', 'masterpiece', 'drama')
        inception = Movie('100001', 'Inception', 'fantastic', 'adventure')
        forrest = Movie('100002', 'Forrest Gump', 'beautiful', 'family')
        titanic = Movie('100003', 'Titanic', 'classic', 'romance')

        movies = [joker, inception, forrest, titanic]

        andrew = Client('111000', 'Andrew')
        john = Client('111001', 'John')
        paul = Client('111002', 'Paul')
        claudia = Client('111003', 'Claudia')

        clients = [andrew, john, paul, claudia]

        rentals = [Rental('111111', '100000', '111000', datetime.date(2020, 5, 5), datetime.date(2020, 5, 15),
                          datetime.date(2020, 5, 20)),
                   Rental('222222', '100001', '111001', datetime.date(2020, 6, 6), datetime.date(2020, 6, 10),
                          datetime.date(2020, 6, 8)),
                   Rental('333333', '100002', '111002', datetime.date(2020, 7, 7), datetime.date(2020, 7, 12),
                          datetime.date(2020, 7, 27))]

        u_service = UndoService()
        m_repo = MovieRepository(movies)
        m_val = MovieValidator()

        c_repo = ClientRepository(clients)
        c_val = ClientValidator()

        r_repo = RentalRepository(rentals)
        r_val = RentalValidator()
        r_service = RentalService(r_repo, r_val, m_repo, c_repo, u_service)

        m_service = MovieService(m_repo, m_val, r_service, u_service)
        c_service = MovieService(m_repo, c_val, r_service, u_service)

        most_rented_movies = r_service.most_rented_movies
        self.assertEqual(most_rented_movies[0].rental_days, 21)
        self.assertEqual(most_rented_movies[1].rental_days, 16)
        self.assertEqual(most_rented_movies[2].rental_days, 3)

        most_active_clients = r_service.most_active_clients
        self.assertEqual(len(most_active_clients), 0)

        late_rentals = r_service.late_rentals
        self.assertEqual(len(late_rentals), 0)



