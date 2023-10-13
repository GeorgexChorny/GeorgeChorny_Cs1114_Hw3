"""
Author: George Chorny
Assignment / Part: HW3 - Q1
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
print('Welcome to the Lemonade Stand Profit Calculator')
season = input('Enter the current season (summer/other):')
smallCupsSold = int(input('Enter the number of small cups of lemonade sold'))
mediumCupsSold = int(input('Enter the number of small cups of lemonade sold'))
largeCupsSold = int(input('Enter the number of small cups of lemonade sold'))
if season == 'summer':
    totalProfit = (smallCupsSold * (2 - 1)) + (mediumCupsSold * (2.5 - 1.25)) + (largeCupsSold * (3 - 1.5))
else:
    totalProfit = (smallCupsSold * (1.5 - .75)) + (mediumCupsSold * (2 - 1)) + (largeCupsSold * (2.5 - 1.25))
print('Total profit for the day in the summer: $' +str(totalProfit))
