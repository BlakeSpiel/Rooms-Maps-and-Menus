import turtle
screen = turtle.Screen()
screen.title("Finding Bob")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


#Functions for the different rooms
#def frontCemetery():
  
  
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

#def entranceCatacombs():

#def eastCatacombs():


church()
cemetery()







turtle.mainloop()
