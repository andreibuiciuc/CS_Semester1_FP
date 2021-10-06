from Domain.Exceptions import DuplicateIdException


class ClientRepository:
    def __init__(self, client_list):
        self._client_list = client_list

    def __len__(self):
        return len(self._client_list)

    @property
    def get_clients(self):
        return self._client_list

    def get_client(self, client_id):
        index = 0
        for client in self._client_list:
            if client.client_id == client_id:
                return self._client_list[index]
            index = index + 1

    def add_client(self, client):
        """
        Method to add a client to the list of clients.
        :param client: A given client.
        :return: -
        """
        for c in self._client_list:
            if c.client_id == client.client_id:
                raise DuplicateIdException("Duplicate id!!")
        self._client_list.append(client)

    def remove_client(self, client_id):
        """
        Method to remove a client from the list of clients.
        :param client_id: A given client id.
        :return: -
        """
        index = 0
        for c in self._client_list:
            if c.client_id == client_id:
                self._client_list.pop(index)
                break
            index = index + 1

    def update_client(self, client_id, name):
        """
        Method to update a client from the list of clients.
        :param client_id: A given client id.
        :param name: New name or '' for keeping the old name.
        :return: -
        """
        for c in self._client_list:
            if c.client_id == client_id:
                if name != '':
                    c.name = name
