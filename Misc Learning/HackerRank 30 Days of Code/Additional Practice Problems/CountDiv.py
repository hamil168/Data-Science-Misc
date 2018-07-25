
"""CountDiv Practice Problem
by Codility

Solution by B Hamilton 7/24/2018

given three integers A, B and K, return the number of integers
within the range [A..B] that are divisible by K, i.e.:
{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2,
function should return 3,
because there are three numbers divisible by 2 within the range [6..11],
namely 6, 8 and 10.

Assume that:
A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
Complexity:

expected worst-case time complexity is O(1);
expected worst-case space complexity is O(1).

"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    # This is in the "prefix sum" section
    # But I don't think we need a prefix sum
    # We just need the values and
    # Intuition

    return ( (B - A)// K  + 1)

    pass


"""
RESULT:
50% of Task Score
75% of Performance
25% of Correctess
Having difficulty with this one. Will need to research further!
Failed on: A=B in {0,1}, K = 11 for A=B=1 got 1 expected 0
- A=10, B = 10, K in {5, 7, 20} for 5 and 20 (got 1 expected 0
)
Failed o A=101, B = 123M, K = 10K  (Got 12346 expected 12345)
"""
