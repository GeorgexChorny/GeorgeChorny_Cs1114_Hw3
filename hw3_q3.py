"""
Author: George Chorny
Assignment / Part: HW3 - Q3
Date due: October 13, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import random

toPlay = input('Would you like to Play \'Twenty-one\'? [y/n]')
if toPlay == 'y':
    totalOpponentScore = random.randint(1, 100)
    while totalOpponentScore < 3 or totalOpponentScore > 33:
        totalOpponentScore = random.randint(1, 100)
    playerCard1 = random.randint(1,11)
    playerCard2 = random.randint(1,11)
    totalPlayerScore = playerCard1 + playerCard2
    print('Your cards are worth', playerCard1,'and', playerCard2)
    anotherRound = input('Would you like another card? [y/n]')
    while anotherRound != 'y' and anotherRound != 'n':
        anotherRound = input('Would you like another card? [y/n]')
    if anotherRound == 'y':
        totalPlayerScore += random.randint(1,11)
    print('Your score is', str(totalPlayerScore)+'!')
    print('Your opponents score is',str(totalOpponentScore)+'!')
    if totalPlayerScore == 21 and totalOpponentScore != 21:
        print('You got a perfect 21 score! You win!')
    elif totalOpponentScore == 21 and totalPlayerScore != 21:
        print('Your opponent got a perfect 21 score! They win!')
    elif abs(21 - totalPlayerScore) < abs(21 - totalOpponentScore):
        print('You win! Your score was', str(totalPlayerScore)+'.')
    elif abs(21 - totalPlayerScore) > abs(21 - totalOpponentScore):
        print('Your opponent wins! Their score was', str(totalOpponentScore) + '.')
    elif abs(21 - totalPlayerScore) == abs(21 - totalOpponentScore):
        print('Its a draw!')

else:
    print('Thank you for playing!')