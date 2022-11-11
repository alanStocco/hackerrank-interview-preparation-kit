#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

# Brute Force solution. Time Complexity O(n^2) with n= len(q)
# For each person that have current position different 
# from original I can see the number on the right that are smaller
# sum these numbers for each one and if a single number is greater of 2 give Too chaotic
def minimumBribes_bf(q):        
    min_bribes = 0
    for idx,v in enumerate(q):        
        # print(f"IDX: {idx} - V: {v}")    
        counter_bribes = 0
        for idx_dx,v_dx in enumerate(q[idx+1:None]):
            # print(f"Interno. Indice: {idx_dx} - Valore: {v_dx}")   
            if v_dx < v:
                counter_bribes = counter_bribes + 1
            if counter_bribes > 2:
                return("Too chaotic")        
        min_bribes = min_bribes + counter_bribes
    return min_bribes    

# TODO better time complexity
# def minimumBribes_v2(q):
#     return None

if __name__ == '__main__':
    t = 2
    n = 5
    
    q = [2,1,5,3,4] # res 3
    q = [2,5,1,3,4] # res Too chaotic
    q = [1,2,5,3,4,7,8,6]  # res 8
    res = minimumBribes_bf(q)
    print("Result : {}".format(res))
    
