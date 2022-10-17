#!/bin/python3

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

# Complexity O(len(a)-d)+O(d)  see https://wiki.python.org/moin/TimeComplexity#list
def rotLeft(a, d):    
    return a[d:] + a[:d]

if __name__ == '__main__':

    d = 48

    a = [431,397,149,275,556,362,852,789,601,357,516,575,670,507,127,888,284,405,806,27,495,879,976,467,342,356,908,750,769,947,425,643,754,396,653,595,108,75,347,394,935,252,683,966,553,724,629,567,93,494,693,965,328,187,728,389,70,288,509,252,449]

    result = rotLeft(a, d)
    print(result)
