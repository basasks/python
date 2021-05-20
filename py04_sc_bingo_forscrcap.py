#################################################################################
# TITLE:            Let's Play BINGO                                            #
# AUTHOR:           BASASKS                                                     #
# PYTHON VERSION:   Python 3.5.9                                                #
# USAGE:            python3 py04_sc_bingo.py                                    #
# NOTES:            Input: # of players, # of cards per player                  #
#################################################################################

import random
import time
import os

ctr = 0
listcardids = []
listdrawnnums = []
listnames = []
dictallcards = {}
dictallcardscopy = {}
listrand = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def checkinputint(prompt):
    while True:
        try:
            z = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that. Please enter value from 1 to 99.")
            continue
        if (z < 1) or (z > 99):
            print("Sorry, I didn't understand that. Please enter value from 1 to 99.")
            continue
        else:
            break
    return z

def checkinputname(prompt):
    while True:
        try:
            name = str(input(prompt).strip()) 
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if name in listnames:
            print("Sorry, that name is already taken. Please enter another name.")
            continue
        else:
            listnames.append(name)
            break
    return name    

def setuplist():
    global listcardids
    global listnames
    listnames = []
    os.system("clear")
    print("\n*****   LET'S PLAY BINGO!   *****")
    time.sleep(1)
    nplayers = checkinputint('\nHow many players would play? ')
    for i in range(0, nplayers):
        name = checkinputname('\nName of player? ')
        cards = checkinputint('Number of cards? ')
        pcardnum = 901
        for j in range(0, int(cards)):
            cardid = name + str(pcardnum)
            j += 1
            listcardids.append(cardid)
            pcardnum += 1
        i += 1

def drawinitrandom(nmin, nmax, col, row):
    global drawnnum
    drawnnum = random.randint(nmin, nmax)
    if drawnnum not in listrand[col]:
        listrand[col][row] = drawnnum
    else:
        drawinitrandom(nmin, nmax, col, row)

def buildcard():
    for col in range(5):
        for row in range(5):
            if col == 0: nmin = 1; nmax = 15
            elif col == 1: nmin = 16; nmax = 30
            elif col == 2: nmin = 31; nmax = 45
            elif col == 3: nmin = 46; nmax = 60
            else: nmin = 61; nmax = 75
            drawinitrandom(nmin, nmax, col, row)
    return listrand

def printcard(ncardid, cardid):
    print( "\nPlayer: " + ncardid[0:(len(ncardid)-3)] + ", Card Number: " +  str(int(ncardid[-3:])-900) )
    for val in range(5):
        col1 = "xx" if str(cardid[0][val]).zfill(2) == "00" else str(cardid[0][val]).zfill(2)
        col2 = "xx" if str(cardid[1][val]).zfill(2) == "00" else str(cardid[0][val]).zfill(2)
        col3 = "xx" if str(cardid[2][val]).zfill(2) == "00" else str(cardid[0][val]).zfill(2)
        col4 = "xx" if str(cardid[3][val]).zfill(2) == "00" else str(cardid[0][val]).zfill(2)
        col5 = "xx" if str(cardid[4][val]).zfill(2) == "00" else str(cardid[0][val]).zfill(2)
        print( col1 + "\t" + col2 + "\t" + col3 + "\t" + col4 + "\t" + col5 )

def drawrandom():
    global drawnnum
    drawnnum = random.randint(1,75)
    if drawnnum not in listdrawnnums:
        listdrawnnums.append(drawnnum)
    else:
        drawrandom()
    return listdrawnnums
    
def checkpattern():   
    lswinners = []
    for key in dictallcards:
        lsck = []
        ck = dictallcards[key]
        lsck.append( ck[0][0] + ck[0][1] + ck[0][2] + ck[0][3] + ck[0][4] )
        lsck.append( ck[1][0] + ck[1][1] + ck[1][2] + ck[1][3] + ck[1][4] )
        lsck.append( ck[2][0] + ck[2][1] + ck[2][2] + ck[2][3] + ck[2][4] )
        lsck.append( ck[3][0] + ck[3][1] + ck[3][2] + ck[3][3] + ck[3][4] )
        lsck.append( ck[4][0] + ck[4][1] + ck[4][2] + ck[4][3] + ck[4][4] )
        lsck.append( ck[0][0] + ck[1][0] + ck[2][0] + ck[3][0] + ck[4][0] )
        lsck.append( ck[0][1] + ck[1][1] + ck[2][1] + ck[3][1] + ck[4][1] )
        lsck.append( ck[0][2] + ck[1][2] + ck[2][2] + ck[3][2] + ck[4][2] )
        lsck.append( ck[0][3] + ck[1][3] + ck[2][3] + ck[3][3] + ck[4][3] )
        lsck.append( ck[0][4] + ck[1][4] + ck[2][4] + ck[3][4] + ck[4][4] )
        lsck.append( ck[0][0] + ck[1][1] + ck[2][2] + ck[3][3] + ck[4][4] )
        lsck.append( ck[4][0] + ck[3][1] + ck[2][2] + ck[1][3] + ck[0][4] )
        if 0 in lsck:
            lswinners.append(key)
    return lswinners

def maindraw():

    global ctr
    ctr += 1
    # Draw one number
    listdrawnnums = drawrandom()
    currentdraw = listdrawnnums[-1]   
    os.system("clear")
    print("\n*****   CURRENT DRAW: " + str(currentdraw) + "   *****")
    
    # Mark all player cards
    for key in dictallcards:
        ls = dictallcards[key]
        for col in range(5):
            for row in range(5):
                if ls[col][row] == currentdraw:
                    ls[col][row] = 0
        ncardid = key
        printcard(ncardid, dictallcards[key])
        #print(key + " = " + str(dictallcards[key]))
        
    # Check pattern if exists
    lswinners = checkpattern()
    time.sleep(2)
    if len(lswinners) > 0 :
        os.system("clear")
        print("\n*****   BINGO! BINGO! BINGO! BINGO! BINGO!   *****\n")
        for y in range(len(lswinners)):
            print("Player " + str(lswinners[y])[0:(len(str(lswinners[y]))-3)] + " for Card Number " + str(int(str(lswinners[y])[-3:])-900))
        print("(Total number of draws: " + str(ctr) + ")")
        print ("\n*****   HAVE A GREAT DAY!   *****\n")
    else:
        maindraw()


# MAIN PROGRAM FLOW

# Create list of all player cards
setuplist()

# Build dictionary of player-card
os.system("clear")
print("\n*****   INITIAL CARDS   *****")
for cardid in listcardids:
    listrand = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    listrand = buildcard()
    dictallcards.update({cardid : listrand})
    ncardid = cardid
    printcard(ncardid, dictallcards[cardid])
dictallcardscopy = dictallcards
time.sleep(3)

# Main Draw
maindraw()

