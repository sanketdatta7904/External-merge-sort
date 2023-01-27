
# THis program is to test the sanity of the external merge sort with comparison of classic merge sort

from mergesort import cms
from random_file_gen import random_binary
import sys
import psutil
import math
import numpy as np

# from external_mergesort import external_merge_sort as ems
from external_mergesort import external_merge_sort as ems

# import external_mergesort



def test_file(choice):
    
    if(choice == 1):
    #---- Test case 1
        num=8192 # 0.031 MB
        block_size=16
    elif(choice == 2):
    #---- Test case 2
        num=32768 # 0.125 MB
        block_size=64
    elif(choice == 3):
    #---- Test case 3 
        num=16384 #0.0625 MB
        block_size=2048 
    
    ram_available = psutil.virtual_memory().available
    print("Total ram available", ram_available/(1024*1024), "mb")
    print("Will be testing with ", num, "numbers")
    import time
    random_binary(num)

    # Testing classical merge sort
    cm_time_sta = time.time()
    cms(num)
    cm_time_end = time.time()
    cm_tim = cm_time_end - cm_time_sta
    print("classic Merge sort time(sec) = %f" %cm_tim)

    # Testing External merge sort
    em_time_sta = time.time()
    ems(num, block_size)
    em_time_end = time.time()
    em_tim = em_time_end - em_time_sta
    print("External Merge sort time(sec) = %f" %em_tim)

    cm_file_name = 'X1.dat'
    em_file_name = 'X.dat'
    cm_list = np.array([])
    em_list = np.array([])
    
    with open(cm_file_name, 'rb') as cm:
        for _ in range(0, int(num)):
            cblock = cm.read(4)
            cnum = int.from_bytes(cblock, byteorder='little', signed=True)
            cm_list = np.append(cm_list, cnum)
    with open(em_file_name, 'rb') as em:
        for _ in range(0, int(num)):
            eblock = em.read(4)
            enum = int.from_bytes(eblock, byteorder='little', signed=True)          
            em_list = np.append(em_list, enum)

    print("Record count of classic merge sort", len(cm_list))
    print("Record count of external merge sort", len(em_list))
    # matchedCount = 0
    # notMatchedCount = 0
    print("matching",(cm_list == em_list).all())
    # for i in range (0, len(cm_list)-1):
    #     if(cm_list[i] == em_list[i]):
    #         matchedCount += 1
    #     else:
    #         notMatchedCount +=1

    # print({"matchedCount": matchedCount, "notMatchedCount": notMatchedCount})
print("test case number:1/2/3 ")
choice = int(input())
test_file(choice)