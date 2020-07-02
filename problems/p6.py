# The sum of the squares of the first ten natural numbers is,
# 1^2+2^2+...+10^2=385
#
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)^2=55^2=3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import numpy as np

n = 100

n_array = np.arange(1, n+1)

sum_of_squares = np.sum(n_array**2)

square_of_sum = np.sum(n_array)**2

difference = square_of_sum - sum_of_squares
print(f"""
The difference between the sum of the squares
and the square of the sum of the natural numbers
from 1 to {n} is {difference}
""")
