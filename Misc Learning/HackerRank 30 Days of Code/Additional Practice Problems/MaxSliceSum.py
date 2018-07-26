"""
Max Slice Sum Problem
by Codility

Solution by B Hamilton

A non-empty array A consisting of N integers is given. A pair of integers (P, Q),
    such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a
    slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Given A and N, return maximum sum of any slice A.

Assume:
N ele int in [1, ..., 1e6]
each element of A is ele in in [ -1e6, ..., 1e6]

result element in [ - 2.417...e6, ..., 2.417...e6]

Target Complexity: Time O(N), Space O(N)

Results: Task Score 53%, Correctness 50%, Performance 60%
"""

def solution(A):

    # intuition:
    #
    P = [A[0]]

    for i in range(1,len(A)):

        # WIndow based on prefix sums
        # Sets P = A[0] for a starting point
        #

        P.append(P[i-1]+A[i])

        # I am missing an extra step here. The max of (P) is not sufficient
        # for the max of any slices
        # what we should be using is the max of P across all slices...
        # but that is O(N^2) or O(NlogN), not O(N)

        # Reviewing the test case results...:
        # This succeeds any time the max slice is P(i,i)

        # Brute force slice job: check all slices of as as differences of P
        # against all others (no duplicates)
        # No time for that yet.


    return max(P)

    # TEST CASES are a ibt opaque here:
    # 50 random numbers FAILED < --- telling
    #
    # failed 9/27 three-element lists
    #
    # failed 2/9 two-element lists
    #
    # passed 1 element lists
    #
    # passed Example
    #
    #
