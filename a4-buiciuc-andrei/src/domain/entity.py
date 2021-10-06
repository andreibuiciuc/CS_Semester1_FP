import math

def get_real(number):
    return number[0]

def get_imag(number):
    return number[1]

def create_number(real_part, imag_part):
    return [real_part, imag_part]

def get_modulo(number):
    modulo = get_real(number) * get_real(number) + get_imag(number) * get_imag(number)
    return math.sqrt(modulo)
