'''
 Problem Statement: 1. Numerical List
    - command-driven user interface
    - complex numbers in z = a + bi form, with a, b integers
    - functionalities:
        A. Add a number; add <number>, insert <number> at <position> //done
        B. Modify numbers
        C. Display numbers with given properties 
''' 
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

def is_int(var):
    try:
        int(var)
        return True
    except ValueError:
        return False

#####            

def to_int(real_part_str, imag_part_str):    
    '''
    Function to convert into integers the real and imaginary part extracted as strings

    :param real_part_str: The string of the real part
    :param iamg_part_str: The string of the imaginary part
    :return: The real and the imaginary part represented as integers 
    '''
    tokens = imag_part_str.split('i')

    if is_int(real_part_str) == False or is_int(tokens[0]) == False:
        raise ValueError("Not integers!!")

    real_part = int(real_part_str)
    imag_part = int(tokens[0].strip())
    return real_part, imag_part
    


def extract_str(parameters):
    '''
    Function to extract the real and imaginary part from a complex number
    Raises ValueError if the complex numbers is not written in a+bi form

    :param parameters: A complex number represented as a string
    :return: The real and imaginary part as strings
    '''
    
    if parameters.find('+') == -1 or parameters.find('i') == -1:
        raise ValueError("Wrong complex number input!!!")
    else:
        tokens = parameters.split('+')
        real_part_str = tokens[0].strip()
        imag_part_str = tokens[1].strip()    
        return real_part_str, imag_part_str


def to_str(number):
    '''
    Function to convert to string a complex number represented as a list
    :param number: A complex number as a list
    :return: A string representing a complex number
    '''
    return str(get_real(number)) + ' + ' + str(get_imag(number)) + 'i'


def add_number(number_list, number):
    '''
    Function to add a number to the list
    :param number_list: The list of complex numbers
    :number: Number to be added in the list
    '''
    number_list.append(number)


def insert_number(number_list, number, position):
    '''
    Function to insert a number at a given position
    Raises ValueError if the position does not exist in the list

    :param number_list: The list of complex numbers
    :param number: A complex number
    :param position: The position where to insert
    '''

    if position >= len(number_list) or position < 0:
        raise ValueError('Index input out of list!!')
    number_list.insert(position, number)


def remove_number(number_list, position):
    '''
    Function to remove a number from a given position
    Raises ValueError if the position does not exist in the list

    :param number_list: The list of complex numbers
    :param position: The position from where to remove
    '''

    if position >= len(number_list) or position < 0:
        raise ValueError('Index input out of list!!')
    number_list.pop(position)
    

def remove_number_positions(number_list, pos1, pos2):
    '''
    Function to remove numbers between two positions
    Raises ValueError if the positions are now well read

    :param number_list: The list of complex numbers
    :param pos1: The starting position
    :param pos2: The final position
    '''
    if pos1 > pos2 or (pos1 < 0 or pos2 < 0) or (pos1 >= len(number_list) or pos2 >= len(number_list)):
        raise ValueError("Wrong positions input!!")
    n_pop = pos2 - pos1 + 1
    while n_pop:
        number_list.pop(pos1)
        n_pop -=1        


def replace_number(number_list, old_number, new_number):
    '''
    Function to replace all appereances of a number in a list with a new value

    :param number_list: The list of complex numbers
    :param old_number: The number to be replaced
    :param new_number: The number that  replaces the old number
    '''
    index = -1
    for number in number_list:
        index = index + 1
        if number == old_number:
            remove_number(number_list, index)
            insert_number(number_list, new_number, index)
            
    

def show_list_ui(number_list):
    '''
    Function to display the list of complex numbers
    
    :param number_list: The list of complex numbers
    '''
    for number in number_list:
        print(to_str(number))


def show_list_real_ui(number_list, pos1, pos2):
    '''
    Function to display the real numbers between to given positions.
    Raises ValueError for invalid positions input

    :param number_list: The list of complex numbers
    :param pos1: The starting position
    :param pos2: The final position
    '''

    if pos1 > pos2:
        raise ValueError("Wrong positions input!!")
    index = -1
    for number in number_list:
        index = index + 1
        if get_imag(number) == 0 and index >= pos1 and index <= pos2:
            print(to_str(number)) 


