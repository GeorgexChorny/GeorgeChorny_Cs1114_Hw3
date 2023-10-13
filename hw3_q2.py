"""
Author: George Chorny
Assignment / Part: HW3 - Q2
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
numberOfDays = int(input('Enter the number of days (1 to 100):'))
totalSteps = 0
adder = 0
while numberOfDays < 1 or numberOfDays > 100:
    numberOfDays = int(input('Enter a valid number:'))
for i in range(1, numberOfDays+1):
    totalSteps += (i + adder)
    adder += 1
print('The baby will have taken a total of',totalSteps,'steps after',numberOfDays,'days.')

