"""
Passing Cars Problem
Prefix Sum Practice
by Codility

Solution by B Hamilton 7/24/2018

A non-empty array A consisting of N integers is given. The consecutive elements
 of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q),
where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:
A = [0, 1, 0, 1, 1]
Ans: 5


"""


def solution(A):
    # 0 <= P <  Q     ( < N)
    # implying a pass only coutns of P < Q

    # Count P (travel east) = 0
    # Count Q (travel west) = 1

    CurrentEastGoers = 0
    CurrentPasses = 0

    for i in range(len(A)):
        if A[i] == 0:  # 0 denotes eastgoing car
            CurrentEastGoers += 1
        elif A[i] == 1:  # 1 denotes qwest going car
            CurrentPasses += CurrentEastGoers  # all eastgoing cars pass the next westgoer
            if CurrentPasses > 1e9:
                CurrentPasses = -1
                break


    return CurrentPasses

    pass

"""RESUTS:
100% Task Score, 100% Correctness, 100% Performance
Time Complexity O(N)
