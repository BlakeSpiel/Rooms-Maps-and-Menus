import turtle
screen = turtle.Screen()
screen.title("Finding Bob")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

#TURTLE FUNCTIONS
def cemetery():
  t.penup()
  t.goto(0, 200)
  t.pendown()
  t.left(108)
  for _ in range(2):
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)

def church():
  t.penup()
  t.goto(100, 0)
  t.pendown()
  t.goto(200, -50)
  t.pendown()
  t.right(108)
  for _ in range(5):
    t.forward(70)
    t.right(72)
    t.forward(70)
    t.left(144)

    print("""
      “The door creaks as you enter the church, 
      and the moon lights up the inside of the building 
      through the cracks in the roof. It looks as if the building 
      could fall apart at any moment.”
    """)

#def catacombs():

#MENU FUNCTION
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

church()
cemetery()
menu()






turtle.mainloop()
