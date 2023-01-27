Implement classical MergeSort and External Memory MergeSort (with 2-way merge in the internal memory). written a small program that generates random numbers
and writes them directly into a file.

Testing:
A. Ways to create a virtual environment with Docker

docker run -it -m 64MB -v <directory> --name python python:3.9-slim bash
    
** Use the file location instead of "<directory>" above
Now once you are inside docker container:

apt-get update
apt-get install build-essential
pip3 install memory-profiler requests
pip3 install numpy
pip3 install psutil


B. Conditions under which the programme(EM) works.
1. We need to pass data in the power of 2
2. We need to pass buffer size in the power of 2

C.  Testing the Sanity of both programs:
To run the test case for testing the accuracy of both classical merge sort and external merge sort
We created testFile.py to ensure the classical merge sort output is identical to the external merge sort output. The program generates a file of random numbers and both classical merge sort and external merge sort operates on the same input file. Once both operation is finished, It tests the accuracy of both processes and prints the result as boolean. We used three test cases where different random number size and different block sizes were provided to verify the accuracy of both programs(~32kb, ~64kb, ~128kb).
   
Command:
python exercise01/testFile.py

and then provide any option between 1/2/3


D. Command for testing the memory and time consumption for External merge sort:

Memory:

1. Uncomment @profile 
just before 
def run() in mergesort.py   #at line number 63 
and 
def run() in external_mergesort.py  #at line number 209

2. Run python code with -m memory_profiler option 

classic merge sort: python -m memory_profiler exercise01/mergesort.py
external merge sort: python -m memory_profiler exercise01/external_mergesort.py

Time:
Every time the program runs, It calculates the time taken for the execution and prints it in the console. This is the data used in the graph for the final report.

*** The testcases used in the graph is mentioned in the function for both classical merge sort and external merge sort (function name in both files : run()) and the respective file size is also mentioned. Please uncomment the number for testing respective test cases.
