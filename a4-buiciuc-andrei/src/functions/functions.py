import src.ui.console
from src.domain.entity import get_imag, get_real, create_number, get_modulo

def add_number_command_ui(number_list, parameters, history_list):
    """
    Function to manipulate the ADD command functionality
    :param number_list: The list of complex numbers
    :param parameters: Specific parameters for the <add> functionality
    :param history_list: A list with all the processes on number_list
    :raises ValueError for invalid parameters
    """

    if parameters.find(' ') != -1:
        raise ValueError('Wrong complex number input!!')

    real_part_str, imag_part_str = extract_str(parameters)
    real_part, imag_part = to_int(real_part_str, imag_part_str)
    number = create_number(real_part, imag_part)
    add_number(number_list, number)

    auxiliary_list = number_list.copy()
    add_to_history(auxiliary_list, history_list)


def insert_number_command_ui(number_list, parameters, history_list):
    """
    Function to manipulate the INSERT command functionality
    :param number_list: The list of complex numbers
    :param parameters: Specific parameters for the <insert> functionality
    :param history_list: A list with all the processes on number_list
    :raises ValueError for invalid parameters
    """
    tokens = parameters.split()
    if len(tokens) != 3:
        raise ValueError('Wrong parameters!!')

    real_part_str, imag_part_str = extract_str(tokens[0])
    real_part, imag_part = to_int(real_part_str, imag_part_str)
    number = create_number(real_part, imag_part)
    position = int(tokens[2])
    insert_number(number_list, number, position)
    auxiliary_list = number_list.copy()
    add_to_history(auxiliary_list, history_list)


def remove_number_command_ui(number_list, parameters, history_list):
    """
    Function to manipulate the REMOVE command functionality
    :param number_list: The list of complex numbers
    :param parameters: Specific parameters for the <remove> functionality
    :param history_list: A list with all the processes on number_list
    :raises ValueError for invalid parameters
    """
    tokens = parameters.split()
    if len(tokens) not in [1, 3]:
        raise ValueError("Wrong parameters!!")

    if len(tokens) == 1:
        position = int(tokens[0])
        remove_number(number_list, position)
        auxiliary_list = number_list.copy()
        add_to_history(auxiliary_list, history_list)
    elif len(tokens) == 3:
        pos1 = int(tokens[0])
        pos2 = int(tokens[2])
        remove_number_positions(number_list, pos1, pos2)
        auxiliary_list = number_list.copy()
        add_to_history(auxiliary_list, history_list)


def replace_number_command_ui(number_list, parameters, history_list):
    """
    Function to manipulate the REPLACE command functionality
    :param number_list: The list of complex numbers
    :param parameters: Specific parameters for the <replace> functionality
    :param history_list: A list with all the processes on number_list
    :raises ValueError for invalid parameters
    """
    tokens = parameters.split()
    if len(tokens) != 3:
        raise ValueError("Wrong parameters!!")
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
    auxiliary_list = number_list.copy()
    add_to_history(auxiliary_list, history_list)


def show_numbers_command_ui(number_list, parameters):
    """
    Function to manipulate the SHOW command functionality
    :param number_list: The list of complex numbers
    :param parameters: Specific parameters for the <show> functionality
    :raises ValueError for invalid parameters or invalid property input
    """

    if parameters == '':
        src.ui.console.show_list_ui(number_list)
    else:
        tokens = parameters.strip().split()

        if tokens[0].lower() not in ['real', 'modulo']:
            raise ValueError('Wrong property input!!')

        if tokens[0].lower() == 'real':
            if len(tokens) != 4:
                raise ValueError("Wrong parameters!!")
            pos1 = int(tokens[1])
            pos2 = int(tokens[3])
            src.ui.console.show_list_real_ui(number_list, pos1, pos2)

        if tokens[0].lower() == 'modulo':
            if len(tokens) != 3:
                raise ValueError("Wrong parameters!!")
            relation = tokens[1]
            value = int(tokens[2])
            src.ui.console.show_list_relation_ui(number_list, relation, value)


