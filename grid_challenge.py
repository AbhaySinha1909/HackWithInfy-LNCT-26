"""
Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the
columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

Example

grid['abc','ade', 'efg']

The grid is illustrated below.

abc

ade

efg

The rows are already in alphabetical order. The columns a ae, bd fand cegare also in alphabetical order, so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.

Function Description

Complete the gridChallenge function in the editor below.

gridChallenge has the following parameter(s):

string grid[n]: an array of strings

Returns

string: either YES or NO

Input Format

The first line contains t, the number of testcases.

Each of the next t sets of lines are described as follows:

The first line contains n, the number of rows and columns in the grid.

- The next lines contains a string of length n

Constraints

1<t<100

1 ≤ n ≤100

Each string consists of lowercase letters in the range ascii[a-z]
"""

# Solution :
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    n = len(grid)
    sorted_grid = []
    for i in grid:
        a = ''.join(sorted(i))
        sorted_grid.append(a)
    
    m = len(grid[0])
    sorrted = True
    for col in range(m):
        for row in range(1, n):
            if sorted_grid[row][col] < sorted_grid[row - 1][col]:
                sorrted = False
                break
        if not sorrted:
            break

    if sorrted:
        return 'YES'
    else:
        return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
