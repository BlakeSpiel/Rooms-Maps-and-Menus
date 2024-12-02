#INITALIZING THE TURTLE FOR USE LATER
import turtle
import random
screen = turtle.Screen()
screen.title("Finding Bob")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# WeaponNeeded, Enemy, Enemy Description, Attacking Description, Defend Description, Attacked Description, Fleeing Description (Success), Fleeing Description (Failure)
zombie_data = ["Shovel",
               "Zombie",
               "A fierce looking zombie appears, with only one thing on its mind, you.",
               "With one fast motion of your Shovel, the zombie is no more",
               "The zombie attempts to hit you with a bat, and it hits itself and perishes.",
               "The zombie rushes you and starts viciously biting you",
               "The zombie shuffle is no match for your speed walk.",
               "The zombie covers your escape and attacks you."]

grue_data = ["N/A",
            "Grue",
            "The darkness makes you feel uneasy,"
            " something is watching from the shadows",
            "You [WEAPON_ACTION] but fail to hit anything in the dark",
            "Defending is useless! You curl into a ball and wait patiently for your death against the shadowed figure approaching.",
            "A fowl Grue appears before your eyes. You’ve died.",
            "N/A",
            "You hear the footsteps coming closer and closer. It’s a grue! You’ve died."]

bob_data = ["3",
            "Bob",
            "It's Bobby!",
            "Why would you attack your long-lost friend?",
            "Defend against what?",
            "N/A",
            "N/A",
            "(Bob turns into evil Bob)"]

evilBob_data = ["N/A",
                "Evil Bob",
                "Bob's true intentions come to light,"
                "Bob has been serial killer X-wing all along!",
                "With adrenaline rushing through your body, you use all your might to [WEAPON_ACTION] at Bob"
                "You take the backpack off your back and use it as a shield against Bob’s knife that will surely give you tetanus. Lucky enough, the knife gets stuck in the ball of lint in the backpack",
                "Your once friend uses his rusty knife to slash into your chest.",
                "N/A",
                "The door slams shut behind you,"
                " there is no escaping."]

movingSkull_data = ["Crowbar",
                    "Moving Skull",
                    "Before your eyes, a moving skull, watching you and preparing to bite.",
                    "The skull shatters into pieces upon contact with your Crowbar.",
                    "The skull attempts to bite you and crumbles into bone fragments. They are extremely sharp.",
                    "You fail to defend yourself, and the skull sees its chance and takes a few painful bites out of you.",
                    "You simply walk away from the torso-less skull.",
                    "You failed to escape the skull in time before its attack and got bit."]

#Different states of charactor
key = 0 #Turns into 1 if they have it
firstTimeMausoleum = True #Locks the door
onward = 0 #For the cave. The number of times they've gone south. Once they hit two they leave.
gruCounter = 0 #If they wonder in the caves for over 7 moves, they get a little supprise :)
inventory = []


def help():
    print("""
    -----COMMANDS-----
    Navigation: North, South, East, West, Up, Down
    Combat: Attack, Run, Defend
    Interaction: Look around, pickup (object name), 
    """)

def huh():
    print("I'm sorry, I didn't get that. If you need help with commands just type Help.")


#TURTLE FUNCTIONS FOR EVERY ROOMS MENU, MAP, AND DESRIPTION.
def cemetery():
    t.clear()
    def description():
        t.write("""
Here you are, in a cemetery. You find graves and a mausoleum to the west, all of which is enclosed by a picket fence. 
You are unable to see the end of the cemetery from where you are standing. Walking back toward the entrance the fog thins out 
As you venture into the cemetery the fog gets thicker, and you feel as if you are being watched. 
You see a small church towards the east of the cemetery through the thick fog. There are nothing but dead trees and graves around.
""")
        print("""
Here you are, in a cemetery. You find graves and a mausoleum to the west, all of which is enclosed by a picket fence. 
You are unable to see the end of the cemetery from where you are standing. Walking back toward the entrance the fog thins out 
As you venture into the cemetery the fog gets thicker, and you feel as if you are being watched. 
You see a small church towards the east of the cemetery through the thick fog. There are nothing but dead trees and graves around.
""")

    def map():
        t.penup()
        t.goto(-100, 200)
        t.pendown()
        for i in range(2):
            t.forward(200)
            t.right(90)
        for i in range(2):
            t.forward(75)
            t.penup()
            t.forward(50)
            t.pendown()
            t.forward(75)
            t.right(90)

    def menu():
        while True:
            menuInput = input().lower()

            if 'south' in menuInput:
                print("You enter the half collapsed church.")
                church()
            elif 'west' in menuInput and key == 1:
                print("You twist the key into the lock and with little effort, you're able to push the doors open.")
                mausoleum()
            elif 'west' in menuInput and key == 0:
                print("You attempt to open the doors but they won't budge. The key must be around here somewhere.")
            elif 'north' in menuInput or 'east' in menuInput:
                print("The fog is too thick to see anything worth investigating, Grues might be lurking around in the deep fog too, so its best to keep in well lit areas.")
                menu()
            elif 'look' in menuInput:
                description()
            elif 'help' in menuInput:
                help()
            else:
                huh()
    map()
    tWriting()
    description()
    menu()

