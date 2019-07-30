import os
import Stats
import Game
import Check
import Monsters.Small.Snail

#these classes are to simplify the call to the imported files sections
class rn:
    fights = Stats.Game.fightswon
    check = Check.start
    smail = Monsters.Small.Snail

validanswer = False

#startup script - run!

os.system('cls' if os.name == 'nt' else 'clear')

while(validanswer != True):
    print ("Welcome to the crypt!\nWill you survive longer then the man before you.\nHe was able to survive",rn.fights, "battles before falling\n" +
    "Will you take on the challenge?")

    menu = input ("what will you do? \n")
    
    if menu == "start":
        rn.smail.slither()
    elif menu == "exit":
        print("We shall meet again adventurer \nFarewell!")
        quit()
    elif menu == "stats":
        rn.check()     
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Hmmm. Lets try again...")
        validanswer = True
        






