import numpy as np

#Instead of Jupyter Notebook, this assignment is gonna be in python script, brace yourselves.

# Problem 1
"""Write a Python Program(with class concepts) to find the area of the triangle using the below formula. 
area = (s*(s-a)(s-b)(s-c)) ** 0.5 
Function to take the length of the sides of triangle from user should be defined in the parent class and 
function to calculate the area should be defined in subclass.
"""

class Triangle:
    def __init__(self):
        #this is a self constructor for Triangle Class
        self.TriangleSides = ['a', 'b', 'c']
    
    def sides_of_Triangle(self):
        #returns sides of triangle
        self.sides_of_Triangle = [input("Enter the side "+i+" :") for i in self.TriangleSides]
        print(self.sides_of_Triangle)
        
class Triangle_Area(Triangle):
    def __init__(self):
        #inheriting Triangle class
        Triangle.__init__(self)
    
    def area_of_triangle(self):
        #calc area of triangle
        triangleSides = iter(self.sides_of_Triangle)
        a = float(next(triangleSides))
        b = float(next(triangleSides))
        c = float(next(triangleSides))
        
        #half-perimeter of triangle
        s = (a+b+c)*0.5
        #Area of Triangle
        Area = (s*(s-a)*(s-b)*(s-c))*0.5
        print('The sides of triangle are a='+str(a)+', b='+str(b)+', c='+str(c))
        Area = ('The Area of the triangle is %0.2f' %Area)
        #return Area
        print(Area)

#creating object of sub calss Triangle Area                    
Area_of_Triangle = Triangle_Area()

#Ask User to Enter the sides of Triangle
Area_of_Triangle.sides_of_Triangle()

#Calculate the Area of Triangle
Area_of_Triangle.area_of_triangle()
#o/p: The sides of triangle are a=35.0, b=24.0, c=26.0
# The Area of the triangle is 48649.22

# Problem 2
"""Write a function filter_long_words() that takes a list of words 
 and an integer n and returns the list of words that are longer than n
"""
def filter_long_words(WordList, n):
    #returns list of words that are longer than Arguement n
    #n has been considered an integer
    WordList = [x.strip() for x in WordList if len(x.strip()) > n]
    
    if (len(WordList)>0):
        print("The list of words that are longer than "+str(n)+" is :")
        return WordList
    else:
        return "No words longer than specified number"
    
WordList_eg = list(input("Enter the list of words: ").split(','))
number = int(input("Enter your number :"))

#Function Calling
filter_long_words(WordList_eg, number)

"""Input:
Please enter your words: 'City', 'Charminar', 'India', 'Hyderabad', 'Eiffel Tower', 'Pari'
Please enter your number: 4

Output:
['Charminar', 'India', 'Hyderabad', 'Eiffel Tower']
"""

# Problem 3
"""Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words . 
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] Here 2,3 and 4 are the lengths of the words in the list.
"""
def words_to_length():
    list_words = list(input("Enter the list of words separated by comma :").split(','))
    list_obj = [i.strip() for i in list_words]
    return list(map(len, list_obj))

#calling function
words_to_length()
"""
i/p : ab,cde,erty,qwerty
o/p : [2, 3, 4, 6] 
"""

# Problem 4
"""
Write a Python function which takes a character (i.e. a string of length 1) 
and returns True if it is a vowel, False otherwise.
"""
def check_vowel():
    l = input("Enter your character :")
    print(l)
    if len(l)==1:
        vowels = ['a','e','i','o','u']
        if l.lower() in vowels:
            return True
        else:
            return False
    else:
        return "Enter single charecter to evaluate the if it is vowel or not"
#Function execution
check_vowel()

"""
i/p: q
o/p: False
"""