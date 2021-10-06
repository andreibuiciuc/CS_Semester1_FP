from Console.GUI import GUI
from Console.UserInterface import UI
from Domain.ClientValidator import ClientValidator
from Domain.MovieValidator import MovieValidator
from Domain.RentalValidator import RentalValidator
from Repository.ClientRepository import ClientRepository
from Generators import generate_movies_init, generate_clients_init, generate_rentals_init
from Repository.MovieRepository import MovieRepository
from Repository.RentalRepository import RentalRepository
from Service.ClientService import ClientService
from Service.MovieService import MovieService
from Service.RentalService import RentalService
from Service.UndoService import UndoService
from tkinter import Tk

undo_service = UndoService()

m_repo = generate_movies_init()
movie_repository = MovieRepository(m_repo)
movie_validator = MovieValidator()
# movie_service = MovieService(movie_repository, movie_validator, rental_service,)


c_repo = generate_clients_init()
client_repository = ClientRepository(c_repo)
client_validator = ClientValidator()
# client_service = ClientService(client_repository, client_validator)


rental_repository = RentalRepository(generate_rentals_init(movie_repository.get_movies, client_repository.get_clients))
rental_validator = RentalValidator()
rental_service = RentalService(rental_repository, rental_validator, movie_repository, client_repository, undo_service)

movie_service = MovieService(movie_repository, movie_validator, rental_service, undo_service)
client_service = ClientService(client_repository, client_validator, rental_service, undo_service)

# ui = UI(movie_service, client_service, rental_service, undo_service)
# ui.start()

print("1. UI")
print("2. GUI")
command = input("Choose the interface you want: ")


if command == '1':
    ui = UI(movie_service, client_service, rental_service, undo_service)
    ui.start()
elif command == '2':
    master = Tk()
    master.geometry("500x200")
    gui = GUI(master, movie_service, client_service, rental_service, undo_service)
    gui.start_gui()
    master.mainloop()
else:
    print("Bad command!")
