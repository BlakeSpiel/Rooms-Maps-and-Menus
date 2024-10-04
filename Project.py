#INITALIZING THE TURTLE FOR USE LATER
import turtle
screen = turtle.Screen()
screen.title("Finding Bob")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Defining the menu function
def menu():
   print('---Menu---')
   print('1. Display Rules')
   print('2. PLay Game')
   print('3. Settings')
   print('4. Exit')
   # Asking the user what they would like to do within the menu
   menuInput = int(input('What would you like to do? (1, 2, or 3)'))
   # If the user chooses 1 then the rules are displayed
   if menuInput == 1:
       # Running the function that displays the rules
       display_rules()
       # Brining the user back to the menu
       menu()
   # If the user chooses 2 then the game is played
   elif menuInput == 2:
       # Running the function that is the game
       play_findingbob()
   # If user chooses 3 then the settings menu is displayed
   elif menuInput == 3:
       # Running the function that displays the settings menu
       display_settings()
   # If user chooses 4 then they are exited from the program
   elif menuInput == 4:
       print('Thanks for playing Finding Bob!')
       # Exiting the program
       exit(1)
   # If the user enters an invalid input then they are directed back to the menu
   else:
       print('Please enter a valid response')
       # Directing the user back to the menu
       menu()


#TURTLE FUNCTIONS DRAWING DIFFERENT ROOMS
def cemetery():
  tWriting()
  t.write("""
        In the cemetery, you come across graves, and a mausoleum to the west. The cemetery is enclosed with a picket fence. 
        You are unable to see the end of the cemetery from where you are standing. Walking back toward the entrance the fog thins out 
        As you venture into the cemetery the fog gets thicker, and you feel as if you are being watched. 
        You see a small church towards the east of the cemetery through the thick fog. There are nothing but dead trees and graves around.
    """)
  t.penup()
  t.goto(-100, 200)
  t.pendown()
  for _ in range(2):
    t.forward(200)
    t.right(90)
  for _ in range(2):
    t.forward(75)
    t.penup()
    t.forward(50)
    t.pendown()
    t.forward(75)
    t.right(90)

def church():
  tWriting()
  t.write("""
        The door creaks as you enter the church, 
        and the moon lights up the inside of the building 
        through the cracks in the roof. It looks as if the building 
        could fall apart at any moment.
    """)
  t.penup()
  t.goto(0, 200)
  t.pendown()
  t.right(108)
  t.penup()
  for _ in range(4):
    t.forward(70)
    t.right(72)
    t.pendown()
    t.forward(70)
    t.left(144)
  t.forward(70)
  t.right(180)

def mausoleum():
  tWriting()
  t.write("""
        The lock on the mausoleum clicks and it is now unlocked. You see a flimsy ladder that leads into darkness.” 
        When the player walks in… “As you take your step, the ladder collapses and you find yourself in a tunnel aligned with skulls on the wall… 
        There is no way back up. There are two long tunnels to the east and west. The tunnel north is concave in   
    """)
  t.penup()
  t.goto(-50, 150)
  t.pendown()
  for _ in range(2):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.penup()
    t.forward(40)
    t.pendown()
    t.forward(50)
    t.right(90)

def catacombs():
  tWriting()
  t.write("""
        The vast hallway looks the exact same as the others. It would be very easy to get lost.”
    """)
  t.penup()
  t.goto(-60, 120)
  t.pendown()
  t.forward(120)
  t.right(90)
  for i in range(2):
    t.forward(40)
    t.penup()
    t.forward(40)
    t.pendown()
    t.forward(40)
    t.right(90)
  t.forward(120)
  t.right(90)

def lair():
  tWriting()
  t.write("""
        Against your gut, you open the door, and you enter a giant vast lair that is well lit with your friend Bob standing in the middle. It’s Bobby!
    """)
  t.penup()
  t.goto(-35, 00)
  t.pendown()
  for _ in range(8):
    t.forward(70)
    t.left(45)

#Places the cursor on the bottom for text
def tWriting():
  t.clear()
  t.penup()
  t.goto(-400, -200)
  t.pendown()
  
#cemetary()
#church()
#mausolum()
#catacombs()
#lair()

#Keeps the turtle menu on the screen
turtle.mainloop()
