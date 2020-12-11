"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""

def DivideByZero(x,y):
    #tries to divide 2 integers
    #returns an expection if divided by 0
    try:
        x/y
    except ZeroDivisionError:
        print("Integer cannot be divisible by 0")
 
 #Executing the function
 DivideByZero(5,0)
 
 """Integer cannot be divisible by 0"""
        

 # Problem 2
 """
 Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].

        Hint: Subject,Verb and Object should be declared in the program as shown below.                
        subjects=["Americans ","Indians"]
        verbs=["play","watch"]
        objects=["Baseball","Cricket"]

Exptected Output  :                       
                   Americans play Baseball.
                   Americans play Cricket.
                   Americans watch Baseball.
                   Americans watch Cricket.
                   Indians play Baseball.
                   Indians play Cricket.
                   Indians watch Baseball.
                   Indians watch Cricket.
 """       

def sentence_gram():
    subject=["Americans","Indians"]
    verb=["play","watch"]
    objects=["Baseball","Cricket"]
    
    sentences = [(sub+' '+vrb+' '+'obj'+'.') for sub in subject for vrb in verb for obj in objects]
    
    print("Output :")
    for i in sentences:
        print(i)
        
#Function execution
sentence_gram()

"""
Output :
Americans play obj.
Americans play obj.
Americans watch obj.
Americans watch obj.
Indians play obj.
Indians play obj.
Indians watch obj.
Indians watch obj.
"""