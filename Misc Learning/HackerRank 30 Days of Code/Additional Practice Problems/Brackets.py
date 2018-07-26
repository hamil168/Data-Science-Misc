"""
Brackets Problem
by Codility

Solution by B Hamilton

String S consisting of N characters is considered to be properly nested if any
of the following conditions is true:

- S is empty;
- S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
- S has the form "VW" where V and W are properly nested strings.

Ex the string "{[()()]}" is properly nested but "([)()]" is not.

Given a string S consisting of N characters, returns 1 if S is properly nested
and 0 otherwise.

N ele integer in [0, ... ,200,000]
S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")"

Expected Complexity: Time O(N) | Space (1)

Result: Task 75% | Correctness 66% | Performanc)e  80%

"""

def solution(S):
    # Implement as eptying a stack

    # Take first element  {
    # add to stack  
    # take second element
    # is it the closure of first element?   }
    # if so, pop first element. Properly nested.
    # otherwise, is it start of a second nest?   (
    # if so, add it to the stack
    # otherwise, is it a close of a different nest? )
    # if so, not a proper nesting

    if S == '':
        return 1   # corrected typo from my first submission

    Stack_Length = 0
    Type = "Placeholder"
    Stack = []
    Opens = ['{', '(', '[']
    Dict = {'{': 'Squiggle', '(': 'Curve', '[': 'Square', '}': 'Squiggle', ')': 'Curve', ']': 'Square'}
    output = 0

    for i in range(len(S)):

        if S[i] in Opens:
            Stack.append(S[i])
            Type = Dict[S[i]]
            output = 0

        elif Dict[S[i]] == Type: # Close brackets
            Stack.pop()

            if len(Stack) == 0:    #print special cases
                Type = None
            else:
                Type = Dict[Stack[-1]]  # this breaks down if we are at the last element

            output = 1

        elif Dict[S[i]] != Type: # close brackets of any other sort
            return 0

    return output

# TEST CASES:
#
# Examples 1 and 2 (not shown here) PASS
# Negative Match Examples PASS
# Empty String pass
# Simple Group poss and neg test, length - 22 ... Fail (got 1 expected 0)
# Performance Test:
# 10k+1 x "(" followed by 10k x ')' + ')( ' + '()'  Fail got 1 expected 0
