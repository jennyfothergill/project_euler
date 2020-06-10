# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from p5 import is_prime

n = int(2e6)

primesum = 0
for i in range(2,n):
    if is_prime(i):
        primesum += i

print(f"The sum of primes below {n} is {primesum}")
