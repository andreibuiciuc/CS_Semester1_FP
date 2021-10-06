import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from functools import partial

from Domain.Exceptions import MovieValidatorException, RentalValidatorException, ClientValidatorException, \
    DuplicateIdException, GenreException, RentalException, ClientException, MovieException


class GUI:
    def __init__(self, master, movie_service, client_service, rental_service, undo_service):
        self._master = master
        self._movie_service = movie_service
        self._client_service = client_service
        self._rental_service = rental_service
        self._undo_service = undo_service

    def movie_window(self):
        window = tk.Toplevel(self._master)
        window.geometry('300x200')
        button_add = Button(window, text="Add a movie", command=self.add_movie_gui, width=20)
        button_add.pack()
        button_remove = Button(window, text="Remove a movie", command=self.remove_movie_gui, width=20)
        button_remove.pack()
        button_update = Button(window, text="Update a movie", command=self.update_movie_gui, width=20)
        button_update.pack()
        button_display = Button(window, text="Display movies", command=self.display_movies, width=20)
        button_display.pack()
        button_search = Button(window, text="Search movies", command=self.search_movies_gui, width=20)
        button_search.pack()

    def client_window(self):
        window = tk.Toplevel(self._master)
        window.geometry('300x200')
        button_add = Button(window, text="Add a client", command=self.add_client_gui, width=20)
        button_add.pack()
        button_remove = Button(window, text="Remove a client", command=self.remove_client_gui, width=20)
        button_remove.pack()
        button_update = Button(window, text="Update a client", command=self.update_client_gui, width=20)
        button_update.pack()
        button_display = Button(window, text="Display clients", command=self.display_clients, width=20)
        button_display.pack()
        button_search = Button(window, text="Search clients", command=self.search_clients_gui, width=20)
        button_search.pack()

    def rental_window(self):
        window = tk.Toplevel(self._master)
        window.geometry('300x200')
        button_rent = Button(window, text="Rent a movie", command=self.rent_movie_gui, width=20)
        button_rent.pack()
        button_return = Button(window, text="Return a movie", command=self.return_movie_gui, width=20)
        button_return.pack()
        button_display = Button(window, text="Display rentals", command=self.display_rentals, width=20)
        button_display.pack()

    def statistics_window(self):
        window = tk.Toplevel(self._master)
        window.geometry('300x200')
        button_a = Button(window, text="Most rented movies", command=self.most_rented_movies, width=20)
        button_a.pack()
        button_b = Button(window, text="Most active clients", command=self.most_active_clients, width=20)
        button_b.pack()
        button_c = Button(window, text="Late rentals", command=self.late_rentals, width=20)
        button_c.pack()

    def get_inputs_add_movie(self, id_entry, title_entry, des_entry, genre_entry):
        movie_id = id_entry.get()
        title = title_entry.get()
        description = des_entry.get()
        genre = genre_entry.get()
        try:
            movie = self._movie_service.create_movie(movie_id, title, description, genre)
            self._movie_service.add_movie_record(movie)
            messagebox.showinfo("Movie added.")
        except (MovieValidatorException, DuplicateIdException) as e:
            messagebox.showinfo("Error")

    def add_movie_gui(self):
        window = tk.Toplevel(self._master)
        id_label = tk.Label(window, text="Movie id")
        id_label.pack()
        id_entry = tk.Entry(window)
        id_entry.pack()

        title_label = tk.Label(window, text="Title")
        title_label.pack()
        title_entry = tk.Entry(window)
        title_entry.pack()

        des_label = tk.Label(window, text="Description")
        des_label.pack()
        des_entry = tk.Entry(window)
        des_entry.pack()

        genre_label = tk.Label(window, text="Genre")
        genre_label.pack()
        genre_entry = tk.Entry(window)
        genre_entry.pack()

        button = tk.Button(window, text="Done", command=partial(self.get_inputs_add_movie, id_entry, title_entry,
                                                                des_entry, genre_entry))
        button.pack()

    def get_inputs_remove_movie(self, id_entry):
        movie_id = id_entry.get()
        self._movie_service.remove_movie_record(movie_id)

    def remove_movie_gui(self):
        window = tk.Toplevel(self._master)
        id_label = tk.Label(window, text="Movie id for removal")
        id_label.pack()
        id_entry = tk.Entry(window)
        id_entry.pack()
        button = tk.Button(window, text="Done", command=partial(self.get_inputs_remove_movie, id_entry))
        button.pack()

    def get_input_movie_update(self, id_entry, title_entry, des_entry, genre_entry):
        movie_id = id_entry.get()
        title = title_entry.get()
        description = des_entry.get()
        genre = genre_entry.get()
        try:
            self._movie_service.update_movie(movie_id, title, description, genre)
            messagebox.showinfo("Updated")
        except (GenreException, AttributeError) as e:
            messagebox.showinfo("Error")

    def update_movie_gui(self):
        window = tk.Toplevel(self._master)
        id_label = tk.Label(window, text="Introduce the movie id for update")
        id_label.pack()
        id_entry = tk.Entry(window)
        id_entry.pack()

        title_label = tk.Label(window, text="New title")
        title_label.pack()
        title_entry = tk.Entry(window)
        title_entry.pack()

        des_label = tk.Label(window, text="New description")
        des_label.pack()
        des_entry = tk.Entry(window)
        des_entry.pack()

        genre_label = tk.Label(window, text="New genre")
        genre_label.pack()
        genre_entry = tk.Entry(window)
        genre_entry.pack()

        button = tk.Button(window, text="Done", command=partial(self.get_input_movie_update, id_entry, title_entry,
                                                                des_entry, genre_entry))
        button.pack()

    def display_movies(self):
        window = tk.Toplevel(self._master)
        text = tk.Text(window, height=20, width=50)
        text.pack()
        for movie in self._movie_service.get_repo.get_movies:
            text.insert(tk.END, str(movie) + '\n')

    def search_movies(self, window, search_entry):
        search = search_entry.get()
        text = tk.Text(window, height=20, width=50)
        text.pack()
        valid_search = False
        for movie in self._movie_service.get_repo.get_movies:
            match_id = re.search(search, movie.movie_id)
            match_title = re.search(search.lower(), movie.title.lower())
            match_description = re.search(search.lower(), movie.description.lower())
            match_genre = re.search(search.lower(), movie.genre.lower())
            if match_id or match_title or match_description or match_genre:
                valid_search = True
                text.insert(tk.END, str(movie) + '\n')
        if valid_search is False:
            text.insert(tk.END, "No search results.")

    def search_movies_gui(self):
        window = tk.Toplevel(self._master)
        search_label = tk.Label(window, text="Search movies")
        search_label.pack()
        search_entry = tk.Entry(window)
        search_entry.pack()
        button = tk.Button(window, text="Search", command=partial(self.search_movies, window, search_entry))
        button.pack()

    def get_input_add_client(self, id_entry, name_entry):
        client_id = id_entry.get()
        name = name_entry.get()
        try:
            client = self._client_service.create_client(client_id, name)
            self._client_service.add_client_record(client)
            messagebox.showinfo("Client added")
        except (ClientValidatorException, DuplicateIdException) as e:
            messagebox.showinfo("Error")

    def add_client_gui(self):
        window = tk.Toplevel(self._master)
        id_label = tk.Label(window, text="Client id")
        id_label.pack()
        id_entry = tk.Entry(window)
        id_entry.pack()

        name_label = tk.Label(window, text="Name")
        name_label.pack()
        name_entry = tk.Entry(window)
        name_entry.pack()

        button = tk.Button(window, text="Done", command=partial(self.get_input_add_client, id_entry, name_entry))
        button.pack()

    def get_input_remove_client(self, id_entry):
        client_id = id_entry.get()
        self._client_service.remove_client_record(client_id)

    def remove_client_gui(self):
        window = tk.Toplevel(self._master)
        id_label = tk.Label(window, text="Client id for removal")
        id_label.pack()
        id_entry = tk.Entry(window)
        id_entry.pack()
        button = tk.Button(window, text="Done", command=partial(self.get_input_remove_client, id_entry))
        button.pack()

    def get_input_update_client(self, id_entry, name_entry):
        client_id = id_entry.get()
        name = name_entry.get()
        try:
            self._client_service.update_client(client_id, name)
            messagebox.showinfo("Updated")
        except AttributeError as e:
            messagebox.showinfo("Error")

    def update_client_gui(self):
        window = tk.Toplevel(self._master)
        id_label = tk.Label(window, text="Client id for update")
        id_label.pack()
        id_entry = tk.Entry(window)
        id_entry.pack()

        name_label = tk.Label(window, text="New name")
        name_label.pack()
        name_entry = tk.Entry(window)
        name_entry.pack()

        button = tk.Button(window, text="Done", command=partial(self.get_input_update_client, id_entry, name_entry))
        button.pack()

    def display_clients(self):
        window = tk.Toplevel(self._master)
        text = tk.Text(window, height=20, width=50)
        text.pack()
        for client in self._client_service.get_repo.get_clients:
            text.insert(tk.END, str(client) + '\n')

    def search_clients(self, window, search_entry):
        search = search_entry.get()
        text = tk.Text(window, height=20, width=50)
        text.pack()
        valid_search = False
        for client in self._client_service.get_repo.get_clients:
            match_id = re.search(search, client.client_id)
            match_name = re.search(search.lower(), client.name.lower())
            if match_id or match_name:
                valid_search = True
                text.insert(tk.END, str(client) + '\n')
        if valid_search is False:
            text.insert(tk.END, "No search result.")

    def search_clients_gui(self):
        window = tk.Toplevel(self._master)
        search_label = tk.Label(window, text="Search clients")
        search_label.pack()
        search_entry = tk.Entry(window)
        search_entry.pack()

        button = tk.Button(window, text="Search", command=partial(self.search_clients, window, search_entry))
        button.pack()

    def rent_movie(self, id_entry, id_m_entry, id_c_entry, year_entry, month_entry, day_entry):
        try:
            rent_id = id_entry.get()
            movie_id = id_m_entry.get()
            client_id = id_c_entry.get()
            rented_date = datetime.date.today()
            year = int(year_entry.get())
            month = int(month_entry.get())
            day = int(day_entry.get())
            due_date = datetime.date(year, month, day)

            rental = self._rental_service.create_rental(rent_id, movie_id, client_id, rented_date, due_date, None)
            self._rental_service.rent_movie_record(rental)
            messagebox.showinfo("Success", "Movie rented.")
        except (DuplicateIdException, ClientException, MovieException, RentalException, ValueError) as e:
            messagebox.showinfo("Error", str(e))

    def rent_movie_gui(self):
        window = tk.Toplevel(self._master)
        id_label = tk.Label(window, text="Rental id")
        id_label.pack()
        id_entry = tk.Entry(window)
        id_entry.pack()

        id_m_label = tk.Label(window, text="Movie id")
        id_m_label.pack()
        id_m_entry = tk.Entry(window)
        id_m_entry.pack()

        id_c_label = tk.Label(window, text="Client id")
        id_c_label.pack()
        id_c_entry = tk.Entry(window)
        id_c_entry.pack()

        year_label = tk.Label(window, text="Year")
        year_label.pack()
        year_entry = tk.Entry(window)
        year_entry.pack()

        month_label = tk.Label(window, text="Month")
        month_label.pack()
        month_entry = tk.Entry(window)
        month_entry.pack()

        day_label = tk.Label(window, text="Day")
        day_label.pack()
        day_entry = tk.Entry(window)
        day_entry.pack()

        button = tk.Button(window, text="Rent", command=partial(self.rent_movie, id_entry, id_m_entry, id_c_entry,
                                                                year_entry, month_entry, day_entry))
        button.pack()

    def return_movie(self, id_entry):
        movie_id = id_entry.get()
        try:
            self._rental_service.return_movie_record(movie_id)
            messagebox.showinfo("Success", "Movie returned")
        except RentalException as e:
            messagebox.showinfo("Error", str(e))

    def return_movie_gui(self):
        window = tk.Toplevel(self._master)
        id_label = tk.Label(window, text="Introduce the movie id for return")
        id_label.pack()
        id_entry = tk.Entry(window)
        id_entry.pack()

        button = tk.Button(window, text='Return', command=partial(self.return_movie, id_entry))
        button.pack()

    def display_rentals(self):
        window = tk.Toplevel(self._master)
        text = tk.Text(window, height=20, width=100)
        text.pack()
        for rental in self._rental_service.get_repo.get_rentals:
            text.insert(tk.END, str(rental) + '\n')

    def most_rented_movies(self):
        window = tk.Toplevel(self._master)
        text = tk.Text(window, height=20, width=100)
        text.pack()
        for movie in self._rental_service.most_rented_movies:
            text.insert(tk.END, str(movie) + '\n')

    def most_active_clients(self):
        window = tk.Toplevel(self._master)
        text = tk.Text(window, height=20, width=100)
        text.pack()
        for client in self._rental_service.most_active_clients:
            text.insert(tk.END, str(client) + '\n')

    def late_rentals(self):
        window = tk.Toplevel(self._master)
        text = tk.Text(window, height=20, width=100)
        text.pack()
        for movie in self._rental_service.late_rentals:
            text.insert(tk.END, str(movie) + '\n')

    def undo(self):
        self._undo_service.undo()

    def redo(self):
        self._undo_service.redo()

    def menu(self):
        label = Label(text="Hello and welcome to Movie Rental. Choose a command below.")
        label.pack()
        button_movies = Button(self._master, text="1. Manage movies", command=self.movie_window, width=20)
        button_movies.pack()
        button_clients = Button(self._master, text="2. Manage clients", command=self.client_window, width=20)
        button_clients.pack()
        button_rentals = Button(self._master, text="3. Manage rentals", command=self.rental_window, width=20)
        button_rentals.pack()
        button_stats = Button(self._master, text="4. Show statistics", command=self.statistics_window, width=20)
        button_stats.pack()
        button_undo = Button(text="5. Undo", command=self.undo, width=20)
        button_undo.pack()
        button_redo = Button(text="6. Redo", command=self.redo, width=20)
        button_redo.pack()

    def start_gui(self):
        self._master.title("Movie Rental")
        self.menu()
