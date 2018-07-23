# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 23:51:19 2018

@author: DRB4
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
    trigger = 0
    base_10_n = n
    
    #print(list(range(20,-1,-1)))
    for pwr_two in range(20,-1,-1): # 0 through 20 in reverse
            
        if (base_10_n - 2**pwr_two) >= 0:
            trigger = 1
            
            list_binaries.append(1)
            base_10_n -= 2**pwr_two


        elif trigger == 1:
            list_binaries.append(0)
    
    #print(list_binaries)
    
    
    longest_chain = 0
    current_chain = 0
    
    for i in list_binaries:
        if i == 1:     # and current_chain >= 1:
            current_chain += 1
        
        #elif i == 1 and current_chain == 0:
            # list element is a 1 and current chain is fresh
            #current_chain += 1
            if current_chain > longest_chain:
                longest_chain = current_chain
                
        elif i == 0:
            # reset chain
            current_chain = 0
    
    print(longest_chain)
            
            
            
    
    
