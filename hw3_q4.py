"""
Author: George Chorny
Assignment / Part: HW3 - Q4
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import math
a = float(input("Please enter value of a:"))
b = float(input("Please enter value of b:"))
c = float(input("Please enter value of c:"))
discriminant = b**2 - (4*a*c)
if discriminant < 0:
    print('The equation has no real solutions')
elif a == 0 and b == 0 and c ==0:
    print('The equation has infinite solutions')
elif a == 0 and b == 0:
    print('The equation has no solution')
elif discriminant == 0:
    print('The equation has 1 solution:', (-1*b)/(2*a))
else:
    if a == 0:
        print('Your equation has 1 solution:', (-c/b))
    else:
        print('The equation has two solutions: x =', ((-1*b)+math.sqrt(discriminant))/(2*a), 'and x = ', ((-1*b)-math.sqrt(discriminant))/(2*a))