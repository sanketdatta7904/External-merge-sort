
import numpy as np
import numpy.random as random
import sys
import os
import numpy as np
import math
import os
import sys
from random_file_gen import random_binary
import time
import psutil

somearr = []



def swap(arr, a, b):
    temp = arr[b]
    arr[b] = arr[a]
    arr[a] = temp


def partition(arr, s, e):
    a = arr[s]
    cout = 0
    for i in range (s, e+1):
        if(arr[i]<a):
            cout = cout +1
    cout = s+cout
    swap(arr, s, cout)
    si = s
    ei = e
    while(si<ei):
        if(arr[si]<a):
            si = si +1
        elif(arr[ei]>=a):
            ei = ei-1
        else:
            swap(arr, si, ei)
            si = si +1
            ei = ei-1
    # print(cout)
    return cout



def quickSort(arr, s, e):
    if(s>=e):
        return
    else:
        pivot = partition(arr, s, e)
        quickSort(arr, s, pivot-1)
        quickSort(arr, pivot+1, e)

    

# external marge sort


def external_merge_sort(num, block_size):
    # Buffer size denotes how many numbers will be taken at once for merging and also the threshold for output to the file
    B_size = block_size
    somearr = []

    filename_in = 'X.dat'
    filename_out = 'Y.dat'
    
    # print("Buffer Size, %d" % B_size)
    # print("num", num)
    
    #First Step: Sorting and adding to the file
    
    fin = open(filename_in, 'rb') 
    fout = open(filename_out, 'wb') 
    
    range_of_sort = math.ceil(num/B_size)
    # print("range_of_sort",range_of_sort)
    for _ in range(0, range_of_sort):   
        block1 = []
        for _ in range(0, B_size):
            try:
                block1.append(int.from_bytes(fin.read(4), byteorder='little', signed=True))
            except:
                break
        # quickSort(block1, 0, len(block1)-1)
        quickSort(block1, 0, len(block1)-1)
        while True:
            try:
                # print(block1[0])
                fout.write(block1.pop(0).to_bytes(4, signed=True, byteorder='little'))       
            except:
                break
                               
        del block1
    fin.close()
    fout.close()
    filename_in, filename_out = filename_out, filename_in

  

    # Sencond Step: streaming buffers to do two way merging for EM sort

    chunk_size = B_size
    while chunk_size < num:
        
        fin = open(filename_in, 'rb') 
        fout = open(filename_out, 'wb') 
        
        chunk_num = 0
        while 2 * chunk_size  * chunk_num  < num:
            block1 = []
            block2 = []
            block_merge = []
            block1_called = 0
            block2_called = 0
         
            fin.seek((chunk_num * 2 * chunk_size)*4 ,os.SEEK_SET)
            for i in range(0, B_size):
                try:
                    block1.append(int.from_bytes(fin.read(4), byteorder='little', signed=True))
                except:
                    break
            
            fin.seek((chunk_num * 2 * chunk_size + chunk_size )*4, os.SEEK_SET)
            for i in range(0, B_size):
                try:
                    block2.append(int.from_bytes(fin.read(4), byteorder='little', signed=True))
                except:
                    break
                    
            # print("chunk num and size 1st", (chunk_num * 2 * chunk_size)*4)        
            # print("chunk num and size 2nd", (chunk_num * 2 * chunk_size + chunk_size )*4)

            while True:
                # print("block1", block1)
                # print("block2",block2)
                # print("block_merge",block_merge)
                if (not block1) & (not block2):
                    break
                elif not block1:
                    block_merge.append(block2.pop(0))
                elif not block2:
                    block_merge.append(block1.pop(0))
                else:
                    if block1[0] <= block2[0]:
                        block_merge.append(block1.pop(0))
                    else:
                        block_merge.append(block2.pop(0))
    
                if len(block_merge) == B_size:
                    while True:
                        try:
                            somearr += block_merge
                            fout.write(block_merge.pop(0).to_bytes(4, signed=True, byteorder='little'))       
                        except:
                            break
            
                if ((not block1) & ((block1_called + 1) * B_size < chunk_size)):
                    block1_called = block1_called + 1
                    # print("block1_refill %d" %block1_called, (chunk_num * 2 * chunk_size + B_size * block1_called))
                    fin.seek((chunk_num * 2 * chunk_size + B_size * block1_called)*4 ,os.SEEK_SET)
                    

                    for i in range(0, B_size):
                        try:
                            block1.append(int.from_bytes(fin.read(4), byteorder='little', signed=True))
                        except:
                            break
                        
                if ((not block2) & ((block2_called + 1) * B_size < chunk_size)):
                    block2_called = block2_called + 1
                    # print("block2_refill %d" %block2_called, (chunk_num * 2 * chunk_size + chunk_size + B_size * block2_called))
                    fin.seek((chunk_num * 2 * chunk_size + chunk_size + B_size * block2_called)*4 ,os.SEEK_SET)
                    
                    for i in range(0, B_size):
                        try:
                            block2.append(int.from_bytes(fin.read(4), byteorder='little', signed=True))
                        except:
                            break
             
            while True:
                try:
                    somearr += block_merge

                    fout.write(block_merge.pop(0).to_bytes(4, signed=True, byteorder='little'))       
                except:
                    break
                    
            chunk_num = chunk_num + 1
            # print("chunk_size, chunk_num = %d" %chunk_size, chunk_num)
            
            del block1, block2, block_merge
    
        fin.close()
        fout.close()
    
        chunk_size = chunk_size * 2
        filename_in, filename_out = filename_out, filename_in
    
    # print(filename_in)
    # print("tot arr>>>>>>>>", somearr)
    # print("total em length", len(somearr))

# print(mergeSort([9,8,7,6,5,4]))
# external_merge_sort()


#@profile
def run(blocksize):
    # num = 16384
    # num = 32768; """For 0.125 mb file"""
    # num = 1048576; """For 4 mb file"""
    num = 2097152; """For 8 mb file"""
    # num = 8388608; """For 32 mb file"""
    # num = 16777216; """For 64 mb file"""
    # num = 33554432; """For 128 mb file"""
    ram_available = psutil.virtual_memory().available
    print("Total ram available", ram_available/(1024*1024), "mb")
    print("Will be testing with ", num, "numbers")

    random_binary(num)

    time_sta = time.time()

    external_merge_sort(num, blocksize)
    

    time_end = time.time()
    tim = time_end - time_sta
    print("emternal merge sort time(sec) = %f" %tim)



if __name__ == '__main__':
    print("Please enter the block size(Must be a number in 2 power table)")
    run(int(input()))
