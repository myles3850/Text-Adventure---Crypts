#this program is purely for checkingt stats and can be used anywhere in the game
import os
import Stats
import Game

# clasifications to simplyfy code needed in the program
human = Stats.Player
mules = Stats.Mule
game = Stats.Game



def start():

    loopcheck = False

    while loopcheck != True:

        if Game.started == True:

            print("Who would you like to check?")
            print("'player'   or  'mule'?")
            who = input()

            if who == "player":
                loopcheck = True
                player()

            elif who == "mule":
                loopcheck = True
                mule() 

            else:
                print("im not sure what that is. Lets try again!")
        else:
            player()

def player():

    loopcheck = False

    while loopcheck != True:

        print("What would you like to check?\n'Health'? 'Armour'? or are you 'finished'?")
        what = input()

        if what == "health":
            os.system('cls' if os.name == 'nt' else 'clear')
            human.health()

        elif what == "armour":
            os.system('cls' if os.name == 'nt' else 'clear')
            human.armour()

        elif what == "finished":
            print("In that case let us start again!")
            loopcheck = True 

        else:
            print("im not sure what that is. Let me ask again")

def mule():

    loopcheck = False

    print("What would you like to check?\n'Health'? 'Armour'? or are you 'finished'?")
    what = input()

    while loopcheck != True:

        if what == "health":
            os.system('cls' if os.name == 'nt' else 'clear')
            mules.health()

        elif what == "armour":
            os.system('cls' if os.name == 'nt' else 'clear')
            mules.armour()

        elif what == "finished":
            print("In that case let us start again!")
            loopcheck = True   

        else:
            print("im not sure what that is. Let me ask again")
