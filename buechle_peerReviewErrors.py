# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
#	print('''You are in a land full of dragons. In front of you,
#	you see two caves. In one cave, the dragon is friendly
#	and will share his treasure with you. The other dragon
#	is greedy and hungry, and will eat you on sight.''')
	print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.\n''')
# removed indentation from multi-line print() formatting so it doesn't show up in program
#	print()
# replaced unnecessary print() call with \n in previous print() call


def chooseCave():
#    cave = ''
	cave = ''
# fixed indentation inconsistency
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

#	return caves
	return cave
# corrected spelling of cave variable in return statement

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
#	time.sleep(3)
	time.sleep(2)
# changed time.sleep() call argument to 2 to match preceding comment and for consistency
	print('A large dragon jumps out in front of you! He opens his jaws and...\n')
#	print()
# replaced unnecessary print() call with \n in previous print() call
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
#		print 'Gobbles you down in one bite!'
		print('Gobbles you down in one bite!')
# added required parenthesis to print function call

playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
# replaced assignment operators, = with comparison operators, ==
	displayIntro()
#	caveNumber = choosecave()
	caveNumber = chooseCave()
# corrected casing in chooseCave() function call
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
#	if playAgain == "no":
	if playAgain != 'yes' and playAgain != 'y':
# replaced check for "no" string with another check for 'yes' or 'y' as a catch-all
#		print("Thanks for planing")
		print("Thanks for playing")
# corrected spelling error in printed string
