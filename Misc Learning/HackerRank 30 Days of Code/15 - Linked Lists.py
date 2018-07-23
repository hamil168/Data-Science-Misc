# -*- coding: utf-8 -*-
"""
HackerRank 30 days of Code 15 - LinkedLists

Created on Sun Jul 22 23:56:15 2018

@author: DRB4

Task: Complete insert function so it creates a new Node and inserts it
at the tail of the linked list referenced by the head parameter
Once new node is added, return the reference to the head node



"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
            
    def insert(self,head,data): 
        # This function inserts one node at a time on the
        # ...end of the existing function.
        # It is implemented as part of a for loop (see below)
        #####################################################

        # First time the function is called, head is None
        # New node containing data as the head ofthe list
        
        # Process:
        # head starts as None, the first value of data represents
        # the length of the following values, and is not needed for the
        # linked list. 

        # Begin hack
        # Event 0: assign head to a "blank" node
        if  head == None:
            head = Node(data)
        
        # Event 1: first Node becomes second data point
        #elif  head.data == placeholder:
            # hack way of getting at second element
            #head.data = data
        
        # Event 2: start at beginning of head
        # step through, checking to see if .next is NONE
        # if it is None, that's where you insert the next Node.
        else:
            current = head
            while current:
                if current.next == None:
                    current.next = Node(data)
                    break
                else:
                    current = current.next          
        
        # Event 3: return unmodified head
        # the Node additions will be included in the class properties
        return head
    
### HR CODE ###### 
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	 

# TEST CASES (first input value is length of input that follows)
# input 4 \n 2 \n 3 \n 4\n 1\n output [2 3 4 1]