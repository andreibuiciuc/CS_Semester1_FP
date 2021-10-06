from src.domain.entity import get_imag, get_modulo

from src.functions.functions import to_str, test_init, add_to_history, split_command, add_number_command_ui, \
    insert_number_command_ui, remove_number_command_ui, replace_number_command_ui, show_numbers_command_ui, \
    filter_command_ui, sum_sublist_command_ui, product_sublist_command_ui, undo_command_ui


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
    :param number_list: The list of complex numbers
    :param pos1: The starting position
    :param pos2: The final position
    :raises ValueError for invalid positions
    '''
    if pos1 > pos2 or (pos1 < 0 or pos2 < 0):
        raise ValueError("Wrong positions input!!")
    index = -1
    for number in number_list:
        index = index + 1
        if get_imag(number) == 0 and pos1 <= index <= pos2:
            print(to_str(number))


def show_list_relation_ui(number_list, relation, value):
    '''
    Function to diplay the numbers having their modulus in a relation with a given value
    :param number_list: The list of complex numbers
    :param relation: <, =, >
    :param value: A given value
    :raises ValueError for invalid relations
    '''
    if relation not in ['>', '<', '=']:
        raise ValueError("Wrong relation input!!")
    if relation in ['=', '<'] and value < 0:
        raise ValueError("Invalid relation!!")
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


#######################
# Command-driven menu #
#######################

def start_command_ui():
    number_list = []
    history_list = []

    test_init(number_list)
    auxiliary_list = number_list.copy()
    add_to_history(auxiliary_list, history_list)

    command_dict = {'add': add_number_command_ui, 'insert': insert_number_command_ui,
                    'remove': remove_number_command_ui,
                    'replace': replace_number_command_ui, 'list': show_numbers_command_ui, 'filter': filter_command_ui,
                    'sum': sum_sublist_command_ui, 'product': product_sublist_command_ui, 'undo': undo_command_ui}

    done = False
    while not done:
        command = input("\nYour command: ")
        command_word, command_params = split_command(command)
        if command_word in command_dict:
            try:
                if command_word in ['add', 'insert', 'remove', 'replace', 'undo', 'filter']:
                    command_dict[command_word](number_list, command_params, history_list)
                else:
                    command_dict[command_word](number_list, command_params)
            except ValueError as val_error:
                print(str(val_error))
        elif command_word == 'exit':
            done = True
        else:
            print("You introduced a bad command!!")


def welcome():
    print("\nHello and welcome to Numerical List! Let z = a + bi be your choice of complex numbers representation.")
    print("Look at the following functionalities: ")
    print("\tA. Add a number: use add <number> or insert <number> at <position>")
    print("\tB. Modify number: use remove <number> or remove <start pos> to <final pos> "
          "or replace <old number> with <new number>")
    print("\tC. Display numbers having different properties: list or list real <start pos> to"
          " <final pos> or list modulo [<, =, >] <number>")
    print("\tD. Obtain different characteristics of sublists: sum <start pos> to <final pos> "
          "or product <start pos> to <final pos>")
    print("\tE. Filter the list: filter real or filter modulo")
    print("\tF. Undo: undo")

