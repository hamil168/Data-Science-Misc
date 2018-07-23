# -*- coding: utf-8 -*-
"""
Hacker Rank 30 Days of Code 14 - Scope


Created on Sun Jul 22 23:53:27 2018

@author: DRB4

Task: 
complete Difference class
- class constructor that takes an array of integers and 
saves it to an instance variable named elements
- computeDifference method that finds the maximum absolute different between
any 2 numbers in N and stores it in the maximumDifference instance variable

1 <= N <= 10
1 <= elements[i] <= 100, where 0 <= i <= N - 1

"""

### MY CODE ###
class Difference:
    def __init__(self, a):
        self.__elements = a
       

    def computeDifference(self):
        self.maximumDifference = 0
        
        # Need the difference of every element with each other
        # count over i
        for i in range(len(self.elements)):
            
            # count over i again, only call it j
            for j in range(len(self.elements) - i):
                # len(elements) - 1 to keep from double counting
                                
                diff = abs(self.elements[i] - self.elements[j])
                
                if diff > self.maximumDifference:
                    self.maximumDifference = diff
        
        return self.maximumDifference
    
    pass


# End of Difference class
################# HR CODE ##################
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

# TEST CASES
# input [1 2 5] output: 4  SUCCESS
# input [8 19 3 2 7] output: 17 SUCCESS