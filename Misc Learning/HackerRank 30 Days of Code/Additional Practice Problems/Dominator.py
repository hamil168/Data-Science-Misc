"""
Dominator Problem
by Codility

Solution by B Hamilton

An array A consisting of N integers is given.

The dominator of array A is the value that occurs in more than half of the
elements of A.

Write a function that, given an array A consisting of N integers, returns
    index of any element of array A in which the dominator of A occurs.
    The function should return −1 if array A does not have a dominator.

(Given) Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range
    [−2,147,483,648..2,147,483,647].

Target Complexity: Time O(N) oor O(NlogN) | Space O(1)

Task Score: 83% | Correctness: 75% | Performance 100% 
"""
def solution(A):
    # I think I cna use a hassh table here,
    # but that will make a solution that is O(N) or worse
    # I may not know how to do so, anyway...
    # I will try a greedy math-based algorithm

    # Key intuition is that the max will have
    # as many coutns as all the others combined, except 1.
    # and so every time we change to a number that isn't the max,
    # decrease the count
    # every time we repeat a number, increase the count
    # In the end, the sum should be 1ish.

    # a,b,c,a,a,d,a,a    1, -1, -1, -1, +1, +1, -1, -1, + 1 = -1

    # may need to do a every time we change the number that is not the
    # 'max', decrease by 1.

    # If A[0], get Id (i.e. a) and Ct (+1)
    # A[1], Id (!=a) so Ct 7483-1
    # A[2] Id [!=a]

    # Constraints
    if len(A) < 0 or len(A) > 100000 or A == []:
        return -1

    #if any(A < -2147483648) or any(A >  2147483647):
    #    return -1

    dominator = None
    dominator_count = 0
    dominator_indices = []

    if len(A) == 0:
        return -1

    for i in range(len(A)):   # an O(N) operation
        #any time the count is 0...
        #the incoming number becomes the dominator
        #and increment the count by 1
        if dominator_count == 0:
            dominator = A[i]
            #dominator_indices.append(i)
            dominator_count += 1

        # if the incoming number is the same as the dominator
        # increment by 1
        # appemd the index
        elif A[i] == dominator:
            dominator_count += 1
            #dominator_indices.append(i)

        # incoming number is the same as the dominator
        # decrement by 1. If this reduces it to 0, the dominator
        # will change on the next pass.
        # pop the end of the stack
        else:
            dominator_count -= 1
            #dominator_indices.pop()

    # A second O(n) operation
    dominator_indices= [idx for idx, num in enumerate(A) if num == dominator]

    # What happens when we end with dominator_count = 0?
    # edge cases where failed
    # all different, non-dominator.
    # need to double check the length is big enough!
    if len(dominator_indices) == 0:
        dominator_indices = [-1]
    elif len(dominator_indices) < round(len(A)/2):
        dominator_indices = [-1]

    #print(dominator_indices)
    # I can generate the indices, but it will not let me
    # Maybe it allows me to return ANY of the indices
    return dominator_indices[0]

# Test Cases that failed:
# any wher len(A) %2 == 0, split 50/50
# half elements the same, and half + 1 elements the same (got 10/20 for value 2,
# but 2 needed 11 to be the dominator
#
# N/2 values of 1, N even + [0,0,1,1,1] (for N = 4, not sure how this works)
#
#
