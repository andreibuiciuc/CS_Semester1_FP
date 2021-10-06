def consistent(amount, coin):
    if amount >= coin:
        return True
    return False


def solution(amount):
    if amount == 0:
        return True
    return False


def display(change, stiva):
    change = sorted(change)
    if change not in stiva:
        print(change)
        stiva.append(change)


def backtracking_iterative(amount, coins, change, stiva):
    pass

s = 5
values = [1, 2, 3, 5, 10, 50]
backtracking_iterative(s, values, [], [])