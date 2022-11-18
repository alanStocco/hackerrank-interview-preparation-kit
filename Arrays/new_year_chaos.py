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

# Time Complexity O(n) linear
def minimumBribes(Q):
    # Start end q, if q[i] != i  means that last person bribe and is in position i-1 or i-2. 
    # If is in left of position i-2 is too chaotic
    moves = 0 
    Q = [P-1 for P in Q]    
    for i,P in enumerate(Q):
        # print(f"i: {i} - P: {P}")
        if P - i > 2: # person is too far away from initial position so cheated more than two person
            print("Too chaotic")
            return
        # print(f"P-1 val: {P-1} e i: {i}")
        # Given position i in the queue I see the two persons just before in position i-2 and i-1, only if
        # person in position i is not in the initial position(so have brided someone)
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                moves += 1
            # if i==4:
            #     print(f"j: {j} Q[j]:{Q[j]}  --- P-1 val: {P-1} e i: {i} , moves: {moves}")
    # print(moves)
    return moves

if __name__ == '__main__':
    t = 2
    n = 5
    
    q = [2,1,5,3,4] # res 3
    # q = [2,5,1,3,4] # res Too chaotic
    # q = [1,2,5,3,4,7,8,6]  # res 8
    # q = [1,2,5,3,7,8,6,4] # res 7
    res = minimumBribes(q)
    print("Result : {}".format(res))
    