def church():
    t.clear()
    def description():
        t.write(
"""
The door creaks as you enter the church, and the moon lights up the inside of the building 
through the cracks in the roof. It looks as if the building could fall apart at any moment.
""")
        print(
"""
The door creaks as you enter the church, and the moon lights up the inside of the building 
through the cracks in the roof. It looks as if the building could fall apart at any moment.
""")
    def map():
        t.penup()
        t.goto(0, 200)
        t.pendown()
        t.right(108)
        t.penup()
        for i in range(4):
            t.forward(70)
            t.right(72)
            t.pendown()
            t.forward(70)
            t.left(144)
        t.forward(70)
        t.right(180)

    def menu():
        while True:
            global key
            menuInput = input().lower()

            if 'north' in menuInput:
                print("You walk back to the eery cemetery.")
                cemetery()
            elif 'south' in menuInput or 'east' in menuInput or 'west' in menuInput:
                print("The only exit you can find is through the grand church door you just walked through.")
            elif 'key' in menuInput and 'pickup' in menuInput:
                print("You pick up the skeleton key.")
                key += 1
            elif 'look' in menuInput:
                description()
            elif 'help' in menuInput:
                help()
            else:
                huh()

    map()
    tWriting()
    description()
    menu()

def mausoleum():
    global firstTimeMausoleum
    t.clear()
    if firstTimeMausoleum == True:
        t.write(
"""
A large gust of wind slams the door behind you.

""")
        print(
"""
A large gust of wind slams the door behind you.

""")
        firstTimeMausoleum == False

    def description():
        t.write(
"""
You're now in the mausoleum. You see rows of shelving all holding old earns. Along the north wall is a flimsy ladder leading into darkness.
""")
        print(
"""
You're now in the mausoleum. You see rows of shelving all holding old earns. Along the north wall is a flimsy ladder leading into darkness.
""")
    def map():
        t.penup()
        t.goto(-50, 150)
        t.pendown()
        for i in range(2):
            t.forward(100)
            t.right(90)
            t.forward(140)
            t.right(90)
        t.penup()
        t.goto(-25, 125)
        t.pendown()
        t.forward(25)
        t.right(90)
        t.penup()
        t.forward(25)
        t.pendown()
        for i in range (3):
            t.right(90)
            t.forward(25)

    def menu():
        while True:
            menuInput = input().lower()

            if 'down' in menuInput:
                catacombs()
            elif 'east' in menuInput:
                print("You're stomache turns knots as your attempts to open the now locked door prove unsuccessfull.")
            elif 'north' in menuInput or 'east' in menuInput or 'west' in menuInput:
                print("You have no urge to look any longer than you already have at the tombs to you're right and left.")
            elif 'look' in menuInput:
                description()
            elif 'help' in menuInput:
                help()
            else:
                huh()

    map()
    tWriting()
    description()
    menu()

