from Domain.Client import Client
from Domain.Exceptions import DuplicateIdException
from Service.UndoService import FunctionCall, Operation


class ClientService:
    def __init__(self, client_repository, client_validator, rental_service, undo_service):
        self._client_repository = client_repository
        self._client_validator = client_validator
        self._rental_service = rental_service
        self._undo_service = undo_service

    @property
    def get_repo(self):
        return self._client_repository

    def check_for_id(self, client_id):
        """
        Method to check for duplicate id in the list of clients.
        :param client_id: A given client id.
        :return:
        """
        for client in self._client_repository.get_clients:
            if client.client_id == client_id:
                return False
        return True

    def create_client(self, client_id, name):
        if self.check_for_id(client_id) is False:
            raise DuplicateIdException('Duplicate id!!')
        else:
            client = Client(client_id, name)
            self._client_validator.validate(client)
            return client

    def add_client(self, client):
        self._client_repository.add_client(client)

    def add_client_record(self, client):
        self.add_client(client)

        fun_undo = FunctionCall(self.remove_client, client.client_id)
        fun_redo = FunctionCall(self.add_client, client)
        self._undo_service.record(Operation(fun_undo, fun_redo))

    def add_client_with_rentals(self, client, rentals):
        self.add_client(client)
        for rental in rentals:
            self._rental_service.add_rental(rental)

    def remove_client(self, client_id):
        self._client_repository.remove_client(client_id)

    def remove_client_with_rentals(self, client_id):
        self.remove_client(client_id)
        self._rental_service.remove_rental_by_client(client_id)

    def remove_client_record(self, client_id):
        # Remove a client from the list of clients.
        client = self._client_repository.get_client(client_id)
        self.remove_client(client_id)

        rentals = self._rental_service.filter_rentals_by_client(client_id)

        if len(rentals) == 0:
            fun_undo = FunctionCall(self.add_client, client)
            fun_redo = FunctionCall(self.remove_client, client_id)
            self._undo_service.record(Operation(fun_undo, fun_redo))

        else:
            self._rental_service.remove_rental_by_client(client_id)
            fun_undo = FunctionCall(self.add_client_with_rentals, client, rentals)
            fun_redo = FunctionCall(self.remove_client_with_rentals, client_id)
            self._undo_service.record(Operation(fun_undo, fun_redo))

    def update_client(self, client_id, name):
        old_name = self._client_repository.get_client(client_id).name

        self._client_repository.update_client(client_id, name)
        fun_undo = FunctionCall(self.reverse_update, client_id, old_name)
        fun_redo = FunctionCall(self.update_client, client_id, name)
        self._undo_service.record(Operation(fun_undo, fun_redo))

    def reverse_update(self, client_id, old_name):
        self._client_repository.update_client(client_id, old_name)

