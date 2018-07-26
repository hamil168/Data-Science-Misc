"""
CountFactors Problem
by Codility

Solution by B Hamilton


A positive integer D is a factor of a positive integer N if there exists an
integer M such that N = D * M.

Ex: 6 is a factor of 24, because M = 4 satisfies the above condition

Write a Fxn, given a positive integer N, returns the number of its factors.

Constraints:
N = [1, ... , 2,147,483,657]

Target Complexity: Time O(root N) | Space O(1)
Task Score: 100% | Correctness 100% | Performance 100%

"""

# O(root N) is a good hint. Every number A from
# 1 to Root N represents 2 factors: A and N / A
# If A is 1 or root N, you can't double count it
# these are only worth 1 (had to figure that out during debugging edges)

import math

def solution(N):

    # Key intuition...  the largest factor of a number is itself.
    # So you have to go through M = 0... ...sqrt(N)
    # and test N  % M == 0
    # count factors
    count = 0

    for i in range(1, math.floor(math.sqrt(N))+1): # +1 for indexing!
        if N % i == 0:
            count += 2 # one for i, one for 24/i

    # 1 is an edge case
    # squares is an edge case
    # both over coutn by 1, so wrap them
    # into this:
    if math.sqrt(N) % 1 == 0:
        count -= 1

    return count

    # Test Cases:
    # Passed all tests
    # Squares N = 16, N = 3
    # tiny N <= 10
    # simple N = 41 (prime), N = 42
    # N = 1
    # N = 7! or 6!
    # N = 2 ^ 28  (which is a square)
    # N = MAX_INT
