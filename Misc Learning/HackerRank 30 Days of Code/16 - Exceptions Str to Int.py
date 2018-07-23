# -*- coding: utf-8 -*-
"""
Hacker Rank 30 Days of Code Day 16 - Exceptions Strings to Integers

Created on Sun Jul 22 23:59:13 2018

@author: DRB4


Task: read a string S, print its integer value else print 'Bad String'
Must use try/except language. No conditionals allowed.

constraints 1<= len(S) <= 6
S is either lower case letters [a-z] or decimal digits [0-9]
"""

#!/bin/python3

import sys

S = input().strip()

try:
    int(S)
    print(S)
except ValueError:
    print('Bad String')
    
# TEST CASES:
# in '3' prints: '3' SUCCESS
# in 'za' prints: 'Bad String' SUCCESS
# in '3134' prints: '3134' SUCCESS
# in 'abc' prints: 'Bad String" SUCCESS