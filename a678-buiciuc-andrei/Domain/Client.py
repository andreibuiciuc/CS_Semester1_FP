class Client:
    def __init__(self, client_id, name):
        self._client_id = client_id
        self._name = name

    @property
    def client_id(self):
        return self._client_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return self._client_id + ' | ' + self._name