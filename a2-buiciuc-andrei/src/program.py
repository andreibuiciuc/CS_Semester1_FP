#
# Write the implementation for A2 in this file
# 

#Non-UI functions are here 

def get_real(number):
    return number[0]

def get_imag(number):
    return number[1]

def create_number(re_part, im_part):
    """
    :param re_part: Real part of the number
    :param im_part: Imaginary part of the number
    :return: List representing a complex number
    """
    return [re_part, im_part]

def to_str(number):
    if get_real(number) == 0 and get_imag(number) == 0:       # case for z = 0                        
        return '0'
    elif get_real(number) == 1 and get_imag(number) == 0:     # case for z = 1
        return '1'
    elif get_real(number) == 0 and get_imag(number) == 1:     # case for z = i
        return 'i'
    elif get_real(number) == 0 and get_imag(number) == -1:   # case for z = -i
        return '-i'
    elif get_real(number) != 0 and get_imag(number) == 0:     # case for z = +/- a 
        return str(get_real(number))  
    elif get_real(number) == 0 and get_imag(number) != 0:      # case for z = +/- bi
        return str(get_imag(number)) + 'i'
    elif get_real(number) != 0 and get_imag(number) == 1:     # case for z = a + i
        return str(get_real(number)) + ' + ' + 'i'
    elif get_real(number) != 0  and get_imag(number) == -1:   # case for z = a - i 
        return str(get_real(number)) + ' - ' + 'i'
    elif get_real(number) != 0 and get_imag(number) > 0:      # case for z = a + bi
        return str(get_real(number)) + ' + ' + str(get_imag(number)) + 'i'
    elif get_real(number) != 0 and get_imag(number) < 0:      # case for z = a - bi  
        return str(get_real(number)) + ' - ' + str(0 - get_imag(number)) + 'i'

def a_functionality(numbers_list):
    """
    Function to find the longest sequence of real numbers.
    :param numbers_list: The list of complex numbers.
    :return:
    """
    l_crt = 0
    l_max = 0
    i = -1
    pos = -1
    for number in numbers_list:
        i = i + 1
        if get_imag(number) == 0:
            l_crt += 1
        else:
            if l_crt > l_max:
                l_max = l_crt
                pos = i - 1
            l_crt = 0
    if l_crt > l_max:
        l_max = l_crt
        pos = i
    
    show_sequence_ui(numbers_list, pos - l_max + 1, pos)

def get_digits(number):
    """
    Function to create a frequency array of digits from both real and imaginary parts.
    :param number: a complex number
    :return: the frequency array of digits
    """
    digits = [0] * 10
    if get_real(number) < 0:
        a = 0 - get_real(number)
    else:
        a = get_real(number)
    while a:
        digits[a % 10] += 1
        a = a // 10
    if get_imag(number) < 0:
        b = 0 - get_imag(number)
    else:
        b = get_imag(number)
    while b:
        digits[b % 10] += 1
        b = b // 10

    for index in range(0, 10):
        if digits[index] != 0:
            digits[index] = 1
    return digits

def create_digits_list(numbers_list):
    """
    Function to create a list of frequency arrays for each complex number
    :param numbers_list: the list of complex numbers
    :return: a list of frequency arrays
    """
    digit_list = []
    for number in numbers_list:
        digit_list.append(get_digits(number))
    return digit_list


def b_functionality(numbers_list):
    """
    Function to find the largest sequence of complex numbers with both real
    and imaginary parts written with the same digits
    :param numbers_list: the list of complex numbers
    :return:
    """
    digit_list = create_digits_list(numbers_list)
    
    list_ant = [-1] * 10
    l_crt = 1
    l_max = 0
    i = -1
    pos = -1
    for digit in digit_list:
        i = i + 1
        if digit == list_ant:
            l_crt += 1
        else:
            if l_crt > l_max:
                l_max = l_crt
                pos = i - 1
            l_crt = 1
            list_ant = digit
    if l_crt > l_max:
        l_max = l_crt
        pos = i

    show_sequence_ui(numbers_list, pos - l_max + 1, pos)



#UI functions are here

def show_sequence_ui(numbers_list, pos0, posf):
    """
    Function to print a sequence
    :param numbers_list: the list of complex numbers
    :param pos0: the position of the first element from the sequence
    :param posf: the position of the last element from the sequence
    """
    #print(numbers_list[pos0:posf + 1])
    if posf == -1:
        print("No elements for this functionality:(")
    else:
        for index in range(pos0, posf + 1):
            print(to_str(numbers_list[index]))
    


def read_list_ui(numbers_list):
    """
    Reads consecutively complex numbers that are added to the list.
    :param numbers_list: the list of complex numbers
    """

    print("Introduce the real and the imaginary part of your z = a + b*i complex number.")

    done = False
    while not done:
        re_part = int(input("Real part: "))
        im_part = int(input("Imaginary part: "))
        number = create_number(re_part, im_part)
        numbers_list.append(number)
        
        command = input("Press x to exit, otherwise continue: ")
        if command == 'x':
            done = True 

def show_list_ui(numbers_list):
    """
    Displays the content of our list of complex numbers
    :param numbers_list: the list of complex numbers
    """
    if not numbers_list:
        print("Empty list!!")
    else:
        for number in numbers_list:
            print(to_str(number))

def print_submenu():
    print("\ta. Longest sequence of real numbers.")
    print("\tb. Longest sequence of numbers written with the same digits.\n")

def print_menu():
    print("\n1. Read a list of complex numbers.")
    print("2. Show the list of complex numbers.")
    print("3. Choose a functionality.")
    print("0. Exit.\n")

def start():
    """
    Prints the main menu and deals with the user's input
    1. Reads the list of complex numbers, z = a + b * i.
    2. Display the list of complex numbers.
    3. Display a functionality.
    4. Exit the application.
    """

    numbers_list = []
    test_init(numbers_list)
    command_dict = {'1': read_list_ui, '2': show_list_ui, '3': print_submenu}
    done = False

    while not done:
        print_menu()
        command = input("Choose a command: ")
        if command == '0':
            done = True
        elif command == '3':
            command_dict[command]()
            
            sub_command = input("Your functionality is: ")
            if sub_command == 'a':
                a_functionality(numbers_list)
            elif sub_command == 'b':
                b_functionality(numbers_list)

        elif command not in command_dict:
            print("Invalid command!")
        else:
            command_dict[command](numbers_list)


def welcome():
    print("\nHello and welcome! Choose a command below." )

def test_init(numbers_list):
    
    numbers_list.append(create_number(2, 1))
    numbers_list.append(create_number(1, 3))
    numbers_list.append(create_number(33, 1))
    numbers_list.append(create_number(13, 0))
    numbers_list.append(create_number(4, 0))
    numbers_list.append(create_number(-2, 0))
    numbers_list.append(create_number(-3, 2))
    numbers_list.append(create_number(-32, -2))
    numbers_list.append(create_number(2, 3))
    numbers_list.append(create_number(22, 33))
    #numbers_list.append(create_number(0, 0))
    
    
welcome()
start()