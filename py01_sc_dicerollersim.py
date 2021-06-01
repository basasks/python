#############################################################
# TITLE:            Dice Rolling Simulator                  #
# AUTHOR:           BASASKS                                 #
# PYTHON VERSION:   Python 3.5.2                            #
# USAGE:            python3 py01_sc_dicerollersim.py        #
# NOTES:                                                    #
#############################################################


#####   MODULES

import random


#####   FUNCTIONS

def checkinput():
    global rollagain
    if rollagain == 'yes': 
        rolldice()
    elif rollagain == 'no':
        print('\nGoodbye!')
    else:
        rollagain = input('\nPlease enter yes or no. Would you like to roll again?\n')
        checkinput()

def rolldice():
    global rollagain
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print('\nYou rolled: ', d1, 'and', d2)
    rollagain = input('Would you like to roll again?\n')
    checkinput()


#####   MAIN CODE

print('\nWelcome to the Dice Rolling Simulator!')
rolldice()
