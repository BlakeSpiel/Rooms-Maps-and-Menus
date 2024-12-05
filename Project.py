# INITALIZING THE TURTLE FOR USE LATER
import turtle
import random
import time

screen = turtle.Screen()
screen.title("Finding Bob")
screen.setup(width=810, height=700)

t = turtle.Turtle()
t2 = turtle.Turtle()
t.speed(0)
t2.speed(0)
t.hideturtle()
t2.hideturtle()

# WeaponNeeded, Enemy, Enemy Description, Attacking Description, Defend Description, Attacked Description, Fleeing Description (Success), Fleeing Description (Failure)
zombie_data = ["shovel",
               "Zombie",
               "A fierce looking zombie appears, with only one thing on its mind, you.",
               "With one fast motion of your Shovel, the zombie is no more",
               "The zombie attempts to hit you with a bat, and it hits itself and perishes.",
               "The zombie rushes you and starts viciously biting you",
               "The zombie shuffle is no match for your speed walk.",
               "The zombie covers your escape and attacks you.",
               "bat"]

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
                "Bob's true intentions come to light, "
                "Bob has been serial killer X-wing all along! \nThere is no room for error.",
                "With adrenaline rushing through your body, you use all your might to [WEAPON_ACTION] at Bob",
                "You take the backpack off your back and use it as a shield against Bob’s knife that will surely give you tetanus. Lucky enough, the knife gets stuck in the ball of lint in the backpack",
                "Your once friend uses his rusty knife to slash into your chest.",
                "The door slams shut behind you,"
                " there is no escaping.",
                "Your once friend uses his rusty knife to slash into your chest."]

movingSkull_data = ["crowbar",
                    "Moving Skull",
                    "Before your eyes, a moving skull, watching you and preparing to bite.",
                    "The skull shatters into pieces upon contact with your Crowbar.",
                    "The skull attempts to bite you and crumbles into bone fragments. They are extremely sharp.",
                    "You fail to defend yourself, and the skull sees its chance and takes a few painful bites out of you.",
                    "You simply walk away from the torso-less skull.",
                    "You failed to escape the skull in time before its attack and got bit.",
                    "bone fragments"]

finalBattle_data = ["You quickly gobble up the Blueberry Pie as Bob attempts to lunge at you.",
                    "Against your conscience, you lunge the firey spear at your best friend."
                    "\nQuick! Bob is on fire charging at you with his rusty knife!",
                    "Bob is struck with your Bat and falls to the ground"
                    "\nYou know what you must do…"
                    ]
# Different states of charactor
onward = 0  # For the cave. The number of times they've gone south. Once they hit two they leave.
gruCounter = 0  # If they wonder in the caves for over 7 moves, they get a little surprise :)
# inventory = ['Bare Hands', 'Skeleton Key', 'Blueberry Pie','Lighter', 'Spear', 'Bat', 'Revolver'] #This is all the things you can collect
inventory = ['Bare Hands']
enemy = False


def help():
    t2.write("""
    -----COMMANDS-----
Navigation: North, South, East, West, Up, Down
Combat: Attack, Run, Defend
Interaction: pickup (object name), Craft, Inventory """)


def huh():
    t2.write("I'm sorry, I didn't get that. If you need help with commands just type Help.")