def sum_sublist_command_ui(number_list, parameters):
    """
    Function to manipulate the SUM command functionality
    :param number_list: The list of complex numbers
    :param parameters: Specific parameters for the <sum> functionality
    :raises ValueError for invalid parameters
    """
    tokens = parameters.strip().split()

    if len(tokens) != 3:
        raise ValueError("Wrong parameters!!")

    position1 = int(tokens[0])
    position2 = int(tokens[2])
    print(sum_numbers(number_list, position1, position2))


def product_sublist_command_ui(number_list, parameters):
    """
    Function to manipulate the PRODUCT command functionality
    :param number_list: The list of complex numbers
    :param parameters: Specific parameters for the <product> functionality
    :raises ValueError for invalid parameters
    """
    tokens = parameters.strip().split()

    if len(tokens) != 3:
        raise ValueError("Wrong parameters!!")

    position1 = int(tokens[0])
    position2 = int(tokens[2])
    print(product_numbers(number_list, position1, position2))


def filter_command_ui(number_list, parameters, history_list):
    """
    Function to manipulate the FILTER command functionality
    :param number_list: The list of complex numbers
    :param parameters: Specific parameters for this functionality
    :param history_list: A list with all the processes on number_list
    """

    tokens = parameters.strip().split()
    if len(tokens) == 0:
        raise ValueError("Wrong property input!!")

    if tokens[0].lower() not in ['real', 'modulo']:
        raise ValueError("Wrong property input!!")

    if tokens[0].lower() == 'real':
        if len(tokens) != 1:
            raise ValueError("Wrong parameters!!")
        filter_real(number_list)

        auxiliary_list = number_list.copy()
        add_to_history(auxiliary_list, history_list)

    if tokens[0].lower() == 'modulo':
        if len(tokens) != 3:
            raise ValueError("Wrong parameters!!")
        relation = tokens[1]
        value = int(tokens[2])
        filter_modulo(number_list, relation, value)

        auxiliary_list = number_list.copy()
        add_to_history(auxiliary_list, history_list)


def undo_command_ui(number_list, parameters, history_list):
    """
    Function to manipulate the UNDO command functionality
    :param number_list: The list of complex numbers
    :param parameters: Specific parameters for this functionality
    :param history_list: A list with all the processes on number_list
    :raises ValueError for invalid property input
    """
    if parameters != '':
        raise ValueError("Wrong property input!!")

    auxiliary_list = number_list
    undo_list = undo_operation(auxiliary_list, history_list)

    # for number in undo_list:
    #     print(to_str(number))
    # print(number_list)


def split_command(command):
    """
    Function to divide user's command into command_word and command_params (parameters)
    :param command: User's command
    :return: command_word, command_params
    """
    # strip is used to eliminate leading and trailing characters
    tokens = command.strip().split(' ', 1)
    tokens[0] = tokens[0].lower()
    return tokens[0], '' if len(tokens) == 1 else tokens[1].strip()


def add_to_history(list, history_list):
    history_list.append(list)


def is_int(var):
    try:
        int(var)
        return True
    except ValueError:
        return False

def to_int(real_part_str, imag_part_str):
    """
    Function to convert into integers the real and imaginary part extracted as strings
    :param real_part_str: The string of the real part
    :param imag_part_str: The string of the imaginary part
    :raises ValueError if
    :return: The real and the imaginary part represented as integers
    """
    tokens = imag_part_str.split('i')

    if is_int(real_part_str) is False or is_int(tokens[0]) is False:
        raise ValueError("Not integers!!")

    real_part = int(real_part_str)
    imag_part = int(tokens[0].strip())
    return real_part, imag_part


