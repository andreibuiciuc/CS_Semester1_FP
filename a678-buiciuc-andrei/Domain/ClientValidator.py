from Domain.Exceptions import ClientValidatorException


class ClientValidator:
    @staticmethod
    def validate(client):
        errors = []
        if client.client_id.isnumeric() is False:
            errors.append('Invalid client id, id should be 6 digits long.')
        if len(client.client_id) == 0:
            errors.append('Invalid client id, empty value provided.')
        if len(client.client_id) > 0 and len(client.client_id) != 6:
            errors.append('Invalid client id, id should be 6 digits long.')
        if len(client.name) == 0:
            errors.append('Invalid name, empty value provided')
        if len(errors) > 0:
            raise ClientValidatorException(errors)