"""
Author: George Chorny
Assignment / Part: HW3 - Q5
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
numLayers = int(input('Please enter a positive integer'))
rowLength = (numLayers*2)-1
for i in range(numLayers, 0, -1):
    print((' '*(numLayers-i))+('*'*rowLength))
    rowLength -= 2
rowLength += 4
for i in range(2, numLayers+1):
    print((' ' * (numLayers - i)) + ('*' * rowLength))
    rowLength += 2
