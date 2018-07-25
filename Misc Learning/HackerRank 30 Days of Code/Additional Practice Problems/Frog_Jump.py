"""
Frog Jump Problem

Solution by B Hamilton 07242018

Write a function:
def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from
position X to a position equal to or greater than Y.
For example, given:
  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Assume that:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
"""


import math

def solution(X, Y, D):
    # write your code in Python 3.6
    # POS = n * D + X >= Y
    # n >= (Y - X) / D
    # smallest value of n to satisfy this...
    # n = (Y - X) / D + (0 if equal, 1 if inequal)
    return math.ceil((Y-X)/D)


    pass


"""
RESULTS:
Task, Performance, Space Scores 100%
O(1) Complexity

"""
