def coin_change(amount, coins, change, stiva):
    if amount == 0:
        change = sorted(change)
        if change not in stiva:
            print(change)
            stiva.append(change)
            return

    if amount < 0:
        return

    for index in range(0, len(coins)):
        coin = coins[index]
        if amount >= coin:
            change.append(coin)
            coin_change(amount-coin, coins, change, stiva)
            change.pop(-1)


def solution(amount):
    if amount == 0:
        return True
    return False


def consistent(amount, coin):
    if amount >= coin:
        return True
    return False


def display(change, stiva):
    change = sorted(change)
    if change not in stiva:
        print(change)
        stiva.append(change)


def backtracking(amount, coins, change, stiva):
    for i in range(0, len(coins)):
        coin = coins[i]
        if consistent(amount, coin):
            change.append(coin)
            backtracking(amount-coin, coins, change, stiva)
            if solution(amount-coin):
                display(change, stiva)
            change.pop(-1)


s = 5
values = [1, 2, 3, 5, 10, 50]
print('---------------------------------')
print("Backtracking - recursive")
coin_change(s, values, [], [])
print('---------------------------------')
print("Backtracking - recursive template")
backtracking(s, values, [], [])
print('---------------------------------')

