""""
Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to expend those calories. 
If Marc has eaten j cupcakes so far, after eating a cupcake with c calories he must walk at least 2 x c miles to maintain his weight. 

Example 
    calorie = [5, 10, 7] 

If he eats the cupcakes in the order shown, the miles he will need to walk are (20 x 5) + (21 x 10) + (22 x 7) = 5+ 20+ 28 = 53. 
This is not the minimum, though, so we need to test other orders of consumption. In this case, our minimum miles is calculated 
as (2° x 10) + (21 x 7) + (22 x 5) = 10 + 14 + 20 = 44. 

Given the individual calorie counts for each of the cupcakes, determine the minimum number of miles Marc must walk to maintain his weight. 
Note that he can eat the cupcakes in any order. 

Function Description 
    Complete the marcsCakewalk function in the editor below. 
    marcs Cakewalk has the following parameter(s): 
        int calorie[n]: the calorie counts for each cupcake 

Returns 
    long: the minimum miles necessary
"""

# Solution :

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    # Write your code here
    calorie.sort(reverse=True)
    n = len(calorie)
    sum = 0
    for i in range(n):
        sum += ((2**i) * calorie[i])
    return sum
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
