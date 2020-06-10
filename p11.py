# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

# (in file p11_grid)

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

import numpy as np

width = 4

grid = np.genfromtxt("p11_grid")
lr = grid.shape[0]

def horizontal(grid, width):
    maxprod = -1
    for row in grid:
        for start in range(lr-width+1):
            nums = row[start:start+width]
            product = np.prod(nums)
            if product > maxprod:
                maxprod = product
                maxnums = nums
    return maxprod,maxnums

def diagonal(grid, width):
    maxprod = -1
    for offset in range(-(lr-width),lr-width+1):
        row = np.diagonal(grid, offset)
        rl = len(row)
        for start in range(rl-width+1):
            nums = row[start:start+width]
            product = np.prod(nums)
            if product > maxprod:
                maxprod = product
                maxnums = nums
    return maxprod,maxnums


prodh,numsh = horizontal(grid, width)
prodv,numsv = horizontal(grid.T, width)
if prodh > prodv:
    maxprod = prodh
    maxnums = numsh
    print("horizontal product > vertical product")
else:
    maxprod = prodh
    maxnums = numsh
    print("horizontal product > vertical product")

prodf,numsf = diagonal(grid, width)
if prodf > maxprod:
    maxprod = prodf
    maxnums = numsf
    print("diagonal product > former max")

prodb,numsb = diagonal(np.fliplr(grid), width)
if prodb > maxprod:
    maxprod = prodb
    maxnums = numsb
    print("reverse diagonal product > former max")

print(
f"""\nThe greatest product of {width} adjacent numbers
is {maxnums} = {maxprod}"""
)

