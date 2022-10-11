#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    tmp = []
    for i in range(4):
        for j in range(4):            
            # print("{} {} {}\n {} \n{} {} {}\n".format(arr[i][j], arr[i][j+1], arr[i][j+2] , arr[i+1][j+1] , arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2]  ))
            tmp.append(sum(arr[i][j:j+3]) + arr[i+1][j+1]  + sum(arr[i+2][j:j+3]) )    
    print(max(tmp))
    return max(tmp)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []
    arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    
    result = hourglassSum(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
