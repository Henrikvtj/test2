''' Rock, Paper, scissors
        By:
            Henrik von Tangen-Jordan
                                    '''

import random

import time


def restart(): #Start of the game / restart sequence
    print (" ")
    print (" ")
    print (" ")
    print ("Welcome to a game of ROCK, PAPER, SCISSORS")
    finish = (input("Press S to restart or ENTER to end the game: "))
    if finish == 's':
        steinsakspapir()
    elif finish == '':
       exit()
    else:
        print ("Err0r, please redo")
        restart()
        
def steinsakspapir(): #The main game sequence

    aipoints = 0 #How many points the AI has

    playerpoints = 0# How many points the Player has

    for i in range(7):
        round = i + 1
        print (" ")
        print (" ")
        print ("Round nr." , round)
        svarliste = ["ROCK", "PAPER", "SCISSORS"]
        aisvar = random.choice(svarliste)
        svar = input("Press 5 to choose Rock, press 6 to choose paper, or press 7 to choose scissors: ")
        print (" ")
        print (" ")
        print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print (" ")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- AI chooses rock

        if aisvar == 'ROCK' and svar == '7':
            aipoints = aipoints + 1
            print ("The AI wins")

        elif aisvar == 'ROCK' and svar == '6':
            playerpoints = playerpoints + 1
            print ("The Player wins")
        elif aisvar == 'ROCK' and svar == '5':
            print ("It's a Draw!")
            
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- AI chooses paper

        elif aisvar == 'PAPER' and svar == '5':
            print ("The AI wins")
            aipoints = aipoints + 1

        elif aisvar == 'PAPER' and svar == '7':   
            print ("The Player wins")
            playerpoints = playerpoints + 1

        elif aisvar == 'PAPER' and svar == '6':
            print ("It's a Draw!")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- AI chooses scissors

        elif aisvar == 'SCISSORS' and svar == '6':
            print ("The AI wins")
            aipoints = aipoints + 1

        elif aisvar == 'SCISSORS' and svar == '5':
            print ("The Player wins")
            playerpoints = playerpoints + 1

        elif aisvar == 'SCISSORS' and svar == '7':
            print ("It's a Draw!")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- No valid answer is entred
        elif svar == '':
            quit
        else:
            print ("Err0r, please redo")

       
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Scoreboard       

        print ("The AI´s points =" , aipoints)
        print ("The Player's points =" , playerpoints)
        print (" ")
        if svar == '5':
            print ("The Player choose ROCK")
        elif svar == '6':
            print ("The Player choose PAPER")
        elif svar == '7':
            print ("The Player choose SCISSORS")
        print (" ")
        print ("The AI choose" , aisvar)
        print (" ")
        print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print (" ")
        time.sleep(4)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Declaring a Victor

    print (" ")
    print (" ")
    print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print (" ")
    print (" ")

    if aipoints > playerpoints:
        print ("The AI WINS THE GAME!!!!")
        print (" ")
        print ("The AI got" , aipoints ,"points!")
        print ("The Player got" , playerpoints , "points!")

    elif aipoints < playerpoints:
        print ("The Player WINS THE GAME!!")
        print ("The AI got" , aipoints ,"points!")
        print ("The Player got" , playerpoints , "points!")

    elif aipoints == playerpoints:
        print ("The game is a DRAW")
        print ("The AI got" , aipoints ,"points!")
        print ("The Player got" , playerpoints , "points!")
    restart()
            
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Start of the game!            
restart()

    