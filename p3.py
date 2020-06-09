# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

# these were some trial functions that ended up being too slow
#def is_factor(N, number):
#    if N % number == 0:
#        return True
#    return False
#
#def is_prime(number):
#    return not has_factor(number)
#
#def has_factor(number):
#    for i in range(2,int(math.sqrt(number))+1):
#        if number % i == 0:
#            #print(f"{number} divisible by {i}")
#            return True
#    return False

def largest_prime_factor(number):
    for i in range(2, int(math.sqrt(number))+1):
        while number % i == 0:
            number /= i
            maxprime = max([number,i])
    return maxprime

if __name__ == "__main__":
    N = 600851475143
    #N = 13195
    print(f"the largest prime factor of {N} is {largest_prime_factor(N)}")
