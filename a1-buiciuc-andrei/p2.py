#
# Implement the program to solve the problem statement from the second set here
#  The product of all proper factors
#

def product(n):
    p = 1
    index = 2
    ok = False
    while index * index <= n:
        if n % index == 0:
            ok = True
            if(n / index != index): 
                p = p * index
                p = p * int(n / index)
                # => p = p * n
            else:
                p = p * index
        index = index + 1
    
    if(ok == False):
        #in case the number does not have proper factors
        p = -1   

    return p
    
if __name__ == "__main__":
    n = int(input("Give a number: "))
    if product(n) == -1:
        print("Number doesn't have proper factors (is prime)")
    else:
        print(product(n))        