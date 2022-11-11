#!/bin/python3

def minimumSwaps(arr): 
    #initialize number of swaps as 0 
    swaps = 0
    #create a dictionary which holds value, index pairs of our array
    #[4,3,1,2] --> {4: 1, 3: 2, 1: 3, 2: 4}
    getIndex = dict(zip(arr,range(1,len(arr)+1)))
    print("START getIndex: {} ".format(getIndex))    
    for i in range(1,len(arr)+1):
        #swap only if value is not equal to index
        # if i==5:
        #     print("START getIndex: {} e arr {}".format(getIndex, arr))    
        # print("getIndex[i]= {} i:{}".format(getIndex[i], i))
        print("getIndex[i cioè {}]: {} - getIndex[arr[i-1] cioè {}]: {} ".format(i, getIndex[i], arr[i-1], getIndex[arr[i-1]] ))
        if getIndex[i]!=i: 
            """
            Example of a proper swap when i=1
            {4: 1, 3: 2, 1: 3, 2: 4} --> {4: 3, 3: 2, 1: 1, 2: 4}
            [4,3,1,2] --> [1,3,4,2]
            Full swap is not required i.e. we don't have to set 1:1 or arr[0]=1(i:i or arr[i-1]=i) because we will never use these two values again. Therefore we can keep these two values as it is. And thus our swap looks as follows.
            {4: 1, 3: 2, 1: 3, 2: 4} --> {4: 3, 3: 2, 1: 3, 2: 4}
            [4,3,1,2] --> [4,3,4,2]
            """
            getIndex[arr[i-1]]=getIndex[i]
            arr[getIndex[i]-1]=arr[i-1]
            swaps+=1
            # if i==2:
            #     print(getIndex)
            # print("getIndex: {} con i: {} ".format(getIndex,i))                
                # return
    return swaps

def minimumSwaps__(arr):
    temp = [0] * (len(arr) + 1)
    print("START arr: {}".format(arr))
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    print("TEMP: {}".format(temp))
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    return swaps

# First version, for each value loop all the rest of the array
# With n as len(arr) complexity is O(n^2). Bad
def minimumSwaps_old(arr):
    # Base check if first it's 1 ok like that
    count = 0
    print("START arr: {}".format(arr))
    for i,v in enumerate(arr):        
        print("")
        print("I is: {} and value arr[i]: {}".format(i, arr[i]))         
        j = len(arr)
        for _ in arr[i+1:]:   
            j-=1
            if j>i:
                print("J is: {} and value arr[j]: {}".format(j, arr[j]))         
                if arr[i] > arr[j]:
                    print("Swap Indexes({},{})".format(i,j))
                    print("Swap Values({},{})".format(arr[i],arr[j]))
                    arr[i], arr[j] = arr[j], arr[i]
                    print("After swapping arr: {}".format(arr))
                    count+=1
    print(arr)
    return count

if __name__ == '__main__':
    a = [7, 1, 3, 2, 4, 5, 6] # 5
    a = [2,3,4,1,5]     # 3
    # a = [1,3,5,2,4,6,7] # 3
    
    # a = [3,7,6,9,1,8,10,4,2,5] # 9
    a = [4,3,1,2] # 3

    result = minimumSwaps(a)
    print(result)
