# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10,001st prime number?

from p5 import is_prime

if __name__ == "__main__":
    n = 10001
    nprime = 0
    i = 2
    while nprime < n:
        if is_prime(i):
            prime = i
            nprime += 1
        i += 1

    print(f"The {n}th prime is {prime}")
