# -*- coding: utf-8 -*-
"""

Solution to HackerRank 30 days of Code
Day 18: Queues and Stacks

Problem: Given a string s, implement a class that 
uses a queue and a stack to detect if s is a palindrome.

Created on Mon Jul 16 11:09:52 2018

@author: DRB4
"""
################ HACKERRANK CODE  (locked) #################
import sys

################ MY SOLUTION #################

class Solution:
    # Fill a stack and a queue the same way at the same time
    # Remove the elements from the stack and queue 1 at a time and compare
    # stacks use FILO and queues use FIFO
    # the string s will be a palindrome if the FILO and FIFO outputs match for
    # every letter in the string
    
        def __init__(self):
                
                # implement both structures as empty lists
                self.stack = []
                self.queue = []
        
        # Stack adds to the end of the list
        def pushCharacter(self, char):
                self.stack.append(char)
                
        # Pop (default or index -1) removes from the end of the list
        # return the pop'd character for comparison to Queue
        def popCharacter(self):
                return self.stack.pop(-1)
                
        # queue.append adds to the end of the list                
        def enqueueCharacter(self, char):
                self.queue.append(char)
                
        # queue.pop(0) removes from the beginning of the list                
        # return the pop'd character for comparison to Stack
        def dequeueCharacter(self):
                return self.queue.pop(0)
        
        pass

################ HACKERRANK CODE (locked) #################
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.") 
    
###########?######### RESULT ###################
#  input(stdin) = 'racecar'
#  output = 'The word, racecar, is a palindrome'
#  compiler message = 'Success'
#
#  input(stdin) = 'yes'
#  output = 'The word, yes, is not a palindrome'
#  compiler message = 'Success'