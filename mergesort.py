
from random_file_gen import random_binary
import time
import sys
import psutil

# random_binary()




def mergeArray(s1, s2):
    a = 0
    b = 0
    arr = []
    while(a < len(s1) and b < len(s2)):
        if(s1[a] > s2[b]):
            arr.append(s2[b])
            b = b+1
        elif(s1[a] <= s2[b]):
            arr.append(s1[a])
            a = a+1
    if(a == len(s1)):
        arr.extend(s2[b:])
    elif(b == len(s2)):
        arr.extend(s1[a:])
    
    return arr

def mergeSort(arr):
   
    if(len(arr) == 1 or len(arr) == 0):
        return arr
    else:
        m = int(len(arr)/2)
        s1 = mergeSort(arr[:m])
        s2 = mergeSort(arr[m:])
        res = mergeArray(s1, s2)
    return res

#@profile
def cms(num):
    
    abc = []
    
    with open('X.dat', 'rb') as f:
        for _ in range(0, int(num)):
            block = f.read(4)
            list = [int.from_bytes(block, byteorder='little', signed=True)]
            abc += list
    print("before merge length", len(abc))


    abc = mergeSort(abc)

    with open('X1.dat', 'wb') as f: 
        for i in range(0, len(abc)):
            f.write(abc[i].to_bytes(4, signed=True, byteorder='little'))
            
    del abc


#@profile
def run():
    
    # Success
    # num = 32768; """For 0.125 mb file"""
    
    # Success
    num = 1048576; """For 4 mb file"""

    # Failed
    # num = 2097152; """For 8 mb file"""

    ram_available = psutil.virtual_memory().available
    print("Total ram available", ram_available/(1024*1024), "mb")
    print("Will be testing with ", num, "numbers")
    
    random_binary(num)

    cm_time_sta = time.time()

    cms(num)

    cm_time_end = time.time()
    cm_tim = cm_time_end - cm_time_sta
    print("classic Merge sort time(sec) = %f" %cm_tim)


# num = int(input())
if __name__ == '__main__':
    run()




