#INITALIZING THE TURTLE FOR USE LATER
import turtle
screen = turtle.Screen()
screen.title("Finding Bob")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(1)
t.hideturtle()

#Different states of charactor
key = 0 #Turns into 1 if they have it
firstTimeMausoleum = True
onward = 0 #For the cave. The number of times they've gone south. Once they hit two they leave.
gruCounter = 0 #If they wonder in the caves for over 7 moves, they get a little supprise :)


#TURTLE FUNCTIONS FOR EVERY ROOMS MENU, MAP, AND DESRIPTION.
def cemetery():
    t.clear()
    def description():
        t.write("""
        In the cemetery, you come across graves, and a mausoleum to the west. The cemetery is enclosed with a picket fence. 
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
        menuInput = input().lower()

        if 'south' in menuInput:
            print("You enter the half collapsed church.")
            church()
        elif 'west' in menuInput and key == 1:
            print("You twist the into the lock and with little effort, you're able to push the doors open.")
            mausoleum()
        elif 'west' in menuInput and key == 0:
            print("You attempt to open the doors but they won't budge. The key must be around here somewhere.")
            menu()
        elif 'north' in menuInput or 'east' in menuInput:
            print("The fog is too thick to see anything worth investigating, Grues might be lurking around in the deep fog too, so its best to keep in well lit areas.")
            menu()
        else:
            print("I don't understand. Try: North, South, East, West.")
            menu()

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
        global key
        menuInput = input().lower()

        if 'north' in menuInput:
            print("You walk back to the eery cemetery.")
            cemetery()
        elif 'south' in menuInput or 'east' in menuInput or 'west' in menuInput:
            print("The only exit you can find is through the grand church door you just walked through.")
            menu()
        elif 'key' in menuInput:
            print("You pick up the skeleton key.")
            key += 1
            menu()
        else:
            print("I don't understand. Try: North, South, East, West.")
            menu()

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
            A large gust of wind and slams the door behind you.

            """)
        firstTimeMausoleum == False

    def description():
        t.write(
            """
            You're now in the mausoleum. You see a rows of shelving next next along with a flimsy ladder that leads into darkness.
            """)
    def map():
        t.penup()
        t.goto(-50, 150)
        t.pendown()
        for i in range(2):
            t.forward(100)
            t.right(90)
            t.forward(50)
            t.penup()
            t.forward(40)
            t.pendown()
            t.forward(50)
            t.right(90)

    def menu():
        menuInput = input().lower()

        if 'down' in menuInput:
            catacombs()
        elif 'east' in menuInput:
            print("You're stomache turns knots as your attempts to open the now locked door prove unsuccessfull.")
            menu()
        elif 'north' in menuInput or 'east' in menuInput or 'west' in menuInput:
            print("You have no urge to look any longer than you already have at the tombs to you're right and left.")
            menu()
        else:
            print("I don't understand. Try: North, South, East, West")
            menu()

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

    def menu(): #I wanted to make it feel like you can get lost, but all you need to do is head south twice in a row. Going in any other direction just pretends like you're moving.
        global onward
        global gruCounter
        menuInput = input().lower()

        while onward < 2 and gruCounter < 6:
            if 'north' in menuInput and onward == 0:
                mausoleum()
            elif 'north' in menuInput and onward > 0:
                gruCounter += 1
                "This isnt right. I'm horribly lost."
                menu()
            elif 'south' in menuInput:
                onward += 1
                print("It's very hard to tell if I've been here already.")
                menu()
            elif 'east' in menuInput:
                gruCounter += 1
                print("Have I been here? The walls all look the same.")
                menu()
            elif 'west' in menuInput:
                gruCounter += 1
                print("How do I get out of here.")
                menu()
            else:
                print("I don't understand. Try: North, South, East, West")
                menu()
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
    def map():
        t.penup()
        t.goto(-35, 00)
        t.pendown()
        for i in range(8):
            t.forward(70)
            t.left(45)
    
    def menu():
        menuInput = input().lower()

        if 'talk' in menuInput:
            print("Dialog")
            #BobbyFight()
        elif 'north' in menuInput or 'south' in menuInput or 'east' in menuInput or 'west' in menuInput:
            print("What is Bobby doing here? I should go talk to him.")
            menu()
        else:
            print("I don't understand.")
            menu()

    map()
    tWriting()
    description()
    menu()

#Places the cursor on the bottom for text
def tWriting():
  t.penup()
  t.goto(-400, -200)
  t.pendown()

# enemy encounter, not even close to done
enemy_name = "Zombie"
enemy_health = 10

user_health = 25

def enemy_encounter():
    print("A fierce-looking zombie appears, with only one thing on it's mind, you.")

    #loop
    while monster_health > 0 and user_health > 0:
        print(f"The {enemy_name} has {enemy_health} health.")
        print(f"You have {user_health} health.")

        #display what the player can do
        print("---------")
        print("1. Attack")
        print("2. Run")
        print("3. Defend")

        #ask what the player wants to do
        answer = int(input("What would you like to do? (1, 2 or 3) "))

        #if player chooses to attack
        if answer == "1":
            #display users inventory

            #asking what item in the inventory to use
            itemUsed = int(input("What item would you like to attack the {enemy_name} with?"))

            #if item is correct, enemy is no more?
    
            #if item chosen is bad one, user has to flee
            userFlee()
        
        #if player chooses to flee
        if answer == "2":
            userFlee()
        
        #if player chooses to defend
        if answer == "3":
            escape = random.randint(0, 1)
            if escape == 0:
                death = random.randint(0,4)
                if death  == 0:
                    print("you have died, game over")
                    #back to menu with no resources or anything
                else:
                    #doc does not say?
            else:
                print(enemy_fleeingDesc_success)

def userFlee():
        # choose 0 or 1 at random, to give a 50% chance to successfully flee or not
        escape = random.randint(0, 1)
        if escape == 0:
            print(enemy_fleeingDesc_failed)
        else:
            print(enemy_fleeingDesc_success)

cemetery()
#church()
#mausoleum()
#catacombs()
#lair()

#Keeps the turtle menu on the screen
turtle.mainloop()