def extract_str(parameters):
    """
    Function to extract the real and imaginary part from a complex number
    :param parameters: A complex number represented as a string
    :raises ValueError for invalid complex number input
    :return: The real and imaginary part as strings
    """

    if parameters.find('+') == -1 or parameters.find('i') == -1:
        raise ValueError("Wrong complex number input!!!")
    else:
        tokens = parameters.split('+')
        real_part_str = tokens[0].strip()
        imag_part_str = tokens[1].strip()
        return real_part_str, imag_part_str


def to_str(number):
    """
    Function to convert to a string a complex number represented as a list
    :param number: A complex number as a list
    :return: A string representing a complex number
    """
    return str(get_real(number)) + ' + ' + str(get_imag(number)) + 'i'


def add_number(number_list, number):
    """
    Function to add a number to the list
    :param number_list: The list of complex numbers
    :param number: Number to be added in the list
    """
    number_list.append(number)


def insert_number(number_list, number, position):
    """
    Function to insert a number at a given position
    :param number_list: The list of complex numbers
    :param number: A complex number
    :param position: The position where to insert
    :raises ValueError for invalid index position
    """

    if position >= len(number_list) or position < 0:
        raise ValueError('Index input out of list!!')
    number_list.insert(position, number)


def remove_number(number_list, position):
    """
    Function to remove a number from a given position
    :param number_list: The list of complex numbers
    :param position: The position from where to remove
    :raises ValueError for invalid index position
    """

    if position >= len(number_list) or position < 0:
        raise ValueError('Index input out of list!!')
    number_list.pop(position)


def remove_number_positions(number_list, pos1, pos2):
    """
    Function to remove numbers between two positions
    :param number_list: The list of complex numbers
    :param pos1: The starting position
    :param pos2: The final position
    :raises ValueError for invalid index positions
    """
    if pos1 > pos2 or (pos1 < 0 or pos2 < 0) or (pos1 >= len(number_list) or pos2 >= len(number_list)):
        raise ValueError("Wrong positions input!!")

    n_pop = pos2 - pos1 + 1
    while n_pop:
        number_list.pop(pos1)
        n_pop -= 1


def replace_number(number_list, old_number, new_number):
    """
    Function to replace all appearances of a number in a list with a new value
    :param number_list: The list of complex numbers
    :param old_number: The number to be replaced
    :param new_number: The number that  replaces the old number
    """
    index = -1
    for number in number_list:
        index = index + 1
        if number == old_number:
            remove_number(number_list, index)
            insert_number(number_list, new_number, index)


def sum_numbers(number_list, position1, position2):
    """
    Function to calculate the sum of complex numbers between two given positions.
    :param number_list: The list of complex numbers
    :param position1: The starting position
    :param position2: The final positions
    :return: The result as a string
    :raises ValueError for invalid positions.
    """
    if (position1 > position2) or (position1 < 0 or position2 < 0) or (position1 > len(number_list)
                                                                       or position2 > len(number_list)):
        raise ValueError("Invalid positions!!")
    sum_real = 0
    sum_imag = 0
    position = -1
    for number in number_list:
        position = position + 1
        if position1 <= position <= position2:
            sum_real += get_real(number)
            sum_imag += get_imag(number)

    result = create_number(sum_real, sum_imag)
    return to_str(result)


def product_numbers(number_list, position1, position2):
    """
    Function to calculate the product od complex numbers between the two given positions
    :param number_list: The list of complex numbers
    :param position1: The starting position
    :param position2: The final position
    :raises ValueError for invalid index positions
    :return: The result as a string
    """
    if (position1 > position2) or (position1 < 0 or position2 < 0) or (position1 > len(number_list)
                                                                       or position2 > len(number_list)):
        raise ValueError("Invalid positions!!")
    number_ant = 0
    result_real = 0
    result_imag = 0
    ok = False
    position = -1
    for number in number_list:
        position = position + 1
        if position1 <= position <= position2:
            if ok is False:
                number_ant = number
                ok = True
            else:
                result_real = get_real(number_ant) * get_real(number) - get_imag(number_ant) * get_imag(number)
                result_imag = get_real(number_ant) * get_imag(number) + get_imag(number_ant) * get_real(number)
                number_ant = create_number(result_real, result_imag)
    return to_str(number_ant)