def show_list_relation_ui(number_list, relation, value):
    '''
    Function to diplay the numbers having their modulus in a relation with a given value
    Raises ValueError for invalid relation input

    :param number_list: The list of complex numbers
    :param relation: The relation for equal, greater than or less than
    :param value: A given value
    '''
    if relation not in ['>','<','=']:
        raise ValueError("Wrong relation input!!")

    if relation in ['=', '<'] and value < 0:
        print("Invalid operation!")
    else:
        ok = False        
        for number in number_list:
            if relation == '<':
                if get_modulo(number) < value:
                    print(to_str(number))
                    ok = True
            if relation == '=':
                if get_modulo(number) == value:
                    print(to_str(number))
                    ok = True
            if relation == '>':
                if get_modulo(number) > value:
                    print(to_str(number))
                    ok = True
    if ok is False:
        print("No elements for this function!")

####

def add_number_command_ui(number_list, parameters):
    '''
    Function to manimpulate ADD command functionality

    :param number_list: The list of complex numbers
    :parameters: Specific parameters for the <add> functionality
    '''

    if parameters.find(' ') != -1:
        raise ValueError('Wrong complex number input!!')

    real_part_str, imag_part_str = extract_str(parameters)
    real_part, imag_part = to_int(real_part_str, imag_part_str)
    number = create_number(real_part, imag_part)
    add_number(number_list, number)


def insert_number_command_ui(number_list, parameters):
    '''
    Function to manipulate INSERT command functionality
    Raises ValueError if there are no sufficient parameters for this functionality

    :param number_list: The list of complex numbers
    :parameters: Specific parameters for the <insert> functionality
    '''

    tokens = parameters.split()
    if len(tokens) < 3:
        raise ValueError('Not enough parameters for this functionality!!')

    real_part_str, imag_part_str = extract_str(tokens[0])
    real_part, imag_part = to_int(real_part_str, imag_part_str)
    number = create_number(real_part, imag_part)
    position = int(tokens[2])
    insert_number(number_list, number, position)


def remove_number_command_ui(number_list, parameters):
    '''
    Function to manipulate REMOVE command functionality
    Raises ValueError if there are no sufficient parameters for this functionality

    :param number_list: The list of complex numbers
    :parameters: Specific parameters for the <remove> functionality
    '''
    tokens = parameters.split()
    if len(tokens) == 0:
        raise ValueError("Not enough parameters for this functionality!!")

    if len(tokens) == 1:
        position = int(tokens[0])
        remove_number(number_list, position)        
    else:
        pos1 = int(tokens[0])
        pos2 = int(tokens[2])
        remove_number_positions(number_list, pos1, pos2)


def replace_number_command_ui(number_list, parameters):
    '''
    Function to manipulate REPLACE command functionality
    Raises ValueError if there are no sufficient parameters for this functionality
    
    :param number_list: The list of complex numbers
    :param parameters: Specific parameters for the <replace> functionality
    '''
    tokens = parameters.split()
    if len(tokens) < 3:
        raise ValueError("Not enough parameters for this functionality!!")


    # Create the number to be replaced
    real_part_str, imag_part_str = extract_str(tokens[0])
    real_part, imag_part = to_int(real_part_str, imag_part_str)
    old_number = create_number(real_part, imag_part)
    # Create the new number
    real_part_str, imag_part_str = extract_str(tokens[2])
    real_part, imag_part = to_int(real_part_str, imag_part_str)
    new_number = create_number(real_part, imag_part)
    # Call the function
    replace_number(number_list, old_number, new_number)


def show_numbers_command_ui(number_list, parameters):
    '''
    Function to manipulate SHOW command functionality

    :param number_list: The list of complex numbers
    :param parameters: Specific parameters for the <show> functionality
    '''

    if parameters == '':
        show_list_ui(number_list)
    else:
        tokens = parameters.strip().split()
        
        if tokens[0].lower() not in ['real', 'modulo']:
            raise ValueError('Wrong property input!!')
       
        if tokens[0].lower() == 'real':
            if len(tokens) < 4:
                raise ValueError("Not enough parameters for this function!!")
            pos1 = int(tokens[1])
            pos2 = int(tokens[3])
            show_list_real_ui(number_list, pos1, pos2)
       
        if tokens[0].lower() == 'modulo':
            if len(tokens) < 3:
                raise ValueError("Not enough parameters for this function!!")
            relation = tokens[1]
            value = int(tokens[2])
            show_list_relation_ui(number_list, relation, value)
######

def split_command(command):
    '''
    Divide user command into command word and command params (parameters)
    
    :param command: User's command
    :return: command word, command parameters
    '''
    # strip is used to eliminate leading and trailing characters
    tokens = command.strip().split(' ', 1)
    tokens[0] = tokens[0].lower()
    return tokens[0], '' if len(tokens) == 1 else tokens[1].strip()


