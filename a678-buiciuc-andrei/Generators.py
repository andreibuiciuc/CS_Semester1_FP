import datetime
import random

from Domain.Client import Client
from Domain.Movie import Movie
from Domain.Rental import Rental


def get_id_string(length):
    chars = '0123456789'
    result = ''.join(random.choice(chars) for index in range(length))
    return result


def get_date():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = 2020
    date = datetime.date(year, month, day)
    return date


def check_movie_title(m_list, title):
    for movie in m_list:
        if movie.title == title:
            return False
    return True


def generate_movies_init():
    generated_list = []

    title_list = ['Titanic', 'Shutter Island', 'Interstellar', 'Inception', 'Tenet', 'Star Wars', 'Forrest Gump',
                  'Taxi Driver', 'Joker', 'Batman', 'Dunkirk', 'Lord Of the Rings', 'Harry Potter']
    description_list = ['classic', 'blockbuster', 'underrated', 'overrated', 'genius', 'popcorn ready',
                        'lovely', 'best', 'incredible', 'so good']
    genre_list = ['action', 'comedy', 'romance', 'thriller', 'biopic',
                  'adventure', 'horror', 'musical', 'drama', 'family']

    i = 0
    while i < 10:
        movie_id = get_id_string(6)
        title = random.choice(title_list)
        description = random.choice(description_list)
        genre = random.choice(genre_list)

        movie = Movie(movie_id, title, description, genre)
        if check_movie_title(generated_list, movie.title) is True:
            generated_list.append(movie)
            i = i + 1

    return generated_list


def check_name(c_list, name):
    for client in c_list:
        if client.name == name:
            return False
    return True


def generate_clients_init():
    generated_list = []
    name_list = ['Claudia', 'Andrew', 'Andra', 'Sandra', 'Serban', 'Paul', 'John', 'Thomas', 'Esteban', 'Julius',
                 'Ricardo']
    i = 0
    while i < 10:
        client_id = get_id_string(6)
        name = random.choice(name_list)
        client = Client(client_id, name)
        if check_name(generated_list, client.name) is True:
            generated_list.append(client)
            i = i + 1
    return generated_list


def check_movie(r_repo, m_id):
    for rental in r_repo:
        if rental.movie_id == m_id:
            if rental.returned_date is None:
                return False
    return True


def check_client(r_repo, c_id):
    for rental in r_repo:
        if rental.client_id == c_id:
            if rental.returned_date is None and datetime.date.today() > rental.due_date:
                return False
    return True


def generate_rentals_init(m_repo, c_repo):
    generated_list = []
    movie_id_list = []
    client_id_list = []
    ret_or_not = [get_date, None]
    for movie in m_repo:
        movie_id_list.append(movie.movie_id)
    for client in c_repo:
        client_id_list.append(client.client_id)

    today = datetime.date.today()
    i = 0
    while i < 10:
        rental_id = get_id_string(6)
        movie_id = random.choice(movie_id_list)
        client_id = random.choice(client_id_list)

        rented_date = get_date()

        # due_date = get_date()

        due_date = rented_date + datetime.timedelta(10)
        returned_date = random.choice(ret_or_not)

        if returned_date is not None:
            returned_date_d = returned_date()

            if rented_date <= due_date and rented_date <= returned_date_d and rented_date <= today:
                rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date_d)
                if check_movie(generated_list, movie_id) is True and check_client(generated_list, client_id) is True:
                    generated_list.append(rental)
                    i += 1
        else:
            if rented_date <= due_date and rented_date <= today:
                rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
                if check_movie(generated_list, movie_id) is True and check_client(generated_list, client_id) is True:
                    generated_list.append(rental)
                    i += 1
    return generated_list

