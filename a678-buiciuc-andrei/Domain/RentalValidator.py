from Domain.Exceptions import RentalValidatorException


class RentalValidator:
    @staticmethod
    def validate(rental):
        errors = []
        if rental.rental_id.isnumeric() is False:
            errors.append('Invalid rental id, id should be 6 digits long')
        if len(rental.rental_id) == 0 or len(rental.rental_id) != 6 or rental.rental_id.isnumeric is False:
            errors.append('Invalid rental id')
        if len(rental.movie_id) == 0 or len(rental.rental_id) != 6 or rental.rental_id.isnumeric is False:
            errors.append('Invalid movie id')
        if len(rental.client_id) == 0 or len(rental.rental_id) != 6 or rental.rental_id.isnumeric is False:
            errors.append('Invalid client id')
        if not (rental.rented_date <= rental.due_date):
            errors.append('Invalid date input!')
        if len(errors) != 0:
            raise RentalValidatorException(errors)
