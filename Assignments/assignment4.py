import numpy as np

#Instead of JupyterNotebook, this assignment is gonna be in python script, brace yourselves.

#Write a Python Program(with class concepts) to find the area of the triangle using the below formula. 
# area = (s*(s-a)(s-b)(s-c)) ** 0.5 
# Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass.

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

