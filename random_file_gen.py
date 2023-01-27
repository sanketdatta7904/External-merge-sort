import numpy.random as random
import os
import sys

def random_binary(num):
    
    int32_maxsize = 1000000
    print("generating rand data from", 0, "to", num)
    with open('X.dat', 'wb') as f: 
        for _ in range(0, num):
            f.write(random.randint(1, int32_maxsize).to_bytes(4, signed=True, byteorder='little'))

    print("random filesize",os.path.getsize('X.dat')/(1024*1024), "mb") 

# random_binary()

