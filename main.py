import random
from turtle import *

s = Screen()
s.setup(500, 500)
# t = Turtle()
# t2 = Turtle()
# t3 = Turtle()
# t4 = Turtle()
# t.shape("turtle")
# t.color("Red")
# s.setup(500, 500)
# def move():
#     t.forward(10)
#
# def backward():
#     t.back(10)
# t.penup()
# t.setpos(-250, 10)

# how to use event listeners
#  1 call listen method on screen
# 2 call onkey method which epects a key to be pressed and a function to be called as parameter

# first we will make screen listen with method listen
s.listen()

#
# # and now event listener is used where there are two parameters
# # #  first one is key and the second one is the function call
# # s.onkey(key="space",fun=move)
# # s.onkey(key="w",fun=backward)
#
#
# # creating Etch a Sketch App
# def forward():
#     t.forward(10)
#
#
# def backward():
#     t.back(10)
#
#
# def right():
#     t.right(10)
#
#
# def left():
#     t.left(10)
#
#
# def clear():
#     t.clear()
#
#
# # def user_input(key,func):
# #     s.onkey(key=key,fun=func)
# #
# #
# # pos=input()
# # function
# # user_input()
#
#
# s.onkey(key="w", fun=forward)
# s.onkey(key="s", fun=backward)
# s.onkey(key="d", fun=right)
# s.onkey(key="a", fun=left)
# s.onkey(key="c", fun=clear)
# player_Guess = s.textinput("Player1", "Who Will Win")
#
# t2.shape("turtle")
# t2.color("blue")
# t2.setpos(-240, 40)
#
# t3.shape('turtle')
# t3.color("Brown")
# t.setpos(-240, 80)
#
# t4.shape("turtle")
# t4.color("Yellow")
# t.setpos(-240, 100)

user_bet=s.textinput("String","Which Color Player win")
# For movement of the turtle below function is used
def movement(turtle_given):
    race_on = True
    for _ in range(10):
        while race_on:
         for turtle in all_turtles:
          # turtle.speed(random.randint(1,5))
          turtle.forward(random.randint(1,10))
          if turtle.xcor()>220:
              race_on=False
              winner=turtle.pencolor()
              if user_bet==winner:
               print(f"You Won {winner} is winner")
              else:
                  print(f"You Lose {winner} is winner ")


# below is a variable created so that we can use it have random postions
random_position = 5
colors_for_Turtle = ['Red', 'Yellow', 'Black', 'Brown', 'Green','Silver']
# names_for_object = ["Ahmad", "Rashid", "Khalil", "Shahid", "Zayn"]
all_turtles = []
for i in range(6):
    # 1 Creating Player Objects
    player = Turtle(shape="turtle")
    all_turtles.append(player)
    # 2 Selecting Random Colors
    selected_color = colors_for_Turtle[i]
    player.penup()
    player.color(selected_color)

    # 3 Random Positons
    # 3.1 Random Gaps btw the Players
    random_position = random_position + 35
    # 3.2 Setting Positions to start of the screen for starting the race
    player.setpos(-230, random_position)
print(all_turtles)
#     4 Calling Function for movements of the players
#
#      1st Main Problemcc
# The Main problem that I faced was that I was not able to move all turtles at the same time only one turtle was moving
#
#      2nd Main problem
# I was creating turtle objects through loop so it was not possible to pick everyone manually
#
#    so we created a list and appended those objects in that


movement(all_turtles)
s.exitonclick()