def catacombs():

    t.clear()
    def description():
        t.write(
"""
The vast hallway looks the exact same as the others. It would be very easy to get lost.”
""")
        print(
"""
The vast hallway looks the exact same as the others. It would be very easy to get lost.”
""")

    def map():
        t.penup()
        t.goto(-60, 120)
        t.pendown()
        for i in range(4):
            t.forward(40)
            t.penup()
            t.forward(40)
            t.pendown()
            t.forward(40)
            t.right(90)

    def menu(): #I wanted to make it feel like you can get lost, but all you need to do is head south twice in a row. Going in any other direction just pretends like you're moving.
        global onward
        global gruCounter
        while True:
            while onward < 2 and gruCounter < 6:
                menuInput = input().lower()
                if 'north' in menuInput and onward == 0:
                    mausoleum()
                elif 'north' in menuInput and onward > 0:
                    gruCounter += 1
                    "This isnt right. I'm horribly lost."
                elif 'south' in menuInput:
                    onward += 1
                    print("It's very hard to tell if I've been here already.")
                elif 'east' in menuInput:
                    gruCounter += 1
                    print("Have I been here? The walls all look the same.")
                elif 'west' in menuInput:
                    gruCounter += 1
                    print("How do I get out of here.")
                elif 'look' in menuInput:
                    description()
                elif 'help' in menuInput:
                    help()
                else:
                    huh()
            print("That looks different. This door must be my way out of here.")
            lair()

    map()
    tWriting()
    description()
    menu()
    #gruFight()

def lair():
    t.clear()
    def description():
        t.write(
"""
Against your gut, you open the door, and you enter a giant vast lair that is well lit with a man standing in the middle. "It’s Bobby!"
""")
        print(
"""
Against your gut, you open the door, and you enter a giant vast lair that is well lit with a man standing in the middle. "It’s Bobby!"
""")
    def map():
        t.penup()
        t.goto(-35, 00)
        t.pendown()
        for i in range(8):
            t.forward(70)
            t.left(45)
    
    def menu():
        while True:
            menuInput = input().lower()

            if 'talk' in menuInput:
                enemy_encounter(evilBob_data)
                #Win() Put a function here for after the fight
            elif 'north' in menuInput or 'south' in menuInput or 'east' in menuInput or 'west' in menuInput:
                print("What is Bobby doing here? I should go talk to him.")
            elif 'look' in menuInput:
                description()
            elif 'help' in menuInput:
                help()
            else:
                huh()

    map()
    tWriting()
    description()
    menu()

#Places the cursor on the bottom for text
def tWriting():
  t.penup()
  t.goto(-400, -200)
  t.pendown()

# enemy encounter, which is all based off the "zork clone data tables" document
def enemy_encounter(_data):
    alreadyDefend = False
    enemy = True
    print(_data[2])
    #loop
    while enemy:

        #display what the player can do
        print("---------")
        print("1. Attack")
        print("2. Run")
        print("3. Defend")

        #ask what the player wants to do
        answer = input("What would you like to do? (1, 2 or 3): ")
        print("---------")

        #if player chooses to attack
        if answer == "1":
            #display users inventory
            print("-----Inventory-----")
            print(inventory)
            #asking what item in the inventory to use
            itemUsed = input(f"What item would you like to attack the {_data[1]} with? ")
            #if item is correct, enemy is no more
            if itemUsed == _data[0]:
                print(_data[3])
                enemy = False
                break
            # if an item is not recognized by the game in the inventory
            elif itemUsed not in inventory:
                print("Please pick an item in your inventory (Case Sensitive)")
            # if item chosen is bad one, user has to flee
            else:
               userFlee(_data)
               enemy = False
                
        #if player chooses to flee
        if answer == "2":
            userFlee(_data)
            break
        
        #if player chooses to defend
        if answer == "3":
            # ensures that if the player has already chosen defend they cannot do it again
            if alreadyDefend:
                print(f"You have already defended yourself against the {_data[1]}. Pick another option.")
            else:
                alreadyDefend = True
                # 50% chance of successful defend
                defend = random.randint(0, 1)
                if defend == 0:
                # if defend hits 0, there is a 1 in 4 chance of dying
                    death = random.randint(0,4)
                    if death  == 0:
                        print(_data[5] + "\nYou have Died, Game Over.")
                        break
                    else:
                    # player gets injured, and another chance to attack or flee
                        print(_data[5] + "\nYou are injured.")

                else:
                    print(_data[4])
                    break

        else:
            #if 1 2 or 3 arent chosen
            print("Please choose a valid answer (1, 2 or 3): ")
    print("---------")

def userFlee(_data):
        print("You attempt to flee.")
        # choose 0 or 1 at random, to give a 50% chance to successfully flee or not
        escape = random.randint(0, 1)
        if escape == 0:
            print(_data[6])

        else:
            # flee failure, user dies
            print(_data[7] + " You have Died, Game Over.")


cemetery()
#church()
#mausoleum()
#catacombs()
#lair()

#Keeps the turtle menu on the screen
turtle.mainloop()
