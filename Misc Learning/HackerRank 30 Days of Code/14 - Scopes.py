# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 23:53:27 2018

@author: DRB4
"""

### MY CODE ###
class Difference:
    def __init__(self, a):
        self.__elements = a
       

    def computeDifference(self):
        self.maximumDifference = 0
        
        for i in range(len(self.elements)):
            
            for j in range(len(self.elements) - i):
        
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