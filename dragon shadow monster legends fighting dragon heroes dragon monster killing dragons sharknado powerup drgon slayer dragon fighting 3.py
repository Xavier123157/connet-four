import random
import time

#asking for name because why not
def getname():
    name = input("enter name:")
    time.sleep(3)
    print(name + " is now playing: dragon shadow monster legends fighting dragon heroes dragon monster killing dragons sharknado powerup dragon slayer dragon fghting 3")

#printing some hype about the game
def gamerundown():
    #making 'rest' so i dont have to put int time sleep every time
    def rest():
        time.sleep(3)

    print("would you like a rundown of the game: dragon shadow monster legends fighting dragon heroes dragon monster killing dragons sharknado powerup dragon slayer dragon fghting 3?")
    rundown = input("enter [Y] for rundown   or   enter [N] to skip rundown")
    #ask for rundown or to skip
    if rundown == 'Y':
        print("you have selected to hear a rundown of the game: dragon shadow monster legends fighting dragon heroes dragon monster killing dragons sharknado powerup dragon slayer dragon fghting 3")
        rest
        print("dragon shadow monster legends fighting dragon heroes dragon monster killing dragons sharknado powerup dragon slayer dragon fghting 3 is an insane text based game!")
        rest
        print("you will be given a series of choices")
        rest
        print("the decisions you make will either kill you, or possibly you will survive long enough to die later")
        rest
        print("can you make it to the end?")
        rest
        print("or will you be brutally murdered along the way")
        rest
        print("you adventure in dragon shadow monster legends fighting dragon heroes dragon monster killing dragons sharknado powerup dragon slayer dragon fghting 3")
        rest
        print("lets get into playing dragon shadow monster legends fighting dragon heroes dragon monster killing dragons sharknado powerup dragon slayer dragon fghting 3")
    
    
    elif rundown == 'N': 
        print("you have selected to skip the rundown of: dragon shadow monster legends fighting dragon heroes dragon monster killing dragons sharknado powerup dragon slayer dragon fghting 3")
        time.sleep(3)
        print("you are free to continue")
    
    else:
        print("invalid choice, please try again")
        gamerundown()
        
#game begins and starts printing the intro
def printintro():
    print("Welcome to dragon shadow monster legends fighting dragon heroes dragon monster killing dragons sharknado powerup dragon slayer dragon fghting 3")
    time.sleep(3)
    input("ARE YOU READY TO EMBRACE THE PURE SHOCK AND AWE PROVIDED BY: dragon shadow monster legends fighting dragon heroes dragon monster killing dragons sharknado powerup dragon slayer dragon fghting 3?")
    time.sleep(3)
    gamerundown()
    #asking for rundown or not
    time.sleep(3)
    getname()
    time.sleep(3)
    print("you are now playing dragon shadow monster legends fighting dragon heroes dragon monster killing dragons sharknado powerup dragon slayer dragon fghting 3")
    time.sleep(3)
    print("You are walking through a deep dark forest")
    time.sleep(3)
    print("a fork in the track appears")
    time.sleep(3)
    print("you have two options....go right deeper into the forest.... or go left towards a weirdly coloured swamp")
    time.sleep(3)

#first choice
def playerchoice():
    choice = input ("which way will you go? [L] or [R] or toss a coin [C]")
   
    if choice == 'L':
        print("you selected left")
        leftA()
        #leads to first left answer
   
    elif choice == 'R':
        print("you slected right")
        rightA()
        #leads to first right answer
   
    elif choice == 'C': 
        print("you want to toss a coin, brave")
        cointoss()
   
    else: 
        print("you made an invalid choice, enter again")
        playerchoice
        #just in case they dont put in the right thing

#response if coin toss is chosen is always the same
def cointoss():
    time.sleep(2)
    print("you cant make a decision")
    time.sleep(2)
    print("is the pressure too overwhelming")
    time.sleep(2)
    print("either way, you die due to lack of brain power")
    time.sleep(2)
    end()
    input:("[enter] to end")
    gamecontinue = False
        
