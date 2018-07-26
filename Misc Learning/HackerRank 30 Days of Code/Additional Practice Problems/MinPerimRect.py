"""
Minimum Perimeter Rectangle
by Codility

Solution by B Hamilton


Given an integer N, returns the minimal perimeter of any rectangle whose
    area is exactly equal to N.

For example, given an integer N = 30, the function should return 22

Assume:
N is an integer within the range [1..1,000,000,000].
expected worst-case time complexity is O(sqrt(N));
expected worst-case space complexity is O(1).

Results:
90% Task Score | 100% COrrectness | 80% Performance

Note: I did this problem twice. The first time I earned a much lower score
because I was not checking to ensure A was an integer given B and N integers.
This required checking P was Even since P. Reading this again, I think
I see a leaked edge case where A = integer + 0.5 . Did not go back to check it.
"""

from math import sqrt, floor

def solution(N):
    # write your code in Python 3.6

    # N (int) : AREA of RECTANGLE
    # A, B (int?) : LENGTH of SIDES
    # N = A * B
    # P = 2 A + 2 B : PERIMETER
    #
    # Given N, return the minimal perimeter whose area is exactly equal ot N

    # Constraints:
    # N as int in range(1, 1e9)
    # complexity: O(root N) <----- hint

    # P = 2 N/B + 2B = 2 ( N/B + B ) = 2 * (N + B^2)/B

    def PFunc(B,N):
        return (2 * ( N + B ** 2) / B)

    # ASSUME B has to be an Integer 1+
    # B from 1 to sqrt(N)
    P = 1e9 + 1 # a safe high value (values for small N were problematic)
    for i in range(1, floor(sqrt(N))+1):

        if (PFunc(i,N) % 2) == 0: #an integer: Need % 2 here;
            #the % to see if it is integer, the 2 to see if it is even...
            #since P = 2 (A + B), P must be even
            P = min(P, PFunc(i,N))

    return int(P)

# Test Cases:
# N = 1, N - 36, N - 48, N = 101, 1234, 4564320, 10000000.., 1000000000
# N = 982451 (prime) failed, it says I got 1e9+1, which is my default P valu
# and the actual answerwas 1.964...e9 ... which is OUTSIDE constrain bounds!!!
#
# Performance Checks passed other than that wrong answer.
