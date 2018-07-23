# -*- coding: utf-8 -*-
"""
Hacker Rank 30 Days of Code Day 10
Binary Numbers 


Created on Sun Jul 22 23:51:19 2018

@author: DRB4


TASK: Given a Base-10 Integer, convert it to Base-2
THEN: Print the base-10 integer denoting the maximum number
    of consecutive 1's in n's binary represenation.
    
Input Format: integer n
Constraints: 1 <= n <= 10e6
Output Format: base 10 integer

ex: input(5) returns (1) b/c 5 is 101 ... longest chain of 1's is 1.
ex: input(6) returns (2) b/c 6 is 110 ... longest chain of 1's is 2.

My Strategy:
    - Note that 2^20 is the first power of 2 greater than 10e6
    - Planning on converting n into a list of 1's and 0's
    - e.g. 5 -> [1,0,1]
    - To account for n constraints, we have to examine every power of 2
    - from 20 to 0 (actually, 19 to 0)

Start with n
Start with the highest power of 2 (19)
Subtract 2^19 from n. If that is < = 0, append nothing to the list
move on to the next power of 2
...
...
and in the case of n = 5:
Subtract 2^2 from n. 5 - 4 >= 0
    set a trigger declaring it is OK to append values
    append a 1 to the list
    set n to (5 - 4)
Subtract 2^1 from (5 - 4); 1 - 2 < 0, 
    append a 0
    n doesn't change
subtract 2^0 from (5 - 4); 1 - 1 >= 0, 
    append a 1
    n goes to 0
    
    
COUNTING THE CHAINS:
    starting from left to right, greedy
    - track the length of the current_chain
        - reset to 0 when you hit a 0
    - keep track of longest_chain so far
    - update longest_chain when applicable
    
    
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    # 1 <= n <= 1e6 (1 million)
    # 2 ^ 20 ~ 1e6
    
    
    list_binaries = []
    base_10_n = n
    
    trigger = 0   # trigger keeps us from adding leading zeros
    
    for pwr_two in range(19,-1,-1): # 0 through 19 in reverse
            
        if (base_10_n - 2**pwr_two) >= 0:
            # activate the trigger
            trigger = 1         
            list_binaries.append(1)
            base_10_n -= 2**pwr_two

        # only add 0's if the trigger is activated
        elif trigger == 1:
            list_binaries.append(0)
      
    longest_chain = 0
    current_chain = 0
    
    
    for i in list_binaries:
        if i == 1:
            current_chain += 1
            
            # update longest_chain
            if current_chain > longest_chain:
                longest_chain = current_chain
                
        elif i == 0:
            # reset chain
            current_chain = 0
    
    print(longest_chain)
            
            
            
    
    