# TURTLE FUNCTIONS FOR EVERY ROOMS MENU, MAP, AND DESRIPTION.
def cemetery():
    t.clear()  # Clearing the room and description on screen for this room

    def description():
        t.write("""
Here you are, in a cemetery. You find graves and a mausoleum to the west, all of which is enclosed by a picket fence. 
You are unable to see the end of the cemetery from where you are standing. Walking back toward the entrance the fog thins out 
As you venture into the cemetery the fog gets thicker, and you feel as if you are being watched. 
You see a small church towards the east of the cemetery through the thick fog. There are nothing but dead trees and graves around.
You notice a shovel along the wall of the small church.
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

    randomEncounter = random.randint(0, 4)
    if randomEncounter == 0:
        enemy_encounter(zombie_data)

    def menu():
        while True:
            menuInput = turtle.textinput("Input Command", "What is your action?").lower().strip()
            t2.clear()

            if 'south' in menuInput:
                t2.write("You enter the half collapsed church.")
                church()
            elif 'west' in menuInput and 'Skeleton Key' in inventory:
                t2.write("""
You twist the key into the lock and with little effort, you're able to push the doors open.
After walking in, a large gust of wind slams the door behind you.
""")
                mausoleum()
            elif 'west' in menuInput and 'Skeleton Key' not in inventory:
                t2.write("You attempt to open the doors but they won't budge. The key must be around here somewhere.")
            elif 'north' in menuInput or 'east' in menuInput:
                t2.write("""
The fog is too thick to see anything worth investigating, Grues might be lurking around in 
the deep fog too, so its best to keep in well lit areas.""")
                menu()
            elif "shovel" in menuInput and "pickup" in menuInput:
                if "shovel" not in inventory:
                    t2.write("A dull, rusty shovel is standing up against the wall of the church, this could be a useful tool on your adventure.")
                    inventory.append('shovel')
                else:
                    t2.write("The shovel is already in your inventory.")
            elif 'shovel' in inventory and "dig" in menuInput:
                if "revolver" not in inventory:
                    t2.write("""
                    You dig down and find a broken in casket with a skeleton and a revolver laying on top. 
                    There is only 1 bullet, and it is likely to jam.
                    """)
                    inventory.append('revolver')
                else:
                    t2.write("You dig into another grave just to find an empty casket.")
            elif 'inventory' in menuInput:
                t2.write(f"""
-----Inventory-----
{[item.lower() for item in inventory]}""")  # Display inventory in lowercase
            elif 'craft' in menuInput:
                craft_items()
            elif 'help' in menuInput:
                help()
            elif 'debug' in menuInput:
                inventory.append('Skeleton Key')
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
            \nYou smell a sweet scent coming from a room in the back of the church.
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
            menuInput = turtle.textinput("Input Command", "What is your action?").lower().strip()
            t2.clear()

            if 'north' in menuInput:
                t2.write("You walk back to the eery cemetery.")
                cemetery()
            elif 'blueberry pie' in inventory and ('east' in menuInput or 'west' in menuInput or 'south' in menuInput):
                t2.write("I wonder where that pie came from.")
            elif 'east' in menuInput or 'west' in menuInput or 'south' in menuInput:
                t2.write("You see a Blueberry Pie, freshly baked, it looks delicious but suspicious.")
            elif 'pie' in menuInput and 'pickup' in menuInput:
                if 'blueberry pie' not in inventory:
                    t2.write("You pick up the delicious Blueberry Pie")
                    inventory.append('blueberry pie')
                else:
                    t2.write("The Blueberry Pie is already in your inventory.")
            elif 'key' in menuInput and 'pickup' in menuInput:
                t2.write("You pick up the skeleton key.")
                inventory.append('Skeleton Key')
            elif 'inventory' in menuInput:
                t2.write(f"""
-----Inventory-----
{[item.lower() for item in inventory]}""")  # Display inventory in lowercase
            elif 'craft' in menuInput:
                craft_items()
            elif 'help' in menuInput:
                help()
                # Gives you all items
            else:
                huh()

    map()
    tWriting()
    description()
    menu()


def mausoleum():
    t.clear()

    def description():
        t.write(
            """
            The mausoleum. Shelves with earns and old caskets surround you. 
            Along the north wall is a flimsy ladder leading into darkness.
            There is a pile of dust in the corner.
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
        for i in range(3):
            t.right(90)
            t.forward(25)

    def menu():
        while True:
            menuInput = turtle.textinput("Input Command", "What is your action?").lower().strip()
            t2.clear()

            if 'down' in menuInput:
                catacombs()
            elif 'east' in menuInput:
                t2.write(
                    "You're stomache turns knots as your attempts to open the now locked door prove unsuccessfull.")
            elif 'north' in menuInput or 'east' in menuInput or 'west' in menuInput:
                t2.write(
                    "You have no urge to look any longer than you already have at the tombs to you're right and left.")
            elif "pickup" in menuInput and "dust" in menuInput:
                if 'lighter' not in inventory:
                    t2.write(
                        """
                        The pile of dust has something under it. It is a old, very used lighter.
                        The lighter used to belong to a man who was buried in the cemetery. 
                        Rumor has it he was buried with his revolver.
                        """)
                    inventory.append('lighter')
                else:
                    t2.write("The lighter is already in your inventory.")
            elif 'inventory' in menuInput:
                t2.write(f"""
-----Inventory-----
{[item.lower() for item in inventory]}""")  # Display inventory in lowercase
            elif 'craft' in menuInput:
                craft_items()
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


    def menu():  # I wanted to make it feel like you can get lost, but all you need to do is head south twice in a row. Going in any other direction just pretends like you're moving.
        global onward
        global gruCounter

        randomEncounter = random.randint(0, 4)


        while True:
            if randomEncounter == 0:
                enemy_encounter(movingSkull_data)

            while onward < 2 and gruCounter < 6:
                menuInput = turtle.textinput("Input Command", "What is your action?").lower().strip()
                t2.clear()
                if 'north' in menuInput and onward == 0:
                    mausoleum()
                elif 'north' in menuInput and onward > 0:
                    gruCounter += 1
                    "This isnt right. I'm horribly lost."
                elif 'south' in menuInput:
                    onward += 1
                    t2.write("It's very hard to tell if I've been here already.")
                    if onward < 2:
                        randomEncounter = random.randint(0, 4)
                elif 'east' in menuInput:
                    gruCounter += 1
                    t2.write("Have I been here? The walls all look the same.")
                    randomEncounter = random.randint(0, 4)
                elif 'west' in menuInput:
                    gruCounter += 1
                    t2.write("How do I get out of here.")
                    randomEncounter = random.randint(0, 4)
                elif 'inventory' in menuInput:
                    t2.write(f"""
    -----Inventory-----
    {[item.lower() for item in inventory]}""")  # Display inventory in lowercase
                elif 'craft' in menuInput:
                    craft_items()
                elif 'look' in menuInput:
                    description()
                elif 'help' in menuInput:
                    help()
                else:
                    huh()
            lair()

    map()
    tWriting()
    description()
    menu()
    # gruFight()


def lair():
    t.clear()

    def description():
        t.write(
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
            menuInput = turtle.textinput("Input Command", "What is your action?").lower().strip()
            t2.clear()

            if 'talk' in menuInput:
                bobFight()
            elif 'inventory' in menuInput:
                t2.write(f"""
-----Inventory-----
{[item.lower() for item in inventory]}""")  # Display inventory in lowercase
            elif 'craft' in menuInput:
                craft_items()
            elif 'help' in menuInput:
                t2.write("What is Bobby doing here? I should go talk to him.")
            else:
                t2.write("No time for that. I should go and talk with Bobby.")

    map()
    tWriting()
    description()
    menu()


# Places the cursor on the bottom for text
def tWriting():
    t.penup()
    t.goto(-450, -200)
    t.pendown()
    t.forward(850)
    t.penup()
    t.goto(-350, -200)
    t.pendown()


def tWrote():
    t2.penup()
    t2.goto(-350, -270)
    t2.pendown()
    t2.clear


tWrote()


def displayInventory(_data):
    # Display user's inventory
    loop = True
    while loop:
        t2.write(f"""
-----Inventory-----")
{[item.lower() for item in inventory]}
What item would you like to attack the {_data[1]} with? """)  # Display inventory in lowercase
        # Ask what item in the inventory to use
        itemUsed = turtle.textinput("Input Command", "What is your action?").lower().strip()
        t2.clear()
        # Check if the item exists in inventory
        if itemUsed not in [item.lower() for item in inventory]:
            t2.write("Please pick an item in your inventory (Case Insensitive)")
        elif itemUsed == _data[0].lower():
            t2.write(_data[3])
            break
        else:
            t2.write("write extra stuff")  # FIX THIS LATER
            userFlee(_data)
            break


def craft_items():
    """Allows the user to craft items."""
    global inventory
    t2.write("What two items would you like to craft together?")
    item1 = input("Enter the first item: ").strip().lower()
    item2 = input("Enter the second item: ").strip().lower()


def craft_items():
    """Allows the user to craft items."""
    global inventory
    t2.write("What two items would you like to craft together?")
    item1 = turtle.textinput("Input Command","Enter the first item: ").strip().lower()
    item2 = turtle.textinput("Input Command", "Enter the second item: ").strip().lower()

    # Check if both items are in the inventory
    if item1 in [item.lower() for item in inventory] and item2 in [item.lower() for item in inventory]:
        crafted = False  # Track whether an item was successfully crafted

        # Check specific crafting recipes
        if (item1 == "lighter" and item2 == "spear") or (item1 == "spear" and item2 == "lighter"):
            t2.write("You light the end of the spear and it engulfs in flames. You are a force to be reckoned with.")
            inventory.remove("Spear")
            inventory.remove("Lighter")
            inventory.append("Fiery Spear")
            crafted = True

        if (item1 == "bone fragments" and item2 == "stick") or (item1 == "stick" and item2 == "bone fragments"):
            t2.write(
                "You combine your stick and a fragment of the skull to craft a mighty spear, this will be a formidable weapon.")
            inventory.remove("Stick")
            inventory.remove("Bone Fragments")
            inventory.append("Spear")
            crafted = True

        if not crafted:
            t2.write("Those items cannot be crafted together.")
    else:
        t2.write("You don't have the necessary items to craft that.")


# enemy encounter, which is all based off the "zork clone data tables" document
def enemy_encounter(_data):
    global randomEncounter
    randomEncounter = 1
    alreadyDefend = False
    enemy = True
    t2.write(_data[2])  # Display enemy description
    # Loop for combat actions
    while enemy:
        t2.clear()
        t2.write(f"""
                    {_data[2]}
                    --------------------------------------------------------------
                    What would you like to do? (Attack, Run, or Defend): 
                    --------------------------------------------------------------""")
        answer = turtle.textinput("Input Command", "What is your action?").lower()
        t2.clear()

        if answer == "attack":
            displayInventory(_data)  # Display the player's inventory for attack selection
            t2.write(f"You defeated the {_data[1]}!")
            # Drop the item associated with the enemy
            if _data[8] not in inventory:
                inventory.append(_data[8])
                t2.write(f"The {_data[1]} dropped a {_data[8]}. It has been added to your inventory.")
            else:
                t2.write(f"The {_data[1]} dropped a {_data[8]}, but you already have one.")
            enemy = False
            break

        elif answer == "run":
            userFlee(_data)
            break

        # if player chooses to defend
        if answer == "defend":
            # ensures that if the player has already chosen defend they cannot do it again
            if alreadyDefend:
                t2.write(f"You have already defended yourself against the {_data[1]}. Pick another option.")
            else:
                alreadyDefend = True
                # 50% chance of successful defend
                defend = random.randint(0, 1)
                if defend == 0:
                    # if defend hits 0, there is a 1 in 4 chance of dying
                    death = random.randint(0, 4)
                    if death == 0:
                        t2.write(_data[5] + "\nYou have Died, Game Over.")
                        break
                    else:
                        # player gets injured, and another chance to attack or flee
                        t2.write(_data[5] + "\nYou are injured.")

                else:
                    t2.write(_data[4])
                    break


def userFlee(_data):
    t2.write("""
You attempt to flee.
                 """)
    # choose 0 or 1 at random, to give a 50% chance to successfully flee or not
    escape = random.randint(0, 1)
    if escape == 0:
        t2.write(_data[6])

    else:
        # flee failure, user dies
        t2.write(_data[7] + " You have Died, Game Over.")


def bobFight():
    alreadyDefend = False
    enemy = True
    evilBob = False
    action_sequence = ["blueberry pie", "fiery spear", "bat", "revolver"]
    current_step = 0

    t2.write("...")
    while enemy:
        # Display what the player can do
        t2.write(f"""
--------------------------------------------------------------
What would you like to do? (Attack, Run, or Defend): 
--------------------------------------------------------------

                 """)
        answer = turtle.textinput("Input Command", "What is your action?").lower()
        t2.clear()

        # If player chooses to attack
        if answer == "attack":
            t2.clear()
            if not evilBob:
                t2.write(bob_data[3])
            else:
                if current_step < len(action_sequence):
                    t2.write(f"""
-----Inventory-----
{[item.lower() for item in inventory]}
What item would you like to attack bob with?""")
                    item_used = turtle.textinput("Input Command", "What is your action?").lower
                    t2.clear()

                    if item_used == action_sequence[current_step]:
                        if not current_step == len(action_sequence) - 1:
                            t2.write(finalBattle_data[current_step])
                        current_step += 1
                        if current_step == len(action_sequence):
                            gameEnd()
                            enemy = False
                    else:
                        t2.write(evilBob_data[5] + " You have Died, Game Over.")
                        break
                else:
                    gameEnd()
                    enemy = False

        # If player chooses to flee, turns Bob into Evil Bob and the fight begins
        elif answer == "run":
            t2.clear()
            if not evilBob:
                t2.write(evilBob_data[2])  # Bob reveals himself as Evil Bob
                evilBob = True
            else:
                t2.write(evilBob_data[6])

        # If player chooses to defend
        elif answer == "defend":
            t2.clear()
            if not evilBob:
                t2.write(bob_data[4])  # Defending against Bob does nothing
            else:
                # ensures that if the player has already chosen defend they cannot do it again
                if alreadyDefend:
                    t2.write(
                        f"The backpack isn't enough this time. You feel the rusty knife fly into you.\nYou have Died, Game Over.")
                    break
                else:
                    alreadyDefend = True
                    t2.write(evilBob_data[4])  # Use the backpack as a shield against Evil Bob

        else:
            # If 1, 2, or 3 aren't chosen
            t2.write("Please choose a valid answer (1, 2, or 3).")


def gameEnd():
    for i in range(10):
        t2.write("                         ")
    t2.clear()
    t2.write(".")
    time.sleep(2)
    t2.clear()
    t2.write("..")
    time.sleep(1)
    t2.clear()
    t2.write("...")
    time.sleep(0.5)
    t2.clear()
    t2.write("....")
    time.sleep(0.25)
    t2.clear()
    t2.write(".....Bob is Dead")
    time.sleep(1)
    t2.clear()
    t2.write("You win, but at what cost")
    time.sleep(3)


# gameEnd()
# craft_items()
# enemy_encounter(zombie_data)
# bobFight()
cemetery()
# church()
# mausoleum()
# catacombs()
# lair()

# Keeps the turtle menu on the screen
# turtle.mainloop()
