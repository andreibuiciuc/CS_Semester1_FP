class MovieException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class ClientException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class RentalException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class DuplicateIdException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class GenreException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class MovieValidatorException(MovieException):
    def __init__(self, error_list='Validation error!'):
        self._error_list = error_list

    @property
    def errors(self):
        return self._error_list

    def __str__(self):
        result = ''
        for error in self.errors:
            result = result + error + '\n'
        return result


class ClientValidatorException(ClientException):
    def __init__(self, error_list='Validation error!'):
        self._error_list = error_list

    @property
    def errors(self):
        return self._error_list

    def __str__(self):
        result = ''
        for error in self.errors:
            result = result + error + '\n'
        return result


class RentalValidatorException(RentalException):
    def __init__(self, errors):
        self._errors = errors

    @property
    def errors(self):
        return self._errors

    def __str__(self):
        result = ''
        for error in self.errors:
            result = result + error + '\n'
        return result
