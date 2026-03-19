""""
Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests, Initially her luck balance is 0. She belleves in "saving luck and wants to check her theory. Each contest is described by two integers. 1 and 2

2/6 is the amount of luck associated with a contest. If Lena wwis the contest, her luck balance wil decrease by 2 if she loses it, her luck balance will increase by Li

Conte

Sub

Max S

Diffica

7) denotes the contest's importance rating, it's equal to I if the contest is important, and it's equal to 0 if

It's unimportant

Rate Y

esc

If Lena loses no more than ke important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? This value may be negative

Example

L-5,1,4 T=1,1,0

Contest

If Lena loses all of the contests, her will be 5+1+4 10. Since she is allowed to inse 2 important.contests and there are only 2 important contests she can lose all three contists to maximize her luck at 10

Function Description

Ifk 1 she has to win at least 1 of the 2 important contests. She would choose to win the lowest value Important contest worth 1. Her final luck will be 5+4-1-8

Complete the luck Balance function in the editor below.

luckBalance has the following parameter(s):

mtk. the number of important contests Lena can lose

int contests/n)(2): a 20 array of integers where each contests contains two integers that represent the

luck balarice and importance of the 1 contest

Returns

int the maximum luck balance achievable.
"""
# Solution :
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    important = []
    luck = 0

    for l, t in contests:
        if t == 0:
            luck += l
        else:
            important.append(l)

    important.sort(reverse=True)
    luck += sum(important[:k])
    luck -= sum(important[k:])
    return luck
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
