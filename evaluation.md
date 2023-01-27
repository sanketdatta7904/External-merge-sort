# General

* README: Here it could make sense to use markdown syntax for better readability.
* Nice that you used docker to simulate the RAM.

# Paper
* Abstracts: I wouldn't call EMMS a well known sorting algorithm.
* 2: Mergesort is a bit to shortly summarized.
* 2: EMMS belongs in chapter 3. Chapter two is for describing the task at hand (sorting), the baseline algorithm (Mergesort) and maybe baseline concepts (EM-model).
* 4.1: Less memory would also not really make a lot of sense here.
* 4.2: It is nice that you explain why Mergesort only ran for this small datasize. And python is also not the best choice for a programming language when it comes to efficiently implementing algorithms.
* 4.2: It's interesting that Mergesort runs so much faster than EMMS. On this level EMMS should easily be ablue to load all the data into the RAM and just run Quicksort a single time.
* Nice figures.

# Code

* Testcases look alright-ish. But instead of compairing both of the sorted arrays with each other, id check if they are correctly sorted
* Poorly documented
* What does `partition` in external memory mergesort
* Reading and writing seems to be well done.

# Overview

# Assessment
* Pass

