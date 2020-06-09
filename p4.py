# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
    nstring = str(number)
    length = len(nstring)
    half = int(length/2)
    if length % 2 == 0:
        palindrome = nstring[:half]+nstring[half-1::-1]
    else:
        palindrome = nstring[:half]+nstring[half::-1]
    if nstring == palindrome:
        return True
    return False

def max_palindrome_product(digits):
    high = int("".join(["9"]*digits))
    low = int("".join(["1"]+["0"]*(digits-1)))
    maxpal = -1
    for i in range(high,low,-1):
        for j in range(high,low,-1):
            product = i*j
            if product > maxpal:
                if is_palindrome(product):
                    maxpal = product
                    maxi = i
                    maxj = j
    return maxi, maxj, maxpal

if __name__ == "__main__":
    i,j,pal = max_palindrome_product(3)
    print(f"{i}x{j} = {pal}")