#comes from choice 1
def leftA():
    time.sleep(2)
    print("you went left towards the swamp")
    time.sleep(2)
    print("as you approach the swamp you see a massive crodile and you are eaten alive")
    time.sleep(2)
    print("death sucks, better luck next time")
    time.sleep(2)
    end()
    input("[enter] to end")
    gamecontinue = False
    #wrong choice so game ends
        
#comes from choice one
def rightA():
    time.sleep(2)
    print("you went right deeper into the forest")
    time.sleep(2)
    print("you approach a wild charlie, there is a chance he hasn't seen you, but you are unsure")
    time.sleep(2)
    print("you have two options, take a left and get the hell out of there.... or go right and try to take on the wild charlie")
    time.sleep(2)
    #second choice
    playerchoiceB()
    
#choosing right from option 1 leads to this (second choice)
def playerchoiceB():
    choice = input ("which way will you go? [L] or [R] or toss a coin [C]")
   
    if choice == 'L':
        print("you selected left")
        leftB()
        #leads to second left option
    
    elif choice == 'R':
        print("you slected right")
        rightB()
        #leads to second right option
   
    elif choice == 'C': 
        print("you want to toss a coin, brave")
        cointoss()
        #same cointoss ending always
    
    else: 
        print("you made an invalid choice, enter again")
        playerchoiceB
        #invalid choice response again

def leftB():
    time.sleep(2)
    print("you run and manage to escape the charlie")
    time.sleep(2)
    print("you approach some treasure, but there is one more choice first")
    time.sleep(2)
    print("in front of you is two doors")
    time.sleep(2)
    print("they are both identical")
    time.sleep(2)
    print("but through one lays treasure")
    time.sleep(2)
    print("and through the other certain death awaits")
    time.sleep(2)
    print("your choice will have to be random")
    time.sleep(2)
    print("which way will you go")
    time.sleep(2)
    playerchoiceC()
    #goes to third choice


def rightB():
    time.sleep(2)
    print("you move to attack the wild charlie")
    time.sleep(2)
    print("but it has seen you through and is anticipating your attack")
    time.sleep(2)
    print("it uses jujitsu to slaughter you")
    time.sleep(2)
    print("death sucks, better luck next time")
    time.sleep(2)
    end()
    input("[enter] to end")
    gamecontinue = False
    #death and end game

#random number for random door being correct
answer = random.randint(1,2)
#regardless of what the player enters win or die is randomly generated
def playerchoiceC():
    choice = input ("which way will you go? [L] or [R] or toss a coin [C]")
    
    if choice == 'L':
        print("you selected left") 
        #it tells you that you go through the left door but depending on the random number generated you have 50/50 chance of winning       
        
        if answer == 1:
            door1()
        elif answer == 2:
            door2()
        
    elif choice == 'R':
        print("you slected right")
        #tells you that the right door has been chosen but 50/50 chance of winning again
        if answer == 1:
            door1()
        elif answer == 2:
            door2()        

    elif choice == 'C': 
        print("you want to toss a coin, brave")
        cointoss()
        #still death by cointoss

    else: 
        print("you made an invalid choice, enter again")
        playerchoiceC()

        

def door1():
    time.sleep(2)
    print("the shadow monster dragon is waiting behind this door")
    time.sleep(2)
    print("death sucks, better luck next time")
    time.sleep(2)
    end()
    input("[enter] to end")
    gamecontinue = False
    #door1 ends in death

def door2():
    time.sleep(2)
    print("your treasure awaits")
    time.sleep(2)
    print("YOU WIN")
    time.sleep(2)
    end()
    input("[enter] to end")
    gamecontinue = False
    #door2 ends with a win

def end():
    print("GAME OVER")
    time.sleep(2)


gamecontinue = True

while gamecontinue == True:
    printintro()
    playerchoice()
    #after the first choice all of the def's lead on to each other
    gamecontinue = False




