#
# Implement the program to solve the problem statement from the first set here
#   Generate the first prime number larger than n
#     1. by iterating n until we find the prime number
#     2. by using Eratosthenes observation to generate prime numbers
#

def prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        i = 3
        while i * i <= x and x % i != 0:
            i = i + 2
        if i * i > x:
            return True
        else:
            return False

def solve(n):
    solution = False
    while not solution:
        n = n + 1
        if prime(n) == True:
            print(n)
            solution = True

def generate_prime(n):

    limit = 999999   #set limit for generating prime numbers
    isPrime = [True] * limit    #list of true values
    
    index = 2
    while index * index <= limit:
        if isPrime[index] == True:
            for i in range(index*index, limit, index):  #we mark the multiples so that they can't be prime numbers
                isPrime[i] = False
        index = index + 1

    for j in range(n + 1, limit):   #the first prime is returned
        if isPrime[j] == True:
            return j

if __name__ == "__main__":
    #1
    n = int(input("Give a natural number: "))
    solve(n)
   
    '''
    m = int(input("Give a natural number: "))
    generate_prime(m)
    print(generate_prime(m))
    '''