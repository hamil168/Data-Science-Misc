"""
Sorting Problem Practice
From Codility




Write a function

def solution(A)

that, given an array A consisting of N integers, returns the number of distinct
 values in array A.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.




RESULTS:
100% Correctness
0% Performance (scored O(N^2) when needed O(n log n)
"""


def solution(A):
    # write your code in Python 3.6

    # Use a bubble sort.
    # Any time there are duplicates, drop the duplicate
    # Then get length of the final array
    #print(A)
    # single pass

    # STEP 1: BUBBLE SORT
    for j in range(1,len(A)-2):

        for i in range(len(A)-j):  # -1 b/c we compare 2 elements

            A[i], A[i+1] = min(A[i],A[i+1]), max(A[i],A[i+1])
            #print(A)

    # STEP 2 GET INDICIES OF DUPLICATES
    poplist = []
    for k in range(len(A)-1):
        if A[k] == A[k+1]:
            poplist.append(k)
            #print(poplist)

    # STEP 3 POP DUPLICATES FROM HIGH INDEX TO LOW
    for i in poplist[::-1]:
        A.pop(i)

    #print(A)

    return len(A)
    pass