def filter_real(number_list):
    """
    Function to filter the list of complex numbers keeping only real numbers
    :param number_list: The list of complex numbers
    """
    result = list(filter(lambda elem: get_imag(elem) == 0, number_list))
    number_list.clear()
    for number in result:
        number_list.append(number)


def filter_modulo(number_list, relation, value):
    """
    Function to filter the list of complex numbers keeping only numbers with modulo in a relation with a value
    :param number_list: The list of complex numbers
    :param relation: <, =, >
    :param value: A given value
    """
    if relation == '<':
        result = list(filter(lambda elem: get_modulo(elem) < value, number_list))
        number_list.clear()
        for number in result:
            number_list.append(number)
    if relation == '=':
        result = list(filter(lambda elem: get_modulo(elem) == value, number_list))
        number_list.clear()
        for number in result:
            number_list.append(number)
    if relation == '>':
        result = list(filter(lambda elem: get_modulo(elem) > value, number_list))
        number_list.clear()
        for number in result:
            number_list.append(number)


def undo_operation(number_list, history_list):
    """
    Function that undoes an operation
    :param number_list: The list of complex numbers
    :param history_list: A list with all the processes on number_list
    :raises ValueError if there are no undos left
    """
    if len(history_list) == 1:
        raise ValueError("No more undos left!!")
    # history_list.pop(-1)
    # return history_list[-1]
    history_list.pop(-1)
    number_list.clear()
    for number in history_list[-1]:
        number_list.append(number)


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
        assert cmd_word == 'insert' and cmd_params == '2+2i at 1'

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
        # assert len(number_list) == list_len - 1
    except ValueError:
        assert True

    try:
        remove_number(number_list, -3)
        # assert len(number_list) == list_len - 1
    except ValueError:
        assert True


def test_remove_number_positions():
    number_list = []
    test_init(number_list)
    list_len = len(number_list)

    # Try to remove numbers from valid positions
    remove_number_positions(number_list, 2, 3)
    assert len(number_list) == list_len - 2

    # Try to remove numbers from invalid position
    try:
        remove_number_positions(number_list, 4, 2)
        # assert len(number_list) == list_len - 2
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

def test_sum_numbers():
    number_list = [[1, 2], [3, 4], [5, 6], [-2, -2]]
    assert sum_numbers(number_list, 0, 3) == '7 + 10i'

    try:
        sum_numbers(number_list, 4, 2)
    except ValueError:
        assert True

def test_product_numbers():
    number_list = [[1, 2], [2, 2], [2, 4], [1, 3], [5, 6]]
    assert product_numbers(number_list, 1, 3) == '-40 + 0i'

    try:
        product_numbers(number_list, -1, 3)
    except ValueError:
        assert True

def test_filter_real():
    number_list = []
    test_init(number_list)
    expected_result = [[1, 0], [4, 0], [1, 0], [0, 0]]
    filter_real(number_list)
    assert number_list == expected_result

def test_filter_modulo():
    number_list = []
    test_init(number_list)
    expected_result = [[1, 0], [1, 0]]
    filter_modulo(number_list, '=', 1)
    assert number_list == expected_result

    number_list = []
    test_init(number_list)
    filter_modulo(number_list, '>', 100)
    assert len(number_list) == 0

def test_undo():
    number_list = [[1, 2], [2, 3], [4, 5]]
    history_list = [[[1, 0], [0, 0]], [[1, 1], [2, 2]]]
    add_to_history(number_list, history_list)
    undo_operation(number_list, history_list)
    assert number_list == [[1, 1], [2, 2]]

def test_functions():
    test_split_command()
    test_add_number()
    test_insert_number_position()
    test_remove_number()
    test_remove_number_positions()
    test_replace_number()
    test_extract_str()
    test_to_int()
    test_sum_numbers()
    test_product_numbers()
    test_filter_modulo()
    test_filter_real()
    test_undo()
