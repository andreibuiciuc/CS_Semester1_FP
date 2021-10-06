"""
A number of n coins are given, with values of a1, ..., an and a value s.
Display all payment modalities for the sum s.
If no payment modality exists print a message.

    Notations:
        amount -> the sum s
        coins  -> the list of coins having some values
        change -> a payment modality ~ represents a candidate for a solution
                  change keeps the indices from the list of coins
        okay   -> we check whether the sum can be written as a payment with the given coins

"""


def init():
    """
    We initialize the list representing a candidate
    """
    return [-1]


def successor(change, length):
    """
    We increase the last index by 1 (to get the next coin from the list of coins)
    We also check if we don't exceed the list of coins
    """
    change[-1] += 1
    return change[-1] < length


def sum_is(change, coins):
    """
    We calculate the sum of the coins given by the list of indices
    We ho through all the indices and we add the corresponding values
    """
    result = 0
    for index in range(0, len(change)):
        result += coins[change[index]]
    return result


def consistent(amount, coins, change):
    """
    We check the consistency:
        - the current sum must not exceed the given amount
        - we add the second condition to avoid having coins that repeat themselves
    """
    return sum_is(change, coins) <= amount and len(set(change)) == len(change)


def solution(amount, coins, change):
    """
    We check whether a candidate is a solution or not
    """
    return sum_is(change, coins) == amount


def display(coins, change, okay):
    if okay == 0:
        print('Payment modalities: ')
    for index in range(0, len(change)):
        print(coins[change[index]], end=' ')
    print(' ')


def coin_change_recursive(amount, coins, change, okay):
    """
    The Recursive Backtracking Algorithm
    """
    while successor(change, len(coins)):
        if consistent(amount, coins, change):
            if solution(amount, coins, change):
                display(coins, change, okay)
                okay = True
            else:
                # we go a step back
                change.append(change[-1] - 1)
                okay = coin_change_recursive(amount, coins, change, okay)
    change.pop()
    return okay


def coin_change_iterative(amount, coins):
    """
    The Iterative Backtracking Algorithm
    """
    change = init()
    okay = False
    while len(change) > 0:
        if not successor(change, len(coins)):
            change.pop()
        elif consistent(amount, coins, change):
            if solution(amount, coins, change):
                display(coins, change, okay)
                okay = True
            else:
                # we go a step back
                change.append(change[-1] - 1)
    if okay is False:
        print("Nope")


def start_recursive(amount, coins):
    """
    We initialize the possible candidate
    We treat the case for no payment modalities
    """
    change = init()
    okay = coin_change_recursive(amount, coins, change, False)
    if okay is False:
        print('Nope')


#print("\nRecursive: ")
#start_recursive(10, [5, 4, 2, 1, 3])

#print("\nIterative: ")
#start_recursive(10, [5, 4, 2, 1, 3])

print("\nRecursive: ")
start_recursive(8, [1, 3, 4, 2, 1, 1])

print("\nIterative: ")
coin_change_iterative(8, [1, 3, 4, 2, 1, 1])


