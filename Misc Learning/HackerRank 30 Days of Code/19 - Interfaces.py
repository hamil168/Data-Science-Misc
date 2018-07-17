# -*- coding: utf-8 -*-
"""

Solution to HackerRank 30 days of Code
Day 19: Interafces

The AdvancedArithmetic interface and the method declaration for the abstract 
divisorSum(n) method are provided for you in the editor below.

Complete the implementation of Calculator class, which implements the 
AdvancedArithmetic interface. The implementation for the divisorSum(n) method 
must return the sum of all divisors of n.

Input: single integer n

Constraints 1 <= n <= 100

Created on Mon Jul 16 11:09:52 2018

@author: DRB4
"""
################ HACKERRANK CODE  (locked) #################
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

################ MY SOLUTION #################

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        
        # check n
        # print(n)

        # create a list of all numbers that could be divisors of n
        # only need to go up to n/2
        # shift end by +1 to account for exclusivity
        # then append n to the list since it can divide itself.
        check_nums = list(range(1,int(n/2)+1))
        check_nums.append(n)
        
        # check the tail of the list
        # print(check_nums[-1])
        
        # create the divisor list using list comprehension and modulo math
        # could have also filter() the check_nums with a lambda function
        divisor_list = [num for num in check_nums if n % num == 0]
        
        # check the divisor list
        #print (divisor_list)
        
        # the goal is to give the sum of divisors
        return sum(divisor_list)
              
        pass

################ HACKERRANK CODE (locked) #################
n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

    
###########?######### RESULT ###################
#  input(stdin) = 6
#  output = 'I implemented: AdvancedArithmetic' \n 12
#  compiler message = 'Success'
#
#  input(stdin) = 1
#  output = 'I implemented: AdvancedArithmetic' \n 1
#  compiler message = 'Success'
#
#  input(stdin) = 20
#  output = 'I implemented: AdvancedArithmetic' \n 42
#  compiler message = 'Success'