def start_command_ui():
    number_list = []
    test_init(number_list)

    command_dict = {'add': add_number_command_ui, 'insert': insert_number_command_ui, 'remove':remove_number_command_ui,
                    'replace': replace_number_command_ui, 'list': show_numbers_command_ui}

    done = False
    while not done:
        command = input("\nYour command: ")
        command_word, command_params = split_command(command)
        if command_word in command_dict:
            try:
                command_dict[command_word](number_list, command_params)
            except ValueError as val_error:
                print(str(val_error))
        elif command_word == 'exit':
            done = True
        else:
            print("You introduced a bad command!!")


def welcome():
    print("\nHello and welcome to Numerical List! Let z = a + bi be your choice of complex numbers represantation.")
    print("Look at the following functionalities: ")
    print("\tA. Add a number: use add <number> or insert <number> at <position>")
    print("\tB. Modify number: use remove <number> or remove <start pos> to <final pos> or replace <old number> with <new number>")
    print("\tC. Display numbers having different properties: list or list real <start pos> to <final pos> or list modulo [<, =, >] <number>")


# Test functions
def test_init(number_list):
    number_list.append(create_number(1, 2))
    number_list.append(create_number(-1, 2))
    number_list.append(create_number(1, 0))
    number_list.append(create_number(4, 0))
    number_list.append(create_number(-2, -2))
    number_list.append(create_number(3, -1))
    number_list.append(create_number(1, 0))
    number_list.append(create_number(0, 0))
    number_list.append(create_number(1, 1))
    number_list.append(create_number(1, -1))


def test_split_command():
    for cmd in ['insert 2+2i at 1', 'inSERT   2+2i at 1', '   insert 2+2i at 1  ']:
        cmd_word, cmd_params = split_command(cmd)
        assert cmd_word == 'insert' and cmd_params =='2+2i at 1'
        
    cmd_word, cmd_params = split_command('exit')
    assert cmd_word == 'exit' and cmd_params == ''


def test_add_number():
    number_list = []
    test_init(number_list) 
    list_len = len(number_list)

    add_number(number_list, '2+3i')
    assert len(number_list) == list_len + 1

    add_number(number_list, '2+-3i')
    assert len(number_list) == list_len + 2

    add_number(number_list, '-2+-3i')
    assert len(number_list) == list_len + 3


def test_insert_number_position():
    number_list = []
    test_init(number_list)
    list_len = len(number_list)

    # Try to insert a number at a valid index-position
    position = 2
    insert_number(number_list, '2+3i', position)
    assert len(number_list) == list_len + 1

    # Try to add a number at a non-valid index-position
    try:
        position = 15
        insert_number(number_list, '2+4i', position)
        assert len(number_list) == list_len + 1
    except ValueError:
        assert True


def test_remove_number():
    number_list = []
    test_init(number_list)
    list_len = len(number_list)

    # Try to remove a number from a valid index-position
    remove_number(number_list, 2)
    assert len(number_list) == list_len - 1

    # Try to remove a number from an invalid index-position
    try:
        remove_number(number_list, 15)
        #assert len(number_list) == list_len - 1
    except ValueError:
        assert True

    try:
        remove_number(number_list, -3)
        #assert len(number_list) == list_len - 1
    except ValueError:
        assert True


def test_remove_number_positions():
    number_list = []
    test_init(number_list)
    list_len = len(number_list)

    # Try to remove numbers from valid positions
    remove_number_positions(number_list, 2, 3)
    assert len(number_list) == list_len - 2

    #Try to remove numbers from invalid position
    try:
        remove_number_positions(number_list, 4, 2)
        #assert len(number_list) == list_len - 2
    except ValueError:
        assert True
    

def test_replace_number():
    number_list = []
    test_init(number_list)
    list_len = len(number_list)

    replace_number(number_list, '1+0i', '5+5i')
    assert len(number_list) == list_len


def test_extract_str():
    # Try when number has valid input
    number = '2+3i'
    real_str, imag_str = extract_str(number)
    assert real_str == '2' and imag_str == '3i'

    # Try when number has invalid input
    number = '2-3i'
    try:
        real_str, imag_str = extract_str(number)
        assert real_str == '2' and imag_str == '3i'
    except ValueError:
        assert True


def test_to_int():
    # Try a valid number input
    real, imag = to_int('2', '3i')
    assert real == 2 and imag == 3

    # Try an invalid number input
    try:
        real, imag = to_int('0.2', '7.0i')
    except ValueError:
        assert True    

test_split_command()
test_add_number()
test_insert_number_position()
test_remove_number()
test_remove_number_positions()
test_replace_number()
test_extract_str()
test_to_int()

welcome()
start_command_ui()
