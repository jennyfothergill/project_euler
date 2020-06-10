#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
import numpy as np

def is_factor(i,number):
    if number % i == 0:
        return True
    return False

def get_factors(number):
    factors = []
    remainder = number
    for i in range(2,int(math.sqrt(number))+1):
        while remainder % i == 0:
            remainder /= i
            factors.append(i)
    if remainder != 1:
        factors.append(remainder)
    return factors

def is_prime(number):
    return not has_factor(number)

def has_factor(number):
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            return True
    return False

def merge_lists(l1, l2):
    for i in l1:
        try:
            l2.remove(i)
        except ValueError:
            pass
    l1.extend(l2)
    return l1


if __name__ == "__main__":
    n = 20
    factors = [i for i in range(2,n+1) if is_prime(i)]
    guess = np.prod(factors)
    heck = True
    while heck:
        for i in range(2,n+1):
            if guess % i != 0:
                ifactors = get_factors(i)
                factors = merge_lists(ifactors,factors)
                guess = np.prod(factors)
                break
        if i == n:
            heck = False
    print(f"""
    {guess} is the smallest number which is evenly divisible
    from numbers 1 through {n}"""
    )
