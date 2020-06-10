# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt

n = 1000

def is_triplet(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    return False

def find_triplet(n):
    for a in range(1, n):
        for b in range(a+1, n):
            for c in range(1000-a-b, n):
                #print(a,b,c)
                if a+b+c == n:
                    if is_triplet(a,b,c):
                        return a,b,c


a,b,c = find_triplet(n)
print(f"The sum of triplet {a}, {b}, and {c} = 1000")

