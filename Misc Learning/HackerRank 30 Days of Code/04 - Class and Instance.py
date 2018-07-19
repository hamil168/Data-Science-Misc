# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:41:35 2018

@author: Ben

OOP: class vs instance
Implement a class Person
with an instance variable age
and an argument initialAge

- Check age is non-negative; if not, make a statement and set to 0
- Method yearPasses() increment age variable by 1
- Method amIOld() does a conditional check on age and returns strings
    - age < 13 print "You are young."
    - 13 <= age < 18 print "You are a teenager."
    - 18 <= age print "You are old."
    
    



"""



##################### MY CODE ################################

class Person:
    def __init__(self,initialAge):
        
        self.age = initialAge

        # Add some more code to run some checks on initialAge
        if self.age < 0:
            print('Age is not valid, setting age to 0.')
            self.age = 0

    def amIOld(self):        
        # Do some computations in here and print out the correct statement to the console
        textout = ""
                 
        if self.age < 13:
            textout = "You are young."
        elif self.age >= 13 and self.age < 18:
            textout = "You are a teenager."
        elif self.age >= 18:
            textout = "You are old."
        
        print(textout)
    
    def yearPasses(self):
        # Increment the age of the person in here
        self.age = self.age + 1

##################### HACKERRANK CODE ################################

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
    
#################### TEST CASES AND RESULT ################################
"""Case 0: initialAge = -1 prints "Age is not valid, setting age to 0." then 
"You are young." Three years passes and it prints "You are young."

Output:
Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.


"""
    
    
